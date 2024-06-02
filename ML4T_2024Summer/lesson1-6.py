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
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()


def compute_daily_returns(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:]/df[:-1].values)-1
    daily_returns.iloc[0,:] = 0
    return daily_returns

def test_run():
    dates= pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM', 'GLD']
    df = get_data(symbols, dates)
    plot(df)
    daily_returns = compute_daily_returns(df)
    #plt.plot(daily_returns)
    # plt.title('Daily Returns')
    # plt.ylabel('Daily Returns')
    # plt.xlabel('Date')

    #plot histogram
    #daily_returns['SPY'].hist(bins=20, label='SPY')
    #daily_returns['XOM'].hist(bins=20, label ='XOM')

    #Scatterplot SPY vs XOM
    daily_returns.plot(kind='scatter', x = 'SPY', y='XOM')
    beta_XOM,alpha_XOM= np.polyfit(daily_returns['SPY'],daily_returns['XOM'],1)
    print('beta_XOM', beta_XOM)
    print('alpha_XOM', alpha_XOM)
    plt.plot(daily_returns['SPY'], beta_XOM*daily_returns['SPY']+alpha_XOM, '-', color='r')
    plt.show()

    daily_returns.plot(kind='scatter', x = 'SPY', y='GLD')
    beta_GLD,alpha_GLD= np.polyfit(daily_returns['SPY'],daily_returns['GLD'],1)
    print('beta_GLD', beta_GLD)
    print('alpha_GLD', alpha_GLD)
    plt.plot(daily_returns['SPY'], beta_XOM*daily_returns['SPY']+alpha_XOM, '-', color='r')

    #calculate correlation coefficient
    print(daily_returns.corr(method='pearson'))




    # get mean and std
    #mean = daily_returns['SPY'].mean()
    #std = daily_returns['SPY'].std()

    #plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    #plt.axvline(std,color='r',linestyle='dashed', linewidth=2)
    #plt.axvline(-std,color='r',linestyle='dashed', linewidth=2)


    print(daily_returns.kurtosis())

    plt.show()
if __name__ == '__main__':
    test_run()




    #list of symbols
    # symbol_list =['FAKE2']
    # #range
    # start_date = '2005-12-31'
    # end_date = '2014-12-07'
    # #create date range
    # idx = pd.date_range(start=start_date, end=end_date)
    # #get adj close of each
    # df_data = get_data(symbol_list, idx)
    # df_data.fillna(method="ffill", inplace=True)
    # df_data.fillna(method="bfill", inplace=True)
    # plot(df_data)