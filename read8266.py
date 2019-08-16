#! /usr/bin/env python
# coding=utf-8
import json
import urllib2
import bs4
from bs4 import BeautifulSoup


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


url = "http://10.0.0.49/json"
page = urllib2.urlopen(url)
bs = BeautifulSoup(page, "html.parser")
ss = str(bs).replace("\n", "")
ss = ss.replace("pm2.5", "pm2dot5")
ss = ss.replace("pm1.0", "pm1dot0")
data = json.loads(ss, object_hook=JSONObject)
print "Pm1.0=" + str(data.Sensors[2].pm1dot0) + "ug/m3"
print "Pm2.5=" + str(data.Sensors[2].pm2dot5) + "ug/m3"
print "Pm10=" + str(data.Sensors[2].pm10) + "ug/m3"
print "HCHO=" + str(data.Sensors[2].HCHO / 1000.0) + "mg/m3"
print "温度" + str(data.Sensors[0].Temperature) + "C"
print "相对湿度" + str(data.Sensors[0].Humidity) + "%"
