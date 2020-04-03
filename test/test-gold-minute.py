from stock_pandas import StockDataFrame
import pandas as pd
tt=pd.read_csv('kline-m1.txt')
stock = StockDataFrame(tt,date_column='ctm')
#print(tt)
#print(stock)
d=stock['kdj.d']
k=stock['kdj.k']
buy=0
sell=0
sum=0
for i in range(1,len(d)):
   if k[i-1]<=d[i-1] and k[i]>=d[i]:
       #print("buy:"+str(tt.iloc[i]))
       print("buy:")
       buy=tt.iloc[i]["close"]
   elif k[i-1]>=d[i-1] and k[i]<=d[i]:
       #print("sell:" +str(tt.iloc[i]))
       sell=tt.iloc[i]["close"]
       print("sell:")
       print("diff:"+str(sell-buy))
       sum=sum+(sell-buy)
       print("total:"+str(sum))
