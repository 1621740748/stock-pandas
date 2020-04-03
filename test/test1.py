from stock_pandas import StockDataFrame
import pandas as pd
stock = StockDataFrame(pd.read_csv('tencent.csv'))
print(stock)
print(stock['kdj.d'])
print(stock['kdj.k'])