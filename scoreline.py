#! /usr/bin/env python
# coding=utf-8
import numpy as np
import pandas as pd
from pandas import to_datetime
import matplotlib.pyplot as plt
import pylab as pl

# 错误分布柱状图
wtable = pd.read_csv('wrongrec.txt', delimiter='\t')
counts = wtable['op'].value_counts()
pl = counts.plot(kind='bar', color='red', alpha=0.6).get_figure()
pl.show()


#  import numpy as np
#  import pandas as pd
#  from pandas import to_datetime
#  import matplotlib.pyplot as plt
# 平均时间和正确率图
table = pd.read_csv('record.txt', parse_dates='timestamp', delimiter='\t')
x = to_datetime(np.array(table['timestamp']))
avaragetime = table['avaragetime']
corr_ratio = table['corr_ratio']
plt.figure()
plt.plot_date(x, avaragetime,
              linestyle='-',
              xdate=True, ydate=False,
              color='red', label='AverageTime(s)')
plt.plot_date(x, corr_ratio,
              linestyle='-',
              xdate=True, ydate=False,
              color='green', label='Correct_Ratio(%)')
plt.yticks(range(0, 101, 5))
plt.grid()
plt.legend(loc='center left')
plt.show()

#
