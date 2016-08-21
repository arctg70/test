#! /usr/bin/env python
# coding=utf-8

# 截取html内表格数据练习

import urllib2
import bs4
from bs4 import BeautifulSoup
print "ok"
url = "http://104.236.183.70/vnstat"
# url = "http://www.jb51.net/onlineread/htmlchar.htm"
print "Setting target url to:", url
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "html.parser")
# print soup
# print soup.table.tr.next_sibling.next_sibling.next_sibling.next_sibling.td.next_sibling.string
# target_line = soup.table.find_all("tr")[2]
# target_line = soup("table")[0]("tr")[2]("td")[2].string

f = open('w-table.txt', 'w')
for line in soup("table")[0]("tr"):
#    print line
    for cell in line(["th", "td"]):
            print cell.string.encode('utf-8')
            f.write(cell.string.encode('utf-8') + '\t')
    f.write('\n')
# print target_line

f.close()
print dir(soup)
