import urllib.request
from urllib.request import urlretrieve
import urllib.parse
import os
from bs4 import BeautifulSoup
import csv
from feature_extr import feature

aldiwan = 'https://www.aldiwan.net/'

#tawil  = aldiwan + "poem.html?Word=%C7%E1%D8%E6%ED%E1&Find=meaning"
kamil  = aldiwan + "poem.html?Word=%C7%E1%DF%C7%E3%E1&Find=meaning"
bassit = aldiwan + "poem.html?Word=%C7%E1%C8%D3%ED%D8&Find=meaning"
rajz = aldiwan + "poem.html?Word=%C7%E1%D1%CC%D2&Find=meaning"
mohdat = aldiwan + "poem.html?Word=%C7%E1%CE%C8%C8&Find=meaning"
motadarik = aldiwan + "poem.html?Word=%C7%E1%E3%CA%CF%C7%D1%DF&Find=meaning"
sarii = aldiwan + "poem.html?Word=%C7%E1%D3%D1%ED%DA&Find=meaning"
#bohor_links = (tawil , kamil , bassit , rajz, mohdat ,motadarik ,sarii)
#bohor_names = ('tawil','kamil','bassit','rajz','mohdat','motadarik','sarii')

bohor_links = (kamil , bassit , rajz, mohdat ,motadarik ,sarii)
bohor_names = ('kamil','bassit','rajz','mohdat','motadarik','sarii')

bohor_dict = dict(zip(bohor_names, bohor_links))

for bahrname, bahrlink in bohor_dict.items():
    file_name = bahrname + '.csv'
    csv_f = open(file_name, "w+", encoding="utf-8")
    writer = csv.writer(csv_f, delimiter=',')
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    req = urllib.request.Request(bahrlink, headers = headers)
    resp = urllib.request.urlopen(req)
    print("connection ok")
    respData = resp.read()
    resp.close()

    soup = BeautifulSoup(respData, "html.parser")

    div = soup.find('div',{'class':'content row'})
    #print(div)
    qassidalinks = []
    divq = div.find_all('div',{'class':'record col-12'})
    for l in divq:

        #link = l.get('href')
        qassida_link = aldiwan + (l.find('a').get('href'))
        qassidalinks.append(qassida_link)


    #for bahr_name in bohor_names :
    for link in qassidalinks :

        datalist = feature(link , bahrname)

        writer.writerow(datalist)