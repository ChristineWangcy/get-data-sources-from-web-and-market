import os
import pandas as pd
dir = '/Users/chunyanwang/Christine documents/projects/data files/downloaded stock data/1014 daily/'
files = os.listdir(dir)

symbols = []
data = pd.DataFrame()
for f in files:
    if f[3] == '0' or f[3] == '6' or f[3] == '3':
        symbols.append(f[3:9])
data['symbols'] = symbols
data.to_csv('/Users/chunyanwang/Christine documents/projects/data files/allstock data in one file/stocks symbol.csv')