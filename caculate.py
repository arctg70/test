#! /usr/bin/env python
#coding=utf-8
import random
import time
import datetime
start=time.time()
a=1
r=0
w=0
repeat=0
#op=random.randint(8,9)
oprator='+-*/'

print '======================================='
while a==1:
    if repeat==0:
		thisstart=time.time()
		op=random.randint(8,9)
    else:
		repeat=0
		tempop=op
		op=999
    if op==0:
        x=random.randint(0,1000)
        y=random.randint(0,1000)
        ans=x+y
        s=" "*24+str(x)+oprator[op]+str(y)+'='
        print s
    if op==1:
        x=random.randint(0,1000)
        y=random.randint(0,x)
        ans=x-y
        s=" "*24+str(x)+oprator[op]+str(y)+'='
        print s
    if op==2:
        x=random.randint(1,1000)
        y=random.randint(2,9)
        ans=x*y
        s=" "*24+str(x)+oprator[op]+str(y)+'='
        print s
    if op==3:
        ans=random.randint(2,1000)
        y=random.randint(2,9)
        x=y*ans
        s=" "*24+str(x)+oprator[op]+str(y)+'='
        print s
    if op==4:
        x=random.randint(1,1000)
        y=random.randint(1,1000)
        z=random.randint(1,100)
        ans=x+y*z
        s=" "*24+str(x)+'+'+str(y)+'*'+str(z)+'='
        print s
    if op==5:
        y=random.randint(1,1000)
        z=random.randint(1,100)
        x=random.randint(1,y*z)
        ans=y*z-x
        s=" "*24+str(y)+'*'+str(z)+'-'+str(x)+'='
        print s
    if op==6:
        x=random.randint(1,1000)
        y=random.randint(1,100)
        z=random.randint(1,100)
        ans=(x+y)*z
        s=" "*24+'('+str(x)+'+'+str(y)+')*'+str(z)+'='
        print s
    if op==7:
        x=random.randint(1,1000)
        y=random.randint(1,x)
        z=random.randint(1,100)
        ans=(x-y)*z
        s=" "*24+'('+str(x)+'-'+str(y)+')*'+str(z)+'='
        print s
    if op==8:
        x=random.randint(100,1000)
        y=random.randint(11,99)
        z=random.randint(1,100)
        ans=x*y
        s=" "*24+str(x)+'*'+str(y)+'='
        print s
    if op==9:
        ans=random.randint(1,100)
        y=random.randint(11,99)
        x=ans*y
        s=" "*24+str(x)+'/'+str(y)+'='
        print s
	if op==999:
		op=tempop
    answer=raw_input("     你的计算结果:")
    end=time.time()
    if answer.isdigit():
        if int(answer)==ans:
            r+=1
            print "                答对了！"
        else:
            w+=1
            print "          算错了！ 正确答案是"+str(ans)
            f=open('wrongrec.txt','a+')
            wrongrec='%s\t%s\t%s\t%s\n' % (str(op),s[24:],str(ans),answer)
            f.write(wrongrec)
            f.close()
        print " "*5+"正确:"+str(r)+"   错误:"+str(w)
        print " "*5+"总耗时:    %.2fs" % (end-start)
        print " "*5+"上一题耗时:%.2fs" % (end-thisstart)
        print " "*5+"平均耗时:  %.2fs" % ((end-start)/(r+w))
        print " "*5+"正确率   %.2f%%" % (float(r)/(r+w)*100)
        print '======================================='
    else:
        if answer=='stop':
            if r+w==0 :break
            timestamp=str(datetime.datetime.now())
            totaltime=end-start
            avaragetime=(end-start)/(r+w)
            corr_ratio=float(r)/(r+w)*100
            f=open('record.txt','a+')
            rec='%s\t%d\t%d\t%.2f\t%.2f\t%.2f\n' % (timestamp,r,w,totaltime,avaragetime,corr_ratio)
            f.write(rec)
            f.close()
            print "BYE!"
            break
        else:
            print "输入错误。请重新输入。"
            repeat=1

