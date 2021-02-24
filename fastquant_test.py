!pip install fastquant
from fastquant import backtest
df = user_portfolio
backtest("smac",df,fast_period=15,slow_period=40)