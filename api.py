import flask
from flask import request, jsonify
import json
import collections
import pandas as pd
import psycopg2


app = flask.Flask(__name__)
app.config["DEBUG"] = True


def make_array(favicon):
    favicon_arr = favicon.split(',')
    return favicon_arr


@app.route('/api/v1/resources/sites', methods=['GET'])
def site_list():
    conn = psycopg2.connect(host="35.192.137.149",database="newsdata", user="postgres", password="ho1234")
    c = conn.cursor()
    items = []
    with conn:
        c.execute(
            """SELECT distinct s.Id, s.Name, s.favicon
                FROM News AS n
                LEFT JOIN Site AS s ON n.SiteId= s.Id 
                ORDER BY PubTime DESC""")
        for row in c.fetchall():
            s['id'] = row[0]
            s['name'] = row[1]
            s['image'] = row[2]
            items.append(s)
        return json.dumps(items)

app.run(host='127.0.0.1', port=8003, debug=True)
