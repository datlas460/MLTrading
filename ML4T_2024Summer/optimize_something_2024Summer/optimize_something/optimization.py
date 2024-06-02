""""""
import math

"""MC1-P2: Optimize a portfolio.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		 	   			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		 	   			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Template code for CS 4646/7646  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		 	   			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		 	   			  		 			 	 	 		 		 	
and other users of this template code are advised not to share it with others  		  	   		 	   			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		 	   			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		 	   			  		 			 	 	 		 		 	
or edited.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		 	   			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		 	   			  		 			 	 	 		 		 	
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		 	   			  		 			 	 	 		 		 	
GT honor code violation.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
-----do not edit anything above this line---  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
Student Name: Srihari Datla	  	   		 	   			  		 			 	 	 		 		 	
GT User ID: sdatla8  		  	   		 	   			  		 			 	 	 		 		 	
GT ID: 903647808 		  	   		 	   			  		 			 	 	 		 		 	
"""  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
import datetime as dt
import scipy.optimize as spo
  		  	   		 	   			  		 			 	 	 		 		 	
import numpy as np
#import os #REMOVETHIS
  		  	   		 	   			  		 			 	 	 		 		 	
import matplotlib.pyplot as plt  		  	   		 	   			  		 			 	 	 		 		 	
import pandas as pd  		  	   		 	   			  		 			 	 	 		 		 	
from util import get_data, plot_data
def author():
    return 'sdatla8'
def study_group():
    return 'sdatla8'



# This is the function that will be tested by the autograder  		  	   		 	   			  		 			 	 	 		 		 	
# The student must update this code to properly implement the functionality  		  	   		 	   			  		 			 	 	 		 		 	
def optimize_portfolio(  		  	   		 	   			  		 			 	 	 		 		 	
    sd=dt.datetime(2008, 1, 1),  		  	   		 	   			  		 			 	 	 		 		 	
    ed=dt.datetime(2009, 1, 1),  		  	   		 	   			  		 			 	 	 		 		 	
    syms=["GOOG", "AAPL", "GLD", "XOM"],  		  	   		 	   			  		 			 	 	 		 		 	
    gen_plot=False,  		  	   		 	   			  		 			 	 	 		 		 	
):  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
    This function should find the optimal allocations for a given set of stocks. You should optimize for maximum Sharpe  		  	   		 	   			  		 			 	 	 		 		 	
    Ratio. The function should accept as input a list of symbols as well as start and end dates and return a list of  		  	   		 	   			  		 			 	 	 		 		 	
    floats (as a one-dimensional numpy array) that represents the allocations to each of the equities. You can take  		  	   		 	   			  		 			 	 	 		 		 	
    advantage of routines developed in the optional assess portfolio project to compute daily portfolio value and  		  	   		 	   			  		 			 	 	 		 		 	
    statistics.  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		 	   			  		 			 	 	 		 		 	
    :type sd: datetime  		  	   		 	   			  		 			 	 	 		 		 	
    :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		 	   			  		 			 	 	 		 		 	
    :type ed: datetime  		  	   		 	   			  		 			 	 	 		 		 	
    :param syms: A list of symbols that make up the portfolio (note that your code should support any  		  	   		 	   			  		 			 	 	 		 		 	
        symbol in the data directory)  		  	   		 	   			  		 			 	 	 		 		 	
    :type syms: list  		  	   		 	   			  		 			 	 	 		 		 	
    :param gen_plot: If True, optionally create a plot named plot.png. The autograder will always call your  		  	   		 	   			  		 			 	 	 		 		 	
        code with gen_plot = False.  		  	   		 	   			  		 			 	 	 		 		 	
    :type gen_plot: bool  		  	   		 	   			  		 			 	 	 		 		 	
    :return: A tuple containing the portfolio allocations, cumulative return, average daily returns,  		  	   		 	   			  		 			 	 	 		 		 	
        standard deviation of daily returns, and Sharpe ratio  		  	   		 	   			  		 			 	 	 		 		 	
    :rtype: tuple  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # Read in adjusted closing prices for given symbols, date range
    dates = pd.date_range(sd, ed)  		  	   		 	   			  		 			 	 	 		 		 	
    prices_all = get_data(syms, dates)  # automatically adds SPY
    prices = prices_all[syms] # only portfolio symbols
    #prices = prices.drop('SPY', axis=1)
    #plt.plot(prices)
    #plt.title('Stock Performance')
    #plt.xlabel('Date')
    #plt.ylabel('Price')
    #plt.legend(prices.columns, title='Stocks')
    #plt.show()
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later  		  	   		 	   			  		 			 	 	 		 		 	



    #generate first allocs
    allocs = np.asarray([])
    for _ in range(len(prices.columns)):
        allocs = np.append(allocs, np.float64(1/len(prices.columns)))



    allocs, cr, adr, sddr, sr, normed, alloced, port_val, daily_returns = get_all(prices, allocs)




    # find the allocations for the optimal portfolio  		  	   		 	   			  		 			 	 	 		 		 	
    # note that the values here ARE NOT meant to be correct for a test case  		  	   		 	   			  		 			 	 	 		 		 	




    # add code here to find the allocations
    # cr, adr, sddr, sr = [
    #     0.25,
    #     0.001,
    #     0.0005,
    #     2.1,
    # ]  # add code here to compute stats
  		  	   		 	   			  		 			 	 	 		 		 	
    # Get daily portfolio value
    normed_spy = get_normalized(prices_SPY)
    port_val_spy = normed_spy*1000000
    daily_returns_spy = compute_daily_returns(port_val_spy)[1:]
    normed_pf = get_normalized(port_val)
    #print('normed pf',normed_pf.head())
    #print('normed spy', normed_spy.head())
    #print('daily returns spy', daily_returns_spy.head())



    #spy_port_val = get_portfolio_value(normed_spy)  # add code here to compute daily portfolio values
  		  	   		 	   			  		 			 	 	 		 		 	
    # Compare daily portfolio value with SPY using a normalized plot  		  	   		 	   			  		 			 	 	 		 		 	
    #gen_plot = True
    if gen_plot:
        df_temp = pd.concat(  		  	   		 	   			  		 			 	 	 		 		 	
            [normed_pf, normed_spy], keys=["Portfolio", "SPY"], axis=1
        )
        plt.plot(df_temp)
        plt.title('Portfolio Performance vs SPY')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend(df_temp.columns)
        plt.savefig('Figure1.png')
        #plt.show()
        pass  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    return allocs, cr, adr, sddr, sr

def get_all(prices, allocs):

    def fmin(allocs):
        allocs = allocs
        #normalize prices
        normed = get_normalized(prices)
        #merge normalized with allocations
        alloced = get_alloced(normed, allocs)
        #calculate port val
        port_val = get_portfolio_value(alloced)
        #compute daily returns
        daily_returns = compute_daily_returns(port_val)[1:]
        #calculate avg daily return
        adr = compute_avg_daily_ret(daily_returns)
        #calculate std deviation
        sddr = compute_std_dev(daily_returns)
        sr = adr/sddr
        return -sr

    #result = spo.minimize(f, allocs, args=(prices), method = 'SLSQP', options={'disp': True})
    # Constraints: sum(allocs) <= 1
    constraints = ({'type': 'eq', 'fun': lambda allocs: 1.0 - np.sum(allocs)})

    # Bounds for each allocation: 0 <= allocs[i] <= 1
    bounds = [(0, 1) for _ in range(len(allocs))]

    # Perform the minimization
    result = spo.minimize(fmin, allocs, method='SLSQP', bounds=bounds, constraints=constraints)




    allocs = result['x']
    #normalize prices
    normed = get_normalized(prices)
    #merge normalized with allocations
    alloced = get_alloced(normed, allocs)
    #calculate port val
    port_val = get_portfolio_value(alloced)
    #compute daily returns
    daily_returns = compute_daily_returns(port_val)[1:]
    #calculate cumulative return
    cr = compute_cum_ret(port_val)
    #calculate avg daily return
    adr = compute_avg_daily_ret(daily_returns)
    #calculate std deviation
    sddr = compute_std_dev(daily_returns)
    sr = adr/sddr * math.sqrt(252)
    return [allocs, cr, adr, sddr, sr, normed, alloced, port_val, daily_returns]




def compute_std_dev(daily_returns):
    return daily_returns.std()

def compute_cum_ret(port_val):
    cum_ret = (port_val.iloc[-1] / port_val.iloc[0]) - 1
    return cum_ret

def compute_avg_daily_ret(daily_returns):
    return daily_returns.mean()

def get_normalized(prices):
    return prices/prices.iloc[0]

def compute_daily_returns(df):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:]/df[:-1].values)-1
    daily_returns.iloc[0] = 0
    return daily_returns

def get_portfolio_value(alloced):
    #pos_vals calculation
    pos_vals = alloced * 1000000
    port_val = pos_vals.sum(axis=1)
    return port_val

def get_alloced(normed, allocs):
    return normed * allocs

#GENERATE FILE PATH #REMOVETHIS
# def symbol_to_path(symbol, base_dir="/home/S/Projects/ML4T/ML4T_2024Summer/data"):
#     return os.path.join(base_dir, f"{str(symbol)}.csv")
#
# a = symbol_to_path('SPY')
# print(a)
# def get_data(symbol_list, dates): #REMOVETHIS
#     df_final=pd.DataFrame(index=dates)
#     if "SPY" not in symbol_list:
#         symbol_list.insert(0,"SPY")
#     for symbol in symbol_list:
#         file_path = symbol_to_path(symbol)
#         df_temp = pd.read_csv(file_path,
#                               parse_dates = True,
#                               index_col='Date',
#                               usecols=["Date", "Adj Close"])
#         df_temp.rename(columns={"Adj Close" : symbol}, inplace=True)
#         df_final = df_final.join(df_temp)
#         if symbol == 'SPY':
#             df_final=df_final.dropna(subset=['SPY'])
#     return df_final

def test_code():
    """  		  	   		 	   			  		 			 	 	 		 		 	
    This function WILL NOT be called by the auto grader.  		  	   		 	   			  		 			 	 	 		 		 	
    """  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    start_date = dt.datetime(2009, 1, 1)  		  	   		 	   			  		 			 	 	 		 		 	
    end_date = dt.datetime(2010, 1, 1)  		  	   		 	   			  		 			 	 	 		 		 	
    symbols = ["GOOG", "AAPL", "GLD", "XOM", "IBM"]  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # Assess the portfolio  		  	   		 	   			  		 			 	 	 		 		 	
    allocations, cr, adr, sddr, sr = optimize_portfolio(  		  	   		 	   			  		 			 	 	 		 		 	
        sd=start_date, ed=end_date, syms=symbols, gen_plot=False  		  	   		 	   			  		 			 	 	 		 		 	
    )  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
    # Print statistics  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Start Date: {start_date}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"End Date: {end_date}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Symbols: {symbols}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Allocations:{allocations}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Sharpe Ratio: {sr}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Volatility (stdev of daily returns): {sddr}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Average Daily Return: {adr}")  		  	   		 	   			  		 			 	 	 		 		 	
    print(f"Cumulative Return: {cr}")  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
  		  	   		 	   			  		 			 	 	 		 		 	
if __name__ == "__main__":  		  	   		 	   			  		 			 	 	 		 		 	
    # This code WILL NOT be called by the auto grader  		  	   		 	   			  		 			 	 	 		 		 	
    # Do not assume that it will be called  		  	   		 	   			  		 			 	 	 		 		 	
    test_code()

