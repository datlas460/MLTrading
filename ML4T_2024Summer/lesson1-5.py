import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd

#GENERATE FILE PATH
def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, f"{str(symbol)}.csv")

a = symbol_to_path('SPY')
print(a)

#GENERATE DATAFRAME
def get_data(symbol_list, dates):
    df_final=pd.DataFrame(index=dates)
    if "SPY" not in symbol_list:
        symbol_list.insert(0,"SPY")
    for symbol in symbol_list:
        file_path = symbol_to_path(symbol)
        df_temp = pd.read_csv(file_path,
                              parse_dates = True,
                              index_col='Date',
                              usecols=["Date", "Adj Close"])
        df_temp.rename(columns={"Adj Close" : symbol}, inplace=True)
        df_final = df_final.join(df_temp)
        if symbol == 'SPY':
            df_final=df_final.dropna(subset=['SPY'])
    return df_final

#PLOT DATA
def plot(df_data):
    plt.plot(df_data)
    plt.title('Incomplete Data')
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()


if __name__ == '__main__':

    #list of symbols
    symbol_list =['FAKE2']
    #range
    start_date = '2005-12-31'
    end_date = '2014-12-07'
    #create date range
    idx = pd.date_range(start=start_date, end=end_date)
    #get adj close of each
    df_data = get_data(symbol_list, idx)
    df_data.fillna(method="ffill", inplace=True)
    df_data.fillna(method="bfill", inplace=True)
    plot(df_data)