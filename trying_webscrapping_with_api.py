from pycoingecko import CoinGeckoAPI
import pandas as pd
import plotly.graph_objects as go

#Simple API Web Scrapping Part 1

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

print("Hi! here the updated price of the bitcoin in USD dollars:")
print(bitcoin_data)
print("")

bitcoin_price_data = bitcoin_data['prices']

print("Here the formatted list, only with prices, I'll use this to make Data Analysis:")
print(bitcoin_price_data)

data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])

print("And now I'll create a DataFrame with Pandas for this data:")
print(data)
print("")

print("Getting the TimeStamp values to make a better Date view in a new column:")
data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms') #Getting the TimeStamp values to make a better Date view in a new column
print(data)
print("")


candlestick_data = data.groupby(data.Date.dt.date).agg({'Price': ['min', 'max', 'first', 'last']})
print("Now we'll format a little more the data!(But is a new dataframe based on the above) Look:")
print(candlestick_data)
print("")

print("Now we'll plot a figure with this Data!")

fig = go.Figure(data=[go.Candlestick(x = candlestick_data.index,
                open=candlestick_data['Price']['first'],
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'],
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False, xaxis_title='Date',
yaxis_title='Price (USD $)', title='Bitcoin Candlestick Chart Over Past 30 Days' )

fig.show()