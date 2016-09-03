#! /usr/bin/env python
#coding=utf-8
import numpy as np
import pandas as pd
from pandas import to_datetime
import matplotlib.pyplot as plt
place='ZSSS'
for pick in range(2015,2017):
    year=str(pick)
    table=pd.read_csv(year+place+'rec.csv',parse_dates='CST',date_parser="%Y-%m-%d" )
    x = to_datetime(np.array(table['CST']))
    MAX=table['Max TemperatureC']
    #  dS = datetime.datetime(2015,1,1)
    #  dend = datetime.datetime(2015,12,31)
    #  x=pd.date_range(start=dS, end=dend, freq='D')
    AVR=table['Mean TemperatureC']
    MIN=table['Min TemperatureC']
    #  plt.figure()
    plt.plot_date(x,MAX,
        linestyle='-',
        xdate=True,ydate=False,
        color='red',)
    plt.plot_date(x,AVR,
        linestyle='-',
        xdate=True,ydate=False,
        color='green',)
    plt.plot_date(x,MIN,
        linestyle='-',
        xdate=True,ydate=False,
        color='blue',)
plt.yticks(range(-20,41,5))
plt.grid()
plt.show()
