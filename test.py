#! /usr/bin/env python
#coding=utf-8

# 字符串练习
s="I just a charactor string."
print s.find("just")

t=s.replace('just','have had')
print s+'\n'+t

print s.rsplit(' ')

print s.upper()


print s.lower()

print s.isupper()

s1=s.split(' ') #已空格做分界符分解s为列表s1
print s1

s1=s[3:10]   #分片
print s1
s1=s[2:15:2]  #分片，步进2
print s1
s1=s[::-1]   #倒序/分片步进-1
print s1

import sys
print(sys.argv)

s1=list(s)     #打散为列表
print s1

L=s.split(" ")
s1=''.join(L)              #连接
s2="[Delimet]".join(L)
print s1
print s2

print vars()
import acengineer
x=acengineer.dewpoint(34,85)
delta=acengineer.delta_box(0.035,34.0,85.0,17)
print x,delta*1000

