#! /usr/bin/env python
#coding=utf-8

import urllib2
import bs4
from bs4 import BeautifulSoup
city='ZSSS'
for pick in range(2000,2017,1):
    year=str(pick)
    url='https://www.wunderground.com/history/airport/'+city+'/'+year+'/1/1/CustomHistory.html?dayend=31&monthend=12&yearend='+year+'&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1'
    page=urllib2.urlopen(url)
    contents=str(BeautifulSoup(page,"html.parser"))
    aaaa=contents.split('<br/>')
    buffer=''
    for line in aaaa:
        #  rec=line[1:].split(',')
        #  f.write(line[1:]+'\n')
        buffer=buffer+line[1:]+'\n'
        #  print rec
    print buffer
    f=open(year+city+'rec.csv','w')
    f.write(buffer[:-1])
    f.close()




