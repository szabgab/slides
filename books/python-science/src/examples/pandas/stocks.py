import pandas
import pandas_datareader.data as web
all_data = { ticker: web.get_data_yahoo(ticker) for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']}

print(all_data.keys())          # dict_keys(['MSFT', 'IBM', 'AAPL', 'GOOG'])
print(all_data['MSFT'].keys())  # Index(['Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'], dtype='object')

price = pandas.DataFrame({ticker: data['Adj Close'] for ticker, data in all_data.items()})

print(price.head())

volume = pandas.DataFrame({ticker: data['Volume'] for ticker, data in all_data.items()})

print(volume.tail())

returns = price.pct_change()  # change in percentage
print(returns.head())

# correlation
print(returns.MSFT.corr(returns.IBM))   # 0.49532932971
print(returns.MSFT.corr(returns.AAPL))  # 0.389551383559

# covariance
print(returns.MSFT.cov(returns.IBM))    # 8.50115754064e-05
print(returns.MSFT.cov(returns.AAPL))   # 9.15254855961e-05

