#导入tushare、pandas等库
import tushare as ts
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from pandas import DataFrame
ts.set_token('32b8468e7397e72da67b1acfe011701bfeffba30aaa26652053703d6')#初始化
pro = ts.pro_api('32b8468e7397e72da67b1acfe011701bfeffba30aaa26652053703d6')
print(ts.get_hist_data('600600',start='2019-07-01',end='2020-08-10'))#查看青海啤酒(600600）指定时间内k线数据
df=ts.get_hist_data('600600',start='2019-07-01',end='2020-08-10')
print(df)#查看赋值是否成功
df.to_csv('D:/青海啤酒股票k线数据.csv')#将股票数据存为csv文件
df=pd.read_csv('D:/青海啤酒股票k线数据.csv')#导入本地存储的股票数据csv文件
print('df:',df)#查看df数据
raw_time = pd.to_datetime(df.pop('date'), format='%Y/%m/%d')#取出时间
print(raw_time)#查看时间取出是否成功
# 相关系数矩阵计算
correlation = df.corr()
print(correlation)#查看相关系数矩阵
#绘制散点图
plt.scatter(df['volume'][:200], df['close'][:200])  # 切片，取前200组数据
plt.xlabel('Volume')
plt.ylabel('Share Price')
plt.title('Volume & Share Price')
plt.show()
# 绘制开盘折线图
plt.plot(raw_time, df['open'])
plt.xlabel('Time')
plt.ylabel('Share Price')
plt.title('Trend')
plt.show()