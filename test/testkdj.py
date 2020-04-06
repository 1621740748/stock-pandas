# -*- coding: utf-8 -*-
import os, sys
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import talib

if len(sys.argv) == 2:
    code = sys.argv[1]
else:
    print('usage: python talib_obv.py stockcode ')
    sys.exit(1)

if len(code) != 6:
    print('stock code length: 6')
    sys.exit(2)

df = ts.get_k_data(code)
df = df[df['date'] > '2019-01-01']
if len(df) < 10:
    print(" len(df) <10 ")
    sys.exit(2)

dw = pd.DataFrame()
# KDJ 值对应的函数是 STOCH
dw['slowk'], dw['slowd'] = talib.STOCH(
    df['high'].values,
    df['low'].values,
    df['close'].values,
    fastk_period=9,
    slowk_period=3,
    slowk_matype=0,
    slowd_period=3,
    slowd_matype=0)
dw.index = range(len(dw))
print(len(dw))

df.index = pd.to_datetime(df.date)
# 画股票收盘价图
fig, axes = plt.subplots(2, 1)
df[['close']].plot(ax=axes[0], grid=True, title=code)
# 画 KDJ 曲线图
dw[['slowk', 'slowd']].plot(ax=axes[1], grid=True)
print(dw)
plt.show()