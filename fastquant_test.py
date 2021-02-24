""" Test run space for fastquant
-For later use on the user's templated or unique portfolio
"""

##!pip install fastquant
from fastquant import backtest, get_stock_data

user_portfolio = get_stock_data("AGG","2019-01-01", "2020-12-31")

df = user_portfolio
backtest("smac",df,fast_period=15,slow_period=40)