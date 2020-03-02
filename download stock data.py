# download recent 3 years stock data from tushare

import tushare as ts
import pandas as pd
import os as os

dir = '/Users/chunyanwang/Christine documents/projects/data files/downloaded stock data/stocks daily data - tushare/'
symbols = pd.read_csv('/Users/chunyanwang/Christine documents/projects/data files/allstock data in one file/stocks symbol.csv')

def download_index_hist():
    df = ts.get_hist_data('sh')
    print(df)
    if isinstance(df, pd.DataFrame) and len(df) > 1:
        df.to_csv(dir + 'sh000001.csv',encoding='utf_8_sig')    
        print('sh000001 is downloaded')

def download_stock_hist():
    for s in symbols['symbols']:
        #download recent 3 years data
        stock_symbol = str(s)
        df = ts.get_hist_data(stock_symbol)
        if isinstance(df, pd.DataFrame) and len(df) > 1:
            df.to_csv('/Users/chunyanwang/Documents/Christine/projects/data files/downloaded stock data/stocks daily data - tushare/'+ str(s) +'.csv',encoding='utf_8_sig')    
            print(str(s)+' is downloaded')


def download_stock_minute_data():
    files = os.listdir(dir)
    files.sort()
    for f in files:
        if len(f) == 10:
            stock = f[:6]
            dates = pd.read_csv(dir+f,header=0)['date']
            all_data = pd.DataFrame()
            for d in dates:
                df = ts.get_tick_data(stock,date=d,src='tt')
                if isinstance(df, pd.DataFrame) and len(df) > 1:
                    df['date'] = d
                    all_data = pd.concat([all_data,df])
                    all_data.to_csv('/Users/chunyanwang/Documents/Christine/projects/data files/downloaded stock data/stocks minute data - tushare/'+ f,encoding='utf_8_sig')    
                    print(f,d,len(all_data))
            print(str(s)+'minute data is downloaded')


#download_stock_hist()
#download_stock_minute_data()
download_index_hist()