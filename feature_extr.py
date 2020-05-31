# -*- coding: utf-8 -*-
"""
Created on Tue Feb 36 22:24:14 2019

"""

import urllib.request
from urllib.request import urlretrieve
import urllib.parse
import os
from bs4 import BeautifulSoup


def feature(url , bahr_name):


	headers = {}
	headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
	req = urllib.request.Request(url, headers = headers)
	resp = urllib.request.urlopen(req)
	print("connection ok")
	respData = resp.read()
	resp.close()
	print('Done')

	soup = BeautifulSoup(respData, "html.parser")

	divpoem = soup.find('div',{'class':'bet-1'}).find_all('h3')

	divauth = soup.find_all('h2')
	auth_name = divauth[3].get_text(strip = True)

	poemslist = []
	
	for i in divpoem:

	    txtsrc0 = i.get_text(strip = True)
	    poemslist.append(txtsrc0)

	poem = "\n".join(poemslist)

	ds = [auth_name ,bahr_name , poem ]

	return ds

#bahr to add after finish scrapping

	


'''
	with open('poetry0.txt','a+', encoding="utf-8") as p: 

		p.write(str(txtsrc) + '\n')
		p.close()
'''
