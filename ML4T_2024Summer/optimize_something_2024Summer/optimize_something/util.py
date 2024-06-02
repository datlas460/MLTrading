
import os
import pandas as pd

#GENERATE FILE PATH #REMOVETHIS
def symbol_to_path(symbol, base_dir="/home/S/Projects/ML4T/ML4T_2024Summer/data"):
    return os.path.join(base_dir, f"{str(symbol)}.csv")

a = symbol_to_path('SPY')
print(a)
def get_data(symbol_list, dates): #REMOVETHIS
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