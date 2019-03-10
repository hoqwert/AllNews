#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 22:56:04 2018

@author: Hoyri
"""

import feedparser
import dateutil.parser as dp
import sqlite3


conn = sqlite3.connect('NewsData.db')
c = conn.cursor()   


def create_newsSite():
    with conn:
        c.execute("""CREATE TABLE Site(
                Name text,
                Url text,
                Isactive number
                )""")


def drop_newsSite():
    with conn:
        c.execute("DROP TABLE Site")


def insert_newsSite():
    with conn:
        c.execute("INSERT INTO Site VALUES ('Habertürk', 'http://www.haberturk.com/rss',1)")


def select_newsSite():
    with conn:
        c.execute("SELECT Name, Url FROM Site")
        return c.fetchall()


def create_news():
    with conn:
        c.execute("""CREATE TABLE News (
                    SiteName text,
                    Title text,
                    Description text,
                    Link text,
                    ImageLink text,
                    TimeSpan number
                    )""")


def insert_news(sitename, title, description, link, imageLink, timespan):
    with conn:
        c.execute("INSERT INTO News (SiteName, Title, Description, Link, ImageLink, TimeSpan) VALUES (:sitename, :title, :description, :link, :imagelink, :timespan)", {'sitename': sitename, 'title': title, 'description': description, 'link': link, 'imagelink': imageLink, 'timespan': timespan})


def select_news():
    with conn:
        c.execute("SELECT Description FROM News")
        return c.fetchall()


def delete_news():
    with conn:
        c.execute("DELETE FROM News")


def drop_news():
    with conn:
        c.execute("DROP TABLE News")


def GetFromImageTag(item):
    print("-----")
    if item["image"] == None:
        img = "" 
    else: 
        img = item["image"]
    return img


def GetFromEnclosure(item):
    print(item.enclosure)
    return item.find(['enclosure', 'g:image_link'])


def GetFromDescription(item):
    #imageText = description[description.find("<img")+4:description.find("/>")-1]
    #imageSrc = imageText[imageText.find("src")+5:imageText.find(">")]
    return " "


def GetImageUrl(site, item):
    return {
            'Habertürk': GetFromImageTag(item)
            }.get(site, '')


drop_news()
create_news()
drop_newsSite()
create_newsSite()
insert_newsSite()
newsLink = select_newsSite()

for name, url in newsLink:
    d = feedparser.parse(url)
    for val in d.entries:
        #parsed_t = dp.parse(val.published)
        #t_in_seconds = parsed_t.strftime('%s')
        imageUrl = GetImageUrl(name, val)
        insert_news('', val.title, imageUrl, val.link, '', 0)
        print(select_news())

conn.close()
