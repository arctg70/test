#! /usr/bin/env python
#coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 练习excel表格读取
# 数据统计和直方图，平均值，偏差和方差
# 散点图
table=pd.read_excel('elmeter.xls',sheetname='Sheet4')
#  arr1=np.array(table)
#  print arr1.mean()
#  print arr1.std()
#  print arr1.var()

nd=pd.Series(table['WPM'])
print nd.mean()
print nd.std()
print nd.var()

nd.hist(bins=40,alpha=0.5,color='red')
plt.xlabel(r'$W/m^2$')
plt.ylabel(r'$Count$')
plt.title(r'$Power Statics$')
plt.xticks(range(0,500,25),rotation=90)
plt.savefig('wpm.png')
plt.show()

#  pd.Series(table['LOADRATE']).hist(bins=40)
#  plt.xlabel('Loadrate')
#  plt.ylabel('Count')
#  plt.show()


data=pd.read_excel('elmeter.xls',sheetname='Sheet4')
print data
data_name=data.set_index('NAME')
#
#  x=data[['WPM']]
#  y=data[['NAME']]
#  plt.figure()
#  plt.ylim(0,60)
#  plt.xlabel('Power Per Squremeter')
#  plt.ylabel('Index')
#  plt.title('Scatter Plot')
#  plt.show()
#
x=data[['AREA']]
y=data[['LOAD']]
print x[0:3]
plt.figure()
plt.plot(x,y,
    linestyle='',
    marker='o',
    markersize=10,
    color='red',
    alpha=0.6,)
#  plt.xlim(0,500)
#  plt.ylim(0,60)
plt.xlabel(r'$Area(m^2)$',fontsize=16)
plt.ylabel(r'$Load(kW)$',fontsize=16)
plt.title(r'$Scatter Plot$',fontsize=16)

x=np.linspace(0,500,500)
y1,y2=130.0*x/1000,350.0*x/1000
plt.plot(x,y1,
        linestyle='-',
        color='blue',
        alpha=0.6,)
plt.plot(x,y2,
        linestyle='-',
        color='green',
        alpha=0.6,)
plt.annotate(r'$Line of 130W/m^2$',#注释文字
    xy=(200, 130.*200/1000),#注释位置
    #  xycoords='data',
    xytext=(-10, 30),#注释文字位置
    textcoords='offset points',#坐标形式是偏移量
    fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))#箭头
plt.annotate(r'$Line of 350W/m^2$',
    xy=(200, 350.*200/1000),
    #  xycoords='data',
    xytext=(-100, 30),
    textcoords='offset points',
    fontsize=16,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))


plt.show()

