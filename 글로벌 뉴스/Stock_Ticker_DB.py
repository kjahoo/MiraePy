import csv
from pandas import Series, DataFrame
import pandas as pd

nyse = pd.read_csv('NYSE_20171204.txt')
nyse = nyse.drop(['<date>', '<open>', '<high>', '<low>', '<close>', '<vol>'], axis=1)
nyse['<market>'] = 'US'
nyse = DataFrame(nyse, columns=['<market>', '<ticker>', '<name>'])

nasdaq = pd.read_csv('NASDAQ_20171204.txt')
nasdaq = nasdaq.drop(['<date>', '<open>', '<high>', '<low>', '<close>', '<vol>'], axis=1)
nasdaq['<market>'] = 'US'
nasdaq = DataFrame(nyse, columns=['<market>', '<ticker>', '<name>'])

us = pd.concat([nyse, nasdaq])



def stock_search(code):
    result = []
    for i in us:
        if code in us[i]:
            print(i)
            result.append(us[i])

    return result


a = stock_search('US')
print(a)
