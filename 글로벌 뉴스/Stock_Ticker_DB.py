import csv
from pandas import Series, DataFrame
import pandas as pd

def stock_search(code):

    nyse = pd.read_csv('NYSE_20171204.txt')
    nyse = nyse.drop(['<date>', '<open>', '<high>', '<low>', '<close>', '<vol>'], axis=1)
    nyse['<market>'] = 'US'
    nyse = DataFrame(nyse, columns=['<market>', '<ticker>', '<name>'])

    nasdaq = pd.read_csv('NASDAQ_20171204.txt')
    nasdaq = nasdaq.drop(['<date>', '<open>', '<high>', '<low>', '<close>', '<vol>'], axis=1)
    nasdaq['<market>'] = 'US'
    nasdaq = DataFrame(nasdaq, columns=['<market>', '<ticker>', '<name>'])

    us = pd.concat([nyse, nasdaq])

    result = pd.concat([DataFrame(us[us['<ticker>'].str.contains(code)]), DataFrame(us[us['<name>'].str.contains(code)])])
    result = result.drop_duplicates(['<ticker>','<name>'], keep='first')
    return result


a = stock_search('A')
print(a)
print(len(a))
