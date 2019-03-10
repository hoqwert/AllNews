import flask
from flask import request, jsonify
import sqlite3
import json
import collections
import logging
import pandas as pd


app = flask.Flask(__name__)
app.config["DEBUG"] = True


def make_array(favicon):
    favicon_arr = favicon.split(',')
    return favicon_arr


@app.route('/api/v1/resources/sites', methods=['GET'])
def site_list():
    conn = sqlite3.connect('NewsData.db')
    c = conn.cursor()
    items = []
    with conn:
        c.execute(
            """SELECT distinct s.Id, s.Name, s.favicon
                FROM News AS n
                LEFT JOIN Site AS s ON n.SiteId= s.Id 
                ORDER BY PubTime DESC""")
        for row in c.fetchall():
            s = collections.OrderedDict()
            s['id'] = row[0]
            s['name'] = row[1]
            s['image'] = row[2]
            items.append(s)
        return json.dumps(items)

@app.route('/api/v1/resources/categories', methods=['GET'])
def category_list():
    conn = sqlite3.connect('NewsData.db')
    c = conn.cursor()
    items = []
    with conn:
        c.execute(
            """SELECT distinct c.Id, c.Name, c.Color
                           FROM Category c""")
        for row in c.fetchall():
            s = collections.OrderedDict()
            s['id'] = row[0]
            s['name'] = row[1]
            s['color'] = row[2]
            items.append(s)
        return json.dumps(items)

@app.route('/api/v1/resources/news', methods=['GET'])
def news_list():
    conn = sqlite3.connect('NewsData.db')
    c = conn.cursor()
    items = []
    page = request.args.get('paging')
    categoryId = request.args.get('categoryId')
    if page is None or not page.isdigit():
        page = "0"
    if categoryId is None or not categoryId.isdigit():
        categoryId = "0"

    select_string = """SELECT distinct
                            n.GroupId, s.favicon, n.Title, n.ImageLink, n.PubTime, n.Id, c.Name as CategoryName, s.Name as SiteName, c.Color, n.Link
                        FROM News AS n INNER JOIN Category  AS c ON n.Category = c.Id INNER JOIN Site AS s ON n.SiteId= s.Id
                        WHERE 
                            n.GroupId IN( SELECT n.GroupId
                    FROM News AS n INNER JOIN Category  AS c ON n.Category = c.Id
                    INNER JOIN News AS n2  ON n2.groupId = n.groupId INNER JOIN Site AS s ON n2.SiteId= s.Id """
    if categoryId != "0":
        select_string = select_string + " WHERE c.Id = {categoryId}"

    select_string += " GROUP BY n.GroupId ORDER BY n2.PubTime DESC LIMIT {page},10 )"
    select_string = select_string.replace("{page}", page)
    select_string = select_string.replace("{categoryId}", categoryId)
    print(select_string)
    dataGroupId = []
    items = []

    with conn:
        sqldata = pd.read_sql_query(select_string, conn)
        data = sqldata.groupby('GroupId')
        for ii in data:
            dataGroupId.append(ii[0])
        for jj in dataGroupId:
            s = collections.OrderedDict()
            s["GroupId"] = jj
            s["NewsList"] = []
            favList = []
            sfdata = (sqldata[sqldata['GroupId'] == jj]).values.tolist()
            for sf in sfdata:
                f = collections.OrderedDict()
                f['groupId'] = sf[0]
                f['favicon'] = sf[1]
                f['title'] = sf[2]
                f['imageLink'] = sf[3]
                f['pubTime'] = sf[4]
                f['newsid'] = sf[5]
                f['category'] = sf[6]
                f['site'] = sf[7]
                f['color'] = sf[8]
                f['link'] = sf[9]
                s["NewsList"].append(f)
                favList.append(sf[1])
            s["Favicon"] = favList
            items.append(s)
    return json.dumps(items)


@app.route('/api/v1/resources/news_detail', methods=['GET'])
def news_detail():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    conn = sqlite3.connect('NewsData.db')
    c = conn.cursor()
    items = []
    with conn:
        c.execute(
            """SELECT n.Id, n.Link, n.Title, n.Description, n.ImageLink,  n.PubTime, s.SiteUrl, s.FavIcon, c.Color, s.Name, c.Name, GROUP_CONCAT(distinct s.favicon)
            FROM News AS n
            INNER JOIN News AS n2 ON n.GroupId = n2.GroupId
            INNER JOIN Category AS c ON n.Category = c.Id
            INNER JOIN Site AS s ON n2.SiteId= s.Id
            WHERE n.Id = """ + str(id) +
            " GROUP BY n.GroupId ORDER BY n2.PubTime DESC")

        for row in c.fetchall():
            d = collections.OrderedDict()
            d['newsid'] = row[0]
            d['link'] = row[1]
            d['title'] = row[2]
            d['description'] = row[3]
            d['imageLink'] = row[4]
            d['pubtime'] = row[5]
            d['siteurl'] = row[6]
            d['favicon'] = row[7]
            d['color'] = row[8]
            d['site'] = row[9]
            d['category'] = row[10]
            d['faviconList'] = make_array(row[11])

            items.append(d)
        return json.dumps(items)


app.run(host='127.0.0.1', port=8003, debug=True)
