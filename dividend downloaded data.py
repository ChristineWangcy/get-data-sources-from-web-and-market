from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import requests
import lxml.html as lh
import tushare as ts

dir = 

data = ts.profit_data(year=2020,top=3000)
data.to_csv('profit report 2020.csv')
