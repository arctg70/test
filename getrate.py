#! /usr/bin/env python
# coding=utf-8
import exchange
from exchange import exrate
from exchange import HKDrate
currency = "港币"
print exrate(currency, 2)
print "RMB" + str(349.0 * exrate("美元", 2))
print "美元"
import math
print math.pi * 33**2
print HKDrate(2)
print exchange.HKDrate(2)
print exchange.HKDrate(1)
print dir(exchange)
# ok
