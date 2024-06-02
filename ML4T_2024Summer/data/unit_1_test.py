#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:23:47 2024

@author: S
"""
import pandas as pd
import matplotlib as plt

dfSPY = pd.read_csv("/home/S/Projects/ML4T/ML4T_2024Summer/data/SPY.csv", 
                    index_col="Date", 
                    parse_dates=True,
                    usecols=['Date','Adj Close'], 
                    na_values=['nan'])
print(dfSPY.head())
dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})

def test_run():
    start_date = '2010-01-22'
    end_date='2010-01-26'
    dates = pd.date_range(start_date,end_date)
    print(dates)
    
    df1 = pd.DataFrame(index=dates)
    
    df1 = df1.join(dfSPY, how='inner').dropna()
    
    print(df1)
    # dfSPY[['Close', 'Adj Close']].plot()
    # plt.show()
    symbols =['GOOG', 'IBM', 'GLD']
    for symbol in symbols:
        df_temp=pd.read_csv(f"./{symbol}.csv", 
                            index_col='Date',
                            parse_dates=True,
                            usecols=['Date', 'Adj Close'],
                            na_values =['nan'])
        df_temp = df_temp.rename(columns={'Adj Close' : symbol})
        df1 = df1.join(df_temp)
        print(df1)
        
        
if __name__ == "__main__":
    test_run()

    



