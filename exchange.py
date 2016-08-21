#! /usr/bin/env python
#coding=utf-8
def exrate(currency,choise):
    """
    从中国银行网站爬取当日的外汇对人民币汇率
    :currency: 币种
    :choise: 1 现汇买入价	2现钞买入价	3现汇卖出价	4现钞卖出价	5中行折算价
    """
    import urllib2
    import bs4
    from bs4 import BeautifulSoup
    url = "http://www.boc.cn/sourcedb/whpj/"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page,"html.parser")
    exrate = 0.0
    for line in soup("table")[1]("tr"):
        if line(["th","td"])[0].string.encode('utf-8') == currency:
            return float(line(["th","td"])[choise].string)/100.0
    return exrate
def HKDrate(choise):
    """HKD vs RMB exchange rate today.

    :choise: 1现汇买入价	2现钞买入价	3现汇卖出价	4现钞卖出价	5中行折算价
    :returns: 港币对人民币当天的汇率

    """
    import urllib2
    import bs4
    from bs4 import BeautifulSoup
    url = "http://www.boc.cn/sourcedb/whpj/"
    page=urllib2.urlopen(url)
    soup=BeautifulSoup(page,"html.parser")
    HKDrate=0.0
    for line in soup("table")[1]("tr"):
        if line(["th","td"])[0].string.encode('utf-8')=="港币":
            return float(line(["th","td"])[choise].string)/100.0
    return HKDrate

