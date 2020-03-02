from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import requests
import lxml.html as lh
import tushare as ts

symbols = pd.read_csv('/Users/chunyanwang/Documents/Christine/projects/data files/allstock data in one file/stocks symbol.csv')

def dividend_info():
    #f = pd.DataFrame()
    f = pd.read_csv('/Users/chunyanwang/Documents/Christine/projects/data files/allstock data in one file/stocks symbol.csv')
    for i in range(2019,2020):
        for j in range(4,5):
            f1 = ts.get_report_data(i,j)
            print(f1)
            f1['date'] = str(i)+str(j)
            f = pd.concat([f,f1])
            f.to_csv('stocks report.csv')
#f = ts.get_stock_basics(2017)
  
'''
    for s in symbols['symbols']:
        #source = urllib.request.urlopen('http://data.eastmoney.com/yjfp/detail/' + str(s) + '.html')
        #source = urllib.request.urlopen('http://f10.eastmoney.com/f10_v2/CapitalStockStructure.aspx?code=SH600004')
        #soup = BeautifulSoup(source,'html5lib')
        page = requests.get('http://f10.eastmoney.com/f10_v2/CapitalStockStructure.aspx?code=SH600004')
        doc = lh.fromstring(page.content)
        table_elments = doc.xpath('//table')
        for t in table_elments:
            print('table ',t)
        exit()

        tables = soup.find_all('table')
        for t in tables:
            print(t)
        exit()

        table = soup.find('table',id="lngbbd_Table")
        print('table ',table)
        exit()
        table_rows = table._ind_all('tr')
        for tr in table_rows:
            print('tr ',tr)
            td = tr.find_all('td')
            print('td ', td)
            row = [i.text for i in td]
            #if row[0][0] == 1 or row[0][0] == 2 or row[0][0] == '1' or row[0][0] == '2':
            print(row)
        exit()
'''
#dividend_info()

data = ts.profit_data(year=2020,top=3000)
data.to_csv('profit report 2020.csv')
