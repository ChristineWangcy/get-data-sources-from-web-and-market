import pandas as pd

symbols = pd.read_excel('/Users/chunyanwang/Christine documents/projects/data files/allstock data in one file/'
                        'America Stocks Ticker Symbols.xlsx',header=0)['Ticker']
print(type(symbols))
new_symbols = []
for s in symbols.values.astype('str'):
    if(('.' not in s) == True):
        new_symbols.append(s)
print(new_symbols)
df_symbols = pd.DataFrame(columns=['ticker'],data=new_symbols)
df_symbols = df_symbols.set_index('ticker')
df_symbols.to_csv('/Users/chunyanwang/Christine documents/projects/data files/allstock data in one file/'
                        'America Stocks Ticker Symbols.csv')

