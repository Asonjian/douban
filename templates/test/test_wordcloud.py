#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：633.html 
@File    ：test_wordcloud.py.py
@Author  ：安健
@Date    ：2021/12/26 23:29 
'''
import jieba        # 结巴分词
from matplotlib import pyplot as plt    #数据可视化
from wordcloud import WordCloud         #词云
from PIL import Image                   #图片处理
import numpy as np                      #数组矩阵运算
import pymysql                          #数据库操作
import re


conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123', db='top_list1')
cursor = conn.cursor()  # 建立一个游标
sql = "select introduct from data_list"
cursor.execute(sql)
data = cursor.fetchall()
text=""
for item in data:
    try:
        a=re.sub('[\s]', '', item[0])
        a_list=a.split("...")
        b=a_list[1]
        b=b.replace('/','')
        text=text+b
    except:
        continue
cursor.close()
conn.close()
##分词
cut=jieba.cut(text)
string=' '.join(cut)
img=Image.open('./tree.jpg')
img_array=np.array(img)
wc=WordCloud(
    background_color='white',
    mask=img_array,
    font_path="STXINGKA.TTF"
)
wc.generate_from_text(string)
#绘制图片
fig=plt.figure(1)
plt.imshow(wc)
plt.axis('off')
#输出图片
plt.savefig(r'.\word2.jpg',dpi=500)
