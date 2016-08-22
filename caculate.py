#! /usr/bin/env python
#coding=utf-8
import random
import time
start=time.time()
a=1
r=0
w=0

oprator='+-*/'

print '======================================='
while a==1:
    thisstart=time.time()
    op=random.randint(0,3)
    if op==0:
        x=random.randint(0,1000)
        y=random.randint(0,1000)
        ans=x+y
    if op==1:
        x=random.randint(0,1000)
        y=random.randint(0,1000)
        while x<y:
            y=random.randint(0,1000)
        ans=x-y
    if op==2:
        x=random.randint(1,1000)
        y=random.randint(2,9)
        ans=x*y
    if op==3:
        ans=random.randint(2,100)
        y=random.randint(2,9)
        x=y*ans
    print " "*24+str(x)+oprator[op]+str(y)+'='
    answer=raw_input("     你的计算结果是:")
    end=time.time()
    if answer.isdigit():
        if int(answer)==ans:
            r+=1
            print "答对:"+str(r)+"   答错:"+str(w)
            print "总耗时:"+str(end-start)
            print "上一题耗时:"+str(end-thisstart)
            print "平均耗时:"+str((end-start)/(r+w))
            print "答对率:"+str(float(r)/(r+w)*100)+"%"
            print "                答对了!"
            print '======================================='
        else:
            w+=1
            print "答对:"+str(r)+"   答错:"+str(w)
            print "总耗时:"+str(end-start)
            print "上一题耗时:"+str(end-thisstart)
            print "平均耗时:"+str((end-start)/(r+w))
            print "答对率:"+str(float(r)/(r+w)*100)+"%"
            print "          算错了!! 正确答案是 "+str(ans)
            print '======================================='
    else:
        if answer=='stop':
            if r+w==0 :break
            print "答对:"+str(r)+"   答错:"+str(w)
            print "总耗时:"+str(end-start)
            print "上一题耗时:"+str(end-thisstart)
            print "平均耗时:"+str((end-start)/(r+w))
            print "答对率:"+str(float(r)/(r+w)*100)+"%"
            print "BYE!"
            break
        else:
            print "字符输入错误."

