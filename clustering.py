# -*- coding: utf-8 -*-
import nltk
import nltk.corpus
import nltk.tokenize.punkt
import nltk.stem.snowball
import string 
import sqlite3
import json
from TurkishStemmer import TurkishStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import re
from sklearn.metrics.pairwise import cosine_similarity

conn = sqlite3.connect('news/api/NewsData.db')
c = conn.cursor()  


def update_newsGroup(groupId, Id):
    with conn:
        c.execute("UPDATE News SET GroupId = :groupId WHERE Id = :Id", {'groupId': groupId, 'Id': Id})


def update_newsStem(stem, id):
    with conn:
        c.execute("UPDATE News SET Stem = :stem WHERE Id = :id", {'stem': stem, 'id': id})


def select_newsAll():
    with conn:
        c.execute("SELECT Id, Title, Link FROM News")
        return c.fetchall()


def select_newsStem():
    with conn:
        c.execute("SELECT Id, Stem FROM News")
        return c.fetchall()


def select_newsGroup1():
    with conn:
        c.execute("SELECT Title, GroupId, Name FROM News n INNER JOIN Site s ON n.SiteId = s.Id  Order By GroupId")
        return c.fetchall()


# Get default English stopwords and extend with punctuation
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')


def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens


def get_stem(a):
    stemmer = TurkishStemmer()
    tokens_a = [token.lower().strip(string.punctuation) for token in tokenize(a)
                if token.lower().strip(string.punctuation) not in stopwords]
    stems_a = [stemmer.stem(token) for token in tokens_a]
    return stems_a


def get_stems():
    newsTitle = select_newsAll()

    for Id, title, link in newsTitle:
        stem = get_stem(title)
        update_newsStem(json.dumps(stem, ensure_ascii=False), Id)

    return select_newsStem()


def tokenize_and_stem(text):
    stemmer = TurkishStemmer()
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


def clearData(text):
    returnText = text
    if "[CDATA[" in text:
        returnText = text.replace("<![CDATA[", "")
        returnText = returnText.replace("]]>", "")
    return returnText


def cluster_news():
    print('clustering running...')
    threshold = 0.6
    newsSteam = get_stems()
    newsTitle = select_newsAll()
    sklearn_tfidf = TfidfVectorizer(norm='l2', min_df=0, use_idf=True, smooth_idf=False, sublinear_tf=True, tokenizer=tokenize)
    tfidf_matrix = sklearn_tfidf.fit_transform(t[1] for t in newsSteam)
    #terms = sklearn_tfidf.get_feature_names()
    result = cosine_similarity(tfidf_matrix)
    group_id = 0
    temp_group_id = 0
    group_list = {}
    for w, y, z in newsTitle:
        group_list.setdefault(w, [])

    for index1, i1 in enumerate(result):
        if not group_list[newsTitle[index1][0]]:
            group_id = group_id + 1
            temp_group_id = group_id
            group_list[newsTitle[index1][0]] = temp_group_id
        else:
            temp_group_id = group_list[newsTitle[index1][0]]
        for index2, i2 in enumerate(i1):
            if i2 > threshold:
                group_list[newsTitle[index2][0]] = temp_group_id
                
    flipped = {}

    for key, value in group_list.items():
        if value not in flipped:
            flipped[value] = [key-1]
        else:
            flipped[value].append(key-1)

    for a in flipped:
        for b in flipped[a]:
            update_newsGroup(a, (newsTitle[b][0]))

    print('clustering run.')


