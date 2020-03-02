# download recent 3 years stock data from tushare

import tushare as ts
import pandas as pd
import os as os

dir = '/Users/chunyanwang/Documents/Christine/projects/data files/downloaded stock data/stocks daily data - tushare/'
symbols = pd.read_csv('/Users/chunyanwang/Documents/Christine/projects/data files/allstock data in one file/stocks symbol.csv')

def download_stock_minute_data(d):
    files = os.listdir(dir)
    files.sort()
    for f in files:
        if len(f) == 10:
            stock = f[:6]
            dates = pd.read_csv(dir+f,header=0)['date']
            all_data = pd.DataFrame()
            df = ts.get_tick_data(stock,date=d,src='tt')
            #df = ts.get_today_ticks(stock)
            if isinstance(df, pd.DataFrame) and len(df) > 1:
                df['date'] = d
                df.to_csv('/Users/chunyanwang/Documents/Christine/projects/data files/downloaded stock data/oneday minute data - tushare'+ f,encoding='utf_8_sig')    
                print(f + ' minute data is downloaded ' + d)

#download_stock_hist()
download_stock_minute_data('2020-01-14')
