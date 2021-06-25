#!/usr/bin/python3
# coding:utf-8

'''
天门帝国7小说爬取
'''

import requests
import re
for i in range(1587,9999):
	url = 'https://m.wandu.cn/bd/get_chapter_info/20548/{}?display=json&stat=0'.format(i)
	req = requests.get(url)
	#print(req.json())
	req1 = req.json()
	#print(req1)
	title = req1['data']['title']
	if title != None:
		content = req1['data']['content']
		content1 = re.sub(r'</p>', '\n', re.sub(r'<\w+?>', '\v', re.sub(r'<p></p>', '', content)))
		# print(title)
		# print(content1)
		with open('/Users/han/Desktop/test.txt', 'a+') as f:
			f.write(title + '\n' + content1)
		print("拉取第{}章完成".format(i-1))
	else:
		print("只有{}章".format(i-1))
		break
