#! /usr/bin/env python
#coding=utf-8
import random
import time
import datetime
start=time.time()
a=1
r=0
w=0

oprator='+-*/'

print '======================================='
while a==1:
    thisstart=time.time()
    op=random.randint(0,4)
    if op==0:
        x=random.randint(0,1000)
        y=random.randint(0,1000)
        ans=x+y
        print " "*24+str(x)+oprator[op]+str(y)+'='
    if op==1:
        x=random.randint(0,1000)
        y=random.randint(0,1000)
        while x<y:
            y=random.randint(0,1000)
        ans=x-y
        print " "*24+str(x)+oprator[op]+str(y)+'='
    if op==2:
        x=random.randint(1,1000)
        y=random.randint(2,9)
        ans=x*y
        print " "*24+str(x)+oprator[op]+str(y)+'='
    if op==3:
        ans=random.randint(2,1000)
        y=random.randint(2,9)
        x=y*ans
        print " "*24+str(x)+oprator[op]+str(y)+'='
    if op==4:
        x=random.randint(1,1000)
        y=random.randint(1,1000)
        z=random.randint(1,100)
        ans=x+y*z
        print " "*24+str(x)+'+'+str(y)+'*'+str(z)+'='
    answer=raw_input("     你的计算结果是:")
    end=time.time()
    if answer.isdigit():
        if int(answer)==ans:
            r+=1
            print " "*5+"答对:"+str(r)+"   答错:"+str(w)
            print " "*5+"总耗时:    %.2fs" % (end-start)
            print " "*5+"上一题耗时:%.2fs" % (end-thisstart)
            print " "*5+"平均耗时:  %.2fs" % ((end-start)/(r+w))
            print " "*5+"答对率:    %.2f%%" % (float(r)/(r+w)*100)
            print "                答对了!"
            print '======================================='
        else:
            w+=1
            print " "*5+"答对:"+str(r)+"   答错:"+str(w)
            print " "*5+"总耗时:    %.2fs" % (end-start)
            print " "*5+"上一题耗时:%.2fs" % (end-thisstart)
            print " "*5+"平均耗时:  %.2fs" % ((end-start)/(r+w))
            print " "*5+"答对率:    %.2f%%" % (float(r)/(r+w)*100)
            print "          算错了!! 正确答案是 "+str(ans)
            print '======================================='
    else:
        if answer=='stop':
            if r+w==0 :break
            timestamp=str(datetime.datetime.now())
            totaltime=end-start
            avaragetime=(end-start)/(r+w)
            corr_ratio=float(r)/(r+w)*100
            print " "*5+"答对:"+str(r)+"   答错:"+str(w)
            print " "*5+"总耗时:    %.2fs" % (totaltime)
            print " "*5+"上一题耗时:%.2fs" % (end-thisstart)
            print " "*5+"平均耗时:  %.2fs" % (avaragetime)
            print " "*5+"答对率:    %.2f%%" % (corr_ratio)
            f=open('record.txt','a+')
            rec='%s\t%d\t%d\t%.2f\t%.2f\t%.2f\n' % (timestamp,r,w,totaltime,avaragetime,corr_ratio)
            f.write(rec)
            f.close()
            print "BYE!"
            break
        else:
            print "字符输入错误."

