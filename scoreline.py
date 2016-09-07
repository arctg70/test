#! /usr/bin/env python
#coding=utf-8
import numpy as np
import pandas as pd
from pandas import to_datetime
import matplotlib.pyplot as plt
table=pd.read_csv('record.txt', parse_dates='timestamp',delimiter='\t' )
x = to_datetime(np.array(table['timestamp']))
avaragetime=table['avaragetime']
corr_ratio=table['corr_ratio']
#  plt.figure()
plt.plot_date(x,avaragetime,
    linestyle='-',
    xdate=True,ydate=False,
    color='red',)
plt.plot_date(x,corr_ratio,
    linestyle='-',
    xdate=True,ydate=False,
    color='green',)
plt.yticks(range(0,101,5))
plt.grid()
plt.show()

