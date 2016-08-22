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
    answer=raw_input("Please enter the answer:")
    end=time.time()
    if answer.isdigit():
        if int(answer)==ans:
            r+=1
            print "Right:"+str(r)+"   Wrong:"+str(w)
            print "Time cost total:"+str(end-start)
            print "Time cost last:"+str(end-thisstart)
            print "Average cost:"+str((end-start)/(r+w))
            print "Correct ratio:"+str(float(r)/(r+w))
            print "Good!"
            print '======================================='
        else:
            w+=1
            print "Right:"+str(r)+"   Wrong:"+str(w)
            print "Time cost total:"+str(end-start)
            print "Time cost last:"+str(end-thisstart)
            print "Average cost:"+str((end-start)/(r+w))
            print "Correct ratio:"+str(float(r)/(r+w))
            print "Wrong!! The answer is "+str(ans)
            print '======================================='
    else:
        if answer=='stop':
            if r+w==0 :break
            print "Right:"+str(r)+"   Wrong:"+str(w)
            print "Time cost total:"+str(end-start)
            print "Time cost last:"+str(end-thisstart)
            print "Average cost:"+str((end-start)/(r+w))
            print "Correct ratio:"+str(float(r)/(r+w))
            print "BYE!"
            break
        else:
            print "wrong input."

