# -*- coding: utf-8 -*-

import pickle

from os import path

import jieba

import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

comment = []
with open('quan.txt', mode = 'r', encoding='utf-8') as f:
	lines = f.readlines()
	for line in lines:
		arr = line.split(',')
		if len(arr) == 5:
			comment.append(arr[4].replace('\n',''))

	# comment_after_split = jieba.cut(str(comment),cut_all=False)
	# wl_space_split = ''.join(comment_after_split)		
	# wordcloud=WordCloud(font_path="fyuan.ttf",background_color="black",width=600,height=300,max_words=50).generate(wl_space_split)
	# #3.生成图片
	# image=wordcloud.to_image()
	# #4.显示图片
	# image.show()

comment_after_split = jieba.cut(str(comment),cut_all=False)
wl_space_split = ' '.join(comment_after_split)		
# # print(wl_space_split)
backgroud_Image = plt.imread('IMG_3246.JPG')

# 设置屏蔽词
stopwords = STOPWORDS.copy()
stopwords.add('电影')
stopwords.add('一部')
stopwords.add('里面')
stopwords.add('讲')
stopwords.add('是')
stopwords.add('有点')
stopwords.add('还是')
stopwords.add('这部')
stopwords.add('真的')
stopwords.add('也许')
stopwords.add('可能')
stopwords.add('之后')

# 设置词云的字体，背景色，最大词大小，背景图
wc = WordCloud(width=1024, height=768, 
	background_color='white',
	mask=backgroud_Image, 
	font_path='fyuan.ttf',
	stopwords=stopwords,
	max_font_size = 400,
	random_state = 50
	)

wc.generate_from_text(wl_space_split)
img_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func=img_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()

wc.to_file('./image.jpg')









