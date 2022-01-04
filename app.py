#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：douban_flask 
@File    ：app.py.py
@Author  ：安健
@Date    ：2021/12/23 14:40 
'''
from flask import Flask,render_template
import pymysql

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/index')
def home():
    return render_template("index.html")
@app.route('/movies')
def movie():
    data_list = []
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123', db='top_list1')
    cursor = conn.cursor()  # 建立一个游标
    sql="select * from data_list"
    cursor.execute(sql)
    data = cursor.fetchall()
    for item in data:
        data_list.append(item)
    cursor.close()
    conn.close()
    return render_template("movies.html",list=data_list)
@app.route('/scores')
def scores():
    score_list=[]   ##所有评分有多少种
    num_list=[]  #分数对应的电影数目
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123', db='top_list1')
    cursor = conn.cursor()  # 建立一个游标
    sql="select scores,count(scores) from data_list group by scores"  # 从top_list中获取score的值并分组
    cursor.execute(sql)
    data = cursor.fetchall()
    for item in data:
        score_list.append(item[0])
        num_list.append(item[1])
    return render_template("scores.html",score_list=score_list,num_list=num_list)
@app.route('/wordcloud')
def wordcloud():
    return render_template("wordcloud.html")
@app.route('/team')
def team():
    return render_template("team.html")
@app.route('/test_echarts')
def test_echarts():
    return render_template("/test/test_echarts.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000,debug=True)
