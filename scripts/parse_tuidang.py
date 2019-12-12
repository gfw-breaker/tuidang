#!/usr/bin/python
# coding: utf-8

import macros
import sys
import os
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

channel = sys.argv[1]
channel_url = sys.argv[2]

index_page = '' + macros.head
links = macros.tail


def get_content(link):

	# get post image
	response = requests.get(link)
	text = response.text.encode('utf-8')
	parser = BeautifulSoup(text, 'html.parser')
	body = parser.find(id='artbody')

	for header in body.find_all('header'):
		header.decompose()
	for aside in body.find_all('aside'):
		aside.decompose()

	return body.prettify().encode('utf-8')


def get_name(link):
	fname = link.split('/')[-1]
	return fname.split('.')[0]


def keep_updating(title):
	return title.find('更新') > -1


index_text = requests.get(channel_url).text.encode('utf-8')
index_html = BeautifulSoup(index_text, 'html.parser')
articles = index_html.find(id='artlist').find_all('div', attrs = {'class': 'arttitle'})
for article in articles:
	a_links = article.find_all('a')
	link = a_links[0]
	a_url = link.get('href').encode('utf-8')
	a_title = link.text.encode('utf-8').strip()
	print a_title
	print a_url
	name = get_name(a_url) + '.md'
	file_path = '../pages/' + channel + '/' + name 
	#content = get_content(a_url)

	#if not os.path.exists(file_path):
	if True:
		print file_path
		content = get_content(a_url)
		macros.write_page(channel, name, file_path, a_title, a_url, content)
	index_page += '#### [' + a_title + '](' + file_path + ') \n'


index_file = open('../indexes/' + channel + '.md', 'w')
index_file.write(index_page)
index_file.close()

