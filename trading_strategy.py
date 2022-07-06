import pandas
from pandas import read_excel
import matplotlib.pyplot as plt
import numpy as np

my_sheet = 'HINDALCO' 
file_name = 'HINDALCO_1D.xlsx'
df = read_excel(file_name, sheet_name = my_sheet)

#print(df['close'])

def SMA(data, period = 50, column='close'):
    return data[column].rolling(window=period).mean()

df['SMA50'] = SMA(df,50)
df['SMA200'] = SMA(df,200)

# Getting the Buy and Sell Signals
df['Signal'] = np.where(df['SMA50'] > df['SMA200'],1,0)
df['Position'] = df['Signal'].diff()

df['Buy'] = np.where(df['Position'] == 1, df['close'], np.NAN)
df['Sell'] = np.where(df['Position'] == -1, df['close'],np.NAN)


plt.figure(figsize=(14,7))
plt.title('Close Price History with Buy & Sell Signals', fontsize=18)
plt.plot(df['close'], alpha=0.5, label='Close')
plt.plot(df['SMA50'], alpha=0.5, label='SMA50')
plt.plot(df['SMA200'], alpha=0.5, label='SMA200')
plt.scatter(df.index, df['Buy'], alpha=1, label='Buy Signal', marker='^', color='green')
plt.scatter(df.index, df['Sell'], alpha=1, label='Sell Signal', marker='v', color='red')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price', fontsize=18)
plt.show()

