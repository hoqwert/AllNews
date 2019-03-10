# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser as date_parser
import sqlite3
import html.parser
from cleanHtmlContent import *

h = html.parser.HTMLParser()

conn = sqlite3.connect('news/api/NewsData.db')
c = conn.cursor()


def create_newsSite():
    with conn:
        c.execute("""CREATE TABLE Site(
                Id number,
                Name text,
                SiteUrl text,
                Favicon text,
                SourceUrl text,
                IsActive number,
                Category number
                )""")

def create_newsCategory():
    with conn:
        c.execute("""CREATE TABLE Category(
                Id number,
                Name text,
                Color text
                )""")


def drop_newsSite():
    with conn:
        c.execute("DROP TABLE Site")

def drop_news_category():
    with conn:
        c.execute("DROP TABLE Category")


def insert_news_category():
    with conn:
        c.execute("INSERT INTO Category VALUES (1, 'Dünya', '#007ABF')")
        c.execute("INSERT INTO Category VALUES (2, 'Ekonomi', '#34CAD6')")
        c.execute("INSERT INTO Category VALUES (3, 'Siyaset', '#F7382D')")
        c.execute("INSERT INTO Category VALUES (4, 'Gündem', '#88A824')")
        c.execute("INSERT INTO Category VALUES (5, 'Son Dakika', '#FD5015')")
        c.execute("INSERT INTO Category VALUES (6, 'Anasayfa', '#FE6E23')")
        c.execute("INSERT INTO Category VALUES (7, 'Manşet', '#FE6E23')")
        c.execute("INSERT INTO Category VALUES (8, 'Yazarlar', '#EBD20C')")

def insert_newsSite():
    with conn:
        c.execute("INSERT INTO Site VALUES (1, 'A Haber','http://www.ahaber.com.tr' ,'ahaber' , 'https://www.ahaber.com.tr/rss/gundem.xml',1, 4)")
        c.execute("INSERT INTO Site VALUES (1, 'A Haber','http://www.ahaber.com.tr' ,'ahaber' , 'https://www.ahaber.com.tr/rss/anasayfa.xml',1, 6)")
        c.execute("INSERT INTO Site VALUES (1, 'A Haber','http://www.ahaber.com.tr' ,'ahaber' , 'https://www.ahaber.com.tr/rss/ekonomi.xml',1, 2)")
        c.execute("INSERT INTO Site VALUES (1, 'A Haber','http://www.ahaber.com.tr' ,'ahaber' , 'https://www.ahaber.com.tr/rss/dunya.xml',1, 1)")
        c.execute("INSERT INTO Site VALUES (1, 'A Haber','http://www.ahaber.com.tr' ,'ahaber' , 'https://www.ahaber.com.tr/rss/haberler.xml',1, 7)")

        c.execute("INSERT INTO Site VALUES (2, 'Cnn Türk','https://www.cnnturk.com', 'cnnturk', 'https://www.cnnturk.com/feed/rss/news',1, 4)")

        #c.execute("INSERT INTO Site VALUES (3, 'Cumhuriyet','http://www.cumhuriyet.com.tr', 'http://www.cumhuriyet.com.tr/favicon.ico', 'http://www.cumhuriyet.com.tr/rss/son_dakika.xml',1, 5)")
        #c.execute("INSERT INTO Site VALUES (3, 'Cumhuriyet','http://www.cumhuriyet.com.tr', 'http://www.cumhuriyet.com.tr/favicon.ico', 'http://www.cumhuriyet.com.tr/rss/1.xml',1, 6)")
        #c.execute("INSERT INTO Site VALUES (3, 'Cumhuriyet','http://www.cumhuriyet.com.tr', 'http://www.cumhuriyet.com.tr/favicon.ico', 'http://www.cumhuriyet.com.tr/rss/5.xml',1, 1)")
        #c.execute("INSERT INTO Site VALUES (3, 'Cumhuriyet','http://www.cumhuriyet.com.tr', 'http://www.cumhuriyet.com.tr/favicon.ico', 'http://www.cumhuriyet.com.tr/rss/6.xml',1, 2)")
        #c.execute("INSERT INTO Site VALUES (3, 'Cumhuriyet','http://www.cumhuriyet.com.tr', 'http://www.cumhuriyet.com.tr/favicon.ico', 'http://www.cumhuriyet.com.tr/rss/2.xml',1, 7)")

        c.execute("INSERT INTO Site VALUES (4, 'Dünya', 'https://www.dunya.com', 'dunya', 'https://www.dunya.com/rss', 1, 4)")

        c.execute("INSERT INTO Site VALUES (5, 'Diriliş', 'http://www.dirilishaber.org', 'dirilishaber', 'http://www.dirilishaber.org/rss/gundem/5.xml',1, 4)")

        c.execute("INSERT INTO Site VALUES (6, 'Evrensel','https://www.evrensel.net', 'evrensel', 'https://www.evrensel.net/rss/haber.xml',1, 4)")
        c.execute("INSERT INTO Site VALUES (6, 'Evrensel','https://www.evrensel.net', 'evrensel', 'https://www.evrensel.net/rss/haber_guncel.xml',1, 4)")
        c.execute("INSERT INTO Site VALUES (6, 'Evrensel','https://www.evrensel.net', 'evrensel', 'https://www.evrensel.net/rss/haber_ekonomi.xml',1, 2)")
        c.execute("INSERT INTO Site VALUES (6, 'Evrensel','https://www.evrensel.net', 'evrensel', 'https://www.evrensel.net/rss/haber_politika.xml',1, 3)")
        c.execute(
            "INSERT INTO Site VALUES (7, 'En Son Haber','http://www.ensonhaber.com', 'ensonhaber', 'http://www.ensonhaber.com/rss/ensonhaber.xml',1, 4)")
        #hata verdi#c.execute("INSERT INTO Site VALUES (8, 'Güneş','http://www.gunes.com', 'http://www.gunes.com/favicon.ico', 'http://www.gunes.com/XmlRss',1, 4)")

        c.execute("INSERT INTO Site VALUES (9, 'Hürriyet','http://www.hurriyet.com.tr', 'hurriyet', 'http://www.hurriyet.com.tr/rss/gundem', 1, 4)")
        c.execute("INSERT INTO Site VALUES (9, 'Hürriyet','http://www.hurriyet.com.tr', 'hurriyet', 'http://www.hurriyet.com.tr/rss/anasayfa', 1, 6)")
        c.execute("INSERT INTO Site VALUES (9, 'Hürriyet','http://www.hurriyet.com.tr', 'hurriyet', 'http://www.hurriyet.com.tr/rss/ekonomi', 1, 2)")

        # c.execute("INSERT INTO Site VALUES (10, 'Haber7', 'http://sondakika.haber7.com/sondakika.rss',1)")
        # c.execute("INSERT INTO Site VALUES (11, 'Habertürk', 'https://www.haberturk.com/rss/manset.xml',1)")
        c.execute(
            "INSERT INTO Site VALUES (12, 'Haberler', 'https://www.haberler.com', 'haberler', 'https://rss.haberler.com/rss.asp?kategori=sondakika',1, 5)")
        # c.execute("INSERT INTO Site VALUES (13, 'InternetHaber', 'http://www.internethaber.com/rss',1)")
        #c.execute("INSERT INTO Site VALUES (14, 'Karar','http://www.karar.com', 'http://www.karar.com/favicon.ico', 'http://www.karar.com/rss/otomatik-rss',1, 4)")
        c.execute(
            "INSERT INTO Site VALUES (15, 'Milliyet','http://www.milliyet.com.tr', 'milliyet', 'http://www.milliyet.com.tr/rss/rssNew/gundemRss.xml',1, 4)")
        c.execute(
            "INSERT INTO Site VALUES (15, 'Milliyet','http://www.milliyet.com.tr', 'milliyet', 'http://www.milliyet.com.tr/rss/rssNew/ekonomiRss.xml',1, 2)")
        c.execute(
            "INSERT INTO Site VALUES (15, 'Milliyet','http://www.milliyet.com.tr', 'milliyet', 'http://www.milliyet.com.tr/rss/rssNew/siyasetRss.xml',1, 3)")
        c.execute(
            "INSERT INTO Site VALUES (16, 'Ntv','https://www.ntv.com.tr', 'ntv', 'https://www.ntv.com.tr/gundem.rss',1, 4)")
        c.execute(
            "INSERT INTO Site VALUES (17, 'Mynet','https://www.mynet.com', 'mynet', 'http://www.mynet.com/haber/rss/son-dakika',1, 5)")
        c.execute(
            "INSERT INTO Site VALUES (18, 'Milli Gazete', 'https://www.milligazete.com.tr', 'milligazete',  'https://www.milligazete.com.tr/rss',1, 4)")
        c.execute(
            "INSERT INTO Site VALUES (19, 'Onedio', 'https://onedio.com', 'onedio', 'https://onedio.com/support/rss.xml?category=50187b5d295c043264000144',1, 4)")
        # c.execute("INSERT INTO Site VALUES (20, 'Türkiye', 'http://www.turkiyegazetesi.com.tr/rss/rss.xml',1)")

        c.execute("INSERT INTO Site VALUES (21, 'Takvim', 'https://www.takvim.com.tr', 'takvim', 'https://www.takvim.com.tr/rss/son24saat.xml',1, 4)")
        c.execute("INSERT INTO Site VALUES (21, 'Takvim', 'https://www.takvim.com.tr', 'takvim', 'https://www.takvim.com.tr/rss/ekonomi.xml',1, 2)")
        c.execute("INSERT INTO Site VALUES (21, 'Takvim', 'https://www.takvim.com.tr', 'takvim', 'https://www.takvim.com.tr/rss/anasayfa.xml',1, 6)")
        c.execute("INSERT INTO Site VALUES (21, 'Takvim', 'https://www.takvim.com.tr', 'takvim', 'https://www.takvim.com.tr/rss/guncel.xml',1, 4)")
        #c.execute("INSERT INTO Site VALUES (21, 'Takvim', 'https://www.takvim.com.tr', 'https://www.takvim.com.tr/favicon.ico', 'https://www.takvim.com.tr/rss/yazarlar.xml',1, 8)")

        c.execute("INSERT INTO Site VALUES (22, 'Star','http://www.star.com.tr', 'star', 'http://www.star.com.tr/rss/sondakika.xml',1, 5)")
        c.execute("INSERT INTO Site VALUES (22, 'Star','http://www.star.com.tr', 'star', 'http://www.star.com.tr/rss/mansetler.xml',1, 4)")
        #yazar# c.execute("INSERT INTO Site VALUES (22, 'Star','http://www.star.com.tr', 'http://www.star.com.tr/favicon.ico', 'http://www.star.com.tr/rss/yazarlar.xml',1, 8)")
        c.execute("INSERT INTO Site VALUES (22, 'Star','http://www.star.com.tr', 'star', 'http://www.star.com.tr/rss/guncel.xml',1, 4)")
        c.execute("INSERT INTO Site VALUES (22, 'Star','http://www.star.com.tr', 'star', 'http://www.star.com.tr/rss/politika.xml',1, 3)")
        c.execute("INSERT INTO Site VALUES (22, 'Star','http://www.star.com.tr', 'star', 'http://www.star.com.tr/rss/dunya.xml',1, 1)")

        c.execute("INSERT INTO Site VALUES (23, 'Sputnik Türkiye','https://tr.sputniknews.com', 'sputniktr', 'https://tr.sputniknews.com/export/rss2/archive/index.xml',1, 4)")

        c.execute("INSERT INTO Site VALUES (24, 'Sabah','https://www.sabah.com.tr', 'sabah', 'https://www.sabah.com.tr/rss/gundem.xml',1, 4)")
        c.execute("INSERT INTO Site VALUES (24, 'Sabah','https://www.sabah.com.tr', 'sabah', 'https://www.sabah.com.tr/rss/ekonomi.xml',1, 2)")
        c.execute("INSERT INTO Site VALUES (24, 'Sabah','https://www.sabah.com.tr', 'sabah', 'https://www.sabah.com.tr/rss/dunya.xml',1, 1)")
        c.execute("INSERT INTO Site VALUES (24, 'Sabah','https://www.sabah.com.tr', 'sabah', 'https://www.sabah.com.tr/rss/anasayfa.xml',1, 6)")
        c.execute("INSERT INTO Site VALUES (24, 'Sabah','https://www.sabah.com.tr', 'sabah', 'https://www.sabah.com.tr/rss/sondakika.xml',1, 5)")

        #"Unknown string format:", timestr# c.execute("INSERT INTO Site VALUES (25, 'Vatan', 'gazetevatan', 'http://www.gazetevatan.com/favicon.ico', 'http://www.gazetevatan.com/rss/gundem.xml',1, 4)")
        #"Unknown string format:", timestr# c.execute("INSERT INTO Site VALUES (25, 'Vatan', 'gazetevatan', 'http://www.gazetevatan.com/favicon.ico', 'http://www.gazetevatan.com/rss/ekonomi.xml',1, 2)")
        #"Unknown string format:", timestr# c.execute("INSERT INTO Site VALUES (25, 'Vatan', 'gazetevatan', 'http://www.gazetevatan.com/favicon.ico', 'http://www.gazetevatan.com/rss/dunya.xml',1, 1)")

        c.execute("INSERT INTO Site VALUES (26, 'Yeni Asya','http://www.yeniasya.com.tr', 'yeniasya', 'http://www.yeniasya.com.tr/rss/manset',1, 7)")
        c.execute("INSERT INTO Site VALUES (26, 'Yeni Asya','http://www.yeniasya.com.tr', 'yeniasya', 'http://www.yeniasya.com.tr/rss/son-dakika',1, 5)")
        c.execute("INSERT INTO Site VALUES (26, 'Yeni Asya','http://www.yeniasya.com.tr', 'yeniasya', 'http://www.yeniasya.com.tr/rss/gundem',1, 4)")
        c.execute("INSERT INTO Site VALUES (26, 'Yeni Asya','http://www.yeniasya.com.tr', 'yeniasya', 'http://www.yeniasya.com.tr/rss/yurt-haber',1, 4)")
        c.execute("INSERT INTO Site VALUES (26, 'Yeni Asya','http://www.yeniasya.com.tr', 'yeniasya', 'http://www.yeniasya.com.tr/rss/dunya',1, 1)")
        c.execute("INSERT INTO Site VALUES (26, 'Yeni Asya','http://www.yeniasya.com.tr', 'yeniasya', 'http://www.yeniasya.com.tr/rss/politika',1, 6)")
        #c.execute("INSERT INTO Site VALUES (26, 'YeniAsya','http://www.yeniasya.com.tr', 'yeniasya', 'http://www.yeniasya.com.tr/rss/yazarlar',1, 8)")

        c.execute("INSERT INTO Site VALUES (27, 'Yeni Şafak','https://www.yenisafak.com', 'yeni_safak', 'https://www.yenisafak.com/Rss',1, 6)")
        c.execute("INSERT INTO Site VALUES (27, 'Yeni Şafak','https://www.yenisafak.com', 'yeni_safak', 'https://www.yenisafak.com/rss?xml=manset',1, 7)")
        c.execute("INSERT INTO Site VALUES (27, 'Yeni Şafak','https://www.yenisafak.com', 'yeni_safak', 'https://www.yenisafak.com/rss?xml=gundem',1, 4)")
        c.execute("INSERT INTO Site VALUES (27, 'Yeni Şafak','https://www.yenisafak.com', 'yeni_safak', 'https://www.yenisafak.com/rss?xml=ekonomi',1, 2)")
        c.execute("INSERT INTO Site VALUES (27, 'Yeni Şafak','https://www.yenisafak.com', 'yeni_safak', 'https://www.yenisafak.com/rss?xml=dunya',1, 1)")
        #yazar# c.execute("INSERT INTO Site VALUES (27, 'YeniŞafak','https://www.yenisafak.com', 'yenisafak', 'https://www.yenisafak.com/rss?xml=yazarlar',1, 7)")

        c.execute("INSERT INTO Site VALUES (28, 'Yeni Akit', 'https://www.yeniakit.com.tr', 'yeniakit', 'https://www.yeniakit.com.tr/rss/haber/gunun-mansetleri',1, 7)")
        c.execute("INSERT INTO Site VALUES (28, 'Yeni Akit', 'https://www.yeniakit.com.tr', 'yeniakit', 'https://www.yeniakit.com.tr/rss/haber',1, 7)")
        c.execute("INSERT INTO Site VALUES (28, 'Yeni Akit', 'https://www.yeniakit.com.tr', 'yeniakit', 'https://www.yeniakit.com.tr/rss/haber/bugunku-akit',1, 7)")
        c.execute("INSERT INTO Site VALUES (28, 'Yeni Akit', 'https://www.yeniakit.com.tr', 'yeniakit', 'https://www.yeniakit.com.tr/rss/haber/siyaset',1, 6)")
        c.execute("INSERT INTO Site VALUES (28, 'Yeni Akit', 'https://www.yeniakit.com.tr', 'yeniakit', 'https://www.yeniakit.com.tr/rss/haber/gundem',1, 4)")
        c.execute("INSERT INTO Site VALUES (28, 'Yeni Akit', 'https://www.yeniakit.com.tr', 'yeniakit', 'https://www.yeniakit.com.tr/rss/haber/ekonomi',1, 2)")
        c.execute("INSERT INTO Site VALUES (28, 'Yeni Akit', 'https://www.yeniakit.com.tr', 'yeniakit', 'https://www.yeniakit.com.tr/rss/haber/dunya',1, 1)")

        c.execute("INSERT INTO Site VALUES (29, 'Yeni Çağ', 'http://www.yenicaggazetesi.com.tr', 'yenicaggazetesi', 'http://www.yenicaggazetesi.com.tr/rss/',1, 4)")

        c.execute("INSERT INTO Site VALUES (30, 'Yeni Asır', 'https://www.yeniasir.com.tr', 'yeniasir', 'https://www.yeniasir.com.tr/rss/anasayfa.xml',1, 4)")
        c.execute("INSERT INTO Site VALUES (30, 'Yeni Asır', 'https://www.yeniasir.com.tr', 'yeniasir', 'https://www.yeniasir.com.tr/rss/Ekonomi.xml',1, 2)")
        c.execute("INSERT INTO Site VALUES (30, 'Yeni Asır', 'https://www.yeniasir.com.tr', 'yeniasir', 'https://www.yeniasir.com.tr/rss/YerelPolitika.xml',1, 6)")
        c.execute("INSERT INTO Site VALUES (30, 'Yeni Asır', 'https://www.yeniasir.com.tr', 'yeniasir', 'https://www.yeniasir.com.tr/rss/DisHaberler.xml',1, 1)")

        c.execute("INSERT INTO Site VALUES (31, 'Yurt Gazetesi', 'http://www.yurtgazetesi.com.tr', 'yurtgazetesi', 'http://www.yurtgazetesi.com.tr/rss.php',1, 4)")
        #c.execute("INSERT INTO Site VALUES (32, 'YeniSöz', 'http://www.yenisoz.com.tr', 'yenisoz.com.tr', 'http://www.yenisoz.com.tr/rss/',1, 4)")
        # c.execute("INSERT INTO Site VALUES (33, 'Sözcü', '',1, 4)")
        # c.execute("INSERT INTO Site VALUES (34, 'Haber7', '',1, 4)")
        # c.execute("INSERT INTO Site VALUES (35, 'GazeteVatan', '',1, 4)")
        # c.execute("INSERT INTO Site VALUES (36, 'Akşam', '',1, 4)")


def select_newsSite():
    with conn:
        c.execute('SELECT Id, Name, SiteUrl, Favicon, SourceUrl, Category  FROM Site')
        return c.fetchall()


def create_news():
    with conn:
        c.execute("""CREATE TABLE News (
                    Id INTEGER PRIMARY KEY,
                    SiteId number,
                    Title text,
                    Description text,
                    Link text,
                    ImageLink text,
                    PubTime text,
                    GroupId number,
                    Type number,
                    Stem text,
                    Category number
                    )""")


def insert_news(siteId, title, description, link, imageLink, pubTime, type, category):
    with conn:
        news = select_newsByLink(link)
        if news is None:
            c.execute(
                "INSERT INTO News (SiteId, Title, Description, Link, ImageLink, PubTime, Type, Category) VALUES (:siteId, :title, :description, :link, :imagelink, :pubtime, :type, :category)",
                {'siteId': siteId, 'title': title, 'description': description, 'link': link, 'imagelink': imageLink,
                 'pubtime': pubTime, 'type': type, 'category': category})
        else:
            c.execute(
                "UPDATE News SET ImageLink = :imageLink, Title= :title, PubTime = :pubTime, Description= :description WHERE Id = :id ",
                {'imageLink': imageLink, 'title': title, 'pubTime': pubTime, 'description': description, 'id': news[0]}
            )


def select_news():
    with conn:
        c.execute("SELECT s.Name, s.SiteUrl, s.Favicon, n.ImageLink, n.Title, n.PubTime FROM News n INNER JOIN Site s ON n.SiteId = s.Id")
        return c.fetchall()

def select_newsByLink(link):
    with conn:
        c.execute("SELECT Id FROM News WHERE Link = :link", {'link': link})
        return c.fetchone()

def delete_news():
    with conn:
        c.execute("DELETE FROM News")


def drop_news():
    with conn:
        c.execute("DROP TABLE News")


def GetFromImageWithUrlTag(item):
    if item.image is None:
        img = ""
    else:
        if item.image.url is None:
            img = ""
        else:
            img = item.image.url.text
    return img


def GetFromImageTag(item):
    if item.image is None:
        img = ""
    else:
        img = item.image.text
    return img


def GetFromImage2Tag(item):
    if item.find("img640x360") is None:
        img = ""
    else:
        img = item.find("img640x360").text
    return img


def GetNoImage():
    return ""


def GetFromEnclosure(item):
    if item.image is None:
        if item.find("enclosure", {"type": "image/jpeg"}) == None:
            ii = ""
        else:
            ii = item.find("enclosure", {"type": "image/jpeg"}).attrs["url"]
    else:
        ii = item.image.url
    return ii


def GetFromMedia(item):
    if item.image is None:
        if item.find("media:thumbnail") == None:
            ii = ""
        else:
            ii = item.find("media:thumbnail").attrs["url"]
    else:
        ii = item.image.url
    return ii


def GetFromDescription(item):
    # imageText = description[description.find("<img")+4:description.find("/>")-1]
    # imageSrc = imageText[imageText.find("src")+5:imageText.find(">")]
    return " "


def GetImageUrl(site, item):
    return {
        'Ahaber': GetNoImage(),
        'Milliyet': GetFromDescription(item),
        'NTV': GetFromDescription(item),
        'Habertürk': GetFromDescription(item),
        'YeniŞafak': GetFromImageWithUrlTag(item),
        'Sabah': GetFromEnclosure(item),
        'Hürriyet': GetFromEnclosure(item),
        'Star': GetFromImageTag(item),
        'Güneş': GetFromImageTag(item),
        'Dünya': GetFromDescription(item),
        'Vatan': GetFromDescription(item),
        'YeniAsya': GetFromEnclosure(item),
        'Cumhuriyet': GetFromEnclosure(item),
        'Haber7': GetFromDescription(item),
        'Takvim': GetNoImage(),
        'Milli Gazete': GetFromEnclosure(item),
        'Evrensel': GetFromDescription(item),
        'YeniAkit': GetFromDescription(item),
        'Diriliş': GetFromDescription(item),
        'YeniÇağ': GetFromDescription(item),
        'Türkiye': GetFromMedia(item),
        'YeniAsır': GetNoImage(),
        'Karar': GetFromEnclosure(item),
        'Yurt': GetFromImageTag(item),
        'YeniSöz': GetFromEnclosure(item),
        'EnSonHaber': GetFromImageTag(item),
        'InternetHaber': GetNoImage(),
        'Onedio': GetFromDescription(item),
        'Mynet': GetFromImage2Tag(item),
        'CnnTurk': GetFromImageTag(item),
        'SputnikTürkiye': GetFromEnclosure(item),
        'AA': GetFromImageTag(item),
        'Haberler': GetFromImageTag(item)
    }.get(site, '')


def get_news_data():
    print("'GetNewsData running...'")
    drop_news_category()
    create_newsCategory()
    insert_news_category()
    drop_news()
    create_news()
    drop_newsSite()
    create_newsSite()
    insert_newsSite()
    news_link = select_newsSite()

    fmt = "%Y-%m-%d %H:%M:%S"
    for Id, Name, SiteUrl, Favicon, SourceUrl, Category in news_link:
        print(Name)
        try:
            resp = requests.get(SourceUrl)
            soup = BeautifulSoup(resp.content, features="xml")
            items = soup.findAll('item')
            for item in items:
                parsed_t = datetime.strptime(date_parser.parse(u'' + item.pubDate.text + '').strftime("%Y-%m-%d %H:%M:%S"), fmt)
                #t_in_seconds = (dateNow - parsed_t).seconds / 60
                image_url = GetImageUrl(Name, item)
                insert_news(Id, cleanhtml(item.title.text), cleanhtml(item.description.text), item.link.text, image_url, parsed_t, 1, Category)
        except:
            print("error")
    print('GetNewsData run.')



