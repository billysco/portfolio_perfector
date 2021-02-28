import pandas as pd
import fire
import questionary
import csv
import json
import os
import numpy as np
import requests
import sqlalchemy as sql
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation
from dotenv import load_dotenv
from pathlib import Path
import datetime
from fastquant import backtest,get_stock_data


# load the environment variables
load_dotenv()

# info = []

print('Congratulations on taking the first step toward planning your retirement')
# get user's current age
current_age = questionary.text("How old are you?").ask()
# get user's desired income and store it as a variable
yearly_retirement_income = questionary.text("What's your desired yearly income in retirement").ask()
# get user's desired retirement age and store it as a variable
retirement_age = questionary.text('What age would you like to retire?').ask()
# get user's current retirement savings 
current_savings = questionary.text('How much money do you currently have saved for retirement that you want to invest?').ask()
# calculate how much money the user needs to retire
retirement_goal = (100 - float(retirement_age))*float(yearly_retirement_income) - float(current_savings)

# determining allocation percentage, formatted as [.bonds,.stocks,.cryptocurrency]
if int(current_age) <= 30:
    allocation_pct = [0.0,0.7,0.3]
elif 30 < int(current_age) <= 40:
    allocation_pct = [0.2,0.6,0.2]
elif 40 < int(current_age) <= 50:
    allocation_pct = [0.4,0.4,0.2]
elif 50 < int(current_age) <= 60: 
    allocation_pct = [0.5,0.4,0.1]
else:
    allocation_pct = [0.7,0.2,0.1]

allocation = questionary.confirm(f"""Your recommended portfolio allocation percentage is {allocation_pct} ([%bonds,%stocks,%cryptocurrency]). 
    Would you like to accept this allocation? If not, you can pick your own portfolio allocation?""").ask()
if allocation:
    portfolio_allocation = allocation_pct
else:
    custom_bond = questionary.text('What percentage of your portfolio would you like to invest in bonds?').ask()
    custom_stock =  questionary.text('What percentage of your portfolio would you like to invest in stocks?').ask()
    custom_crypto = questionary.text('What percentage of your portfolio would you like to invest in cryptocurrency?').ask()
    #set the variable for custom allocation
    portfolio_allocation = [float(custom_bond),float(custom_stock),float(custom_crypto)]


# store client info in a list THIS IS USED FOR PRETTY MUCH EVERYTHING GOING FORWARD
info = [int(current_age),int(yearly_retirement_income),int(retirement_age),int(current_savings),int(retirement_goal),portfolio_allocation]

# Optional: export the client info to a csv file
header = ['current_age','yearly_retirement_income','retirement_age','current_savings','retirement_goal','portfolio_allocation']
output_path = Path("data/info.csv")
with open(output_path,'w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerow(info)
 

# Set response URLs
btc_url = "https://api.alternative.me/v2/ticker/Bitcoin/?convert=USD"

# Using the Python requests library, make an API call to access the current price of BTC
btc_response = requests.get(btc_url).json()

# Navigate the BTC response object to access the current price of BTC
btc_price = btc_response['data']['1']['quotes']['USD']['price']

# Set alpaca API key
alpaca_api_key = os.getenv('ALPACA_API_KEY')
alpaca_secret_key = os.getenv('ALPACA_SECRET_KEY')

# Create the Alpaca tradeapi.REST object
alpaca = tradeapi.REST(alpaca_api_key,alpaca_secret_key,api_version='v2') 

# Set the tickers to be used
tickers = ['AGG','QQQ']

# Set timeframe to 1D 
timeframe = '1D'

# Format current date as ISO format
# Set both the start and end date at the date of your prior weekday 
# This will give you the closing price of the previous trading day
start_date = pd.Timestamp('2016-02-25',tz='America/New_York').isoformat() # TODO update date
end_date = pd.Timestamp('2021-02-25',tz='America/New_York').isoformat() # TODO to update date

# Set client age
age = info[0]

# Use the Alpaca get_barset function to get current closing prices the portfolio
# Be sure to set the `df` property after the function to format the response object as a DataFrame
prices_df = alpaca.get_barset(tickers,timeframe,start=start_date,end=end_date).df

# Set the portfolio allocation %s from the client data provided
percent_stocks = portfolio_allocation[1]
# print(percent_stocks)
percent_bonds = portfolio_allocation[0]
# print(percent_bonds)
percent_crypto = portfolio_allocation[2]
# print(percent_crypto)

# Calculate the amount of money the client has in stocks, bonds, and cryptocurrency
stock_amt = percent_stocks*info[3]

btc_amt = percent_crypto*info[3]

bond_amt = percent_bonds *info[3]


# Determine what percent of the client's stock/bond portfolio is in stocks and how much is in bonds
if float(stock_amt) > 0:
    stock_weight = (float(stock_amt)+float(bond_amt))/float(stock_amt)
else:
    stock_weight = 0

if float(bond_amt) > 0:
    bond_weight = (float(bond_amt)+float(stock_amt))/float(bond_amt)
else:
    bond_weight = 0

# Set portfolio weights to be used for Monte Carlo simulation
portfolio_weights = [bond_weight,stock_weight]

# Set parameters for MCSim, currently set to 100 simulations over 1 year
MC_sim = (MCSimulation(portfolio_data=prices_df,weights=portfolio_weights,num_simulation=100,num_trading_days=252))

# Run the Monte Carlo
MC_sim.calc_cumulative_return()

# Get the data from the Monte Carlo simulation
cumulative_returns = MC_sim.summarize_cumulative_return()

# Set the mean return as a variable to be used in future calculations
mean_return = cumulative_returns['mean']
# print(mean_return)

# Set the years until retirement return as a variable to be used in future calculations
years_to_retirement = float(retirement_age)-float(current_age)
# print(years_to_retirement)

# Calculate the std dev
std_dev = cumulative_returns['std']

# Set qqq close as a variable
qqq_close = prices_df['QQQ']['close']

# Set qqq returns as a variable
stock_daily_returns = qqq_close.pct_change().dropna()

# Calate cumulative returns
stock_cumulative_returns = (1 + stock_daily_returns).cumprod()

# Calculate std dev
stock_std_dev = stock_cumulative_returns.std()

# Calculate annualized std dev
annualized_stock_std_dev = stock_std_dev * np.sqrt(252)

# Calculate avg annual stock returns
avg_annual_stock_returns = stock_daily_returns.mean()*252

# Calculate stock sharpe ratio
stock_sharpe_ratio = avg_annual_stock_returns/annualized_stock_std_dev

# Set the close price of agg as a variable
agg_close = prices_df['AGG']['close']

# Calculate the daily returns of bonds
bond_daily_returns = agg_close.pct_change().dropna()

# Calculate the cumulative returns of bonds
bond_cumulative_returns = (1 + bond_daily_returns).cumprod()

# Calculate std dev
bond_std_dev = bond_cumulative_returns.std()

# Calculate annualized std dev
annualized_bond_std_dev = bond_std_dev * np.sqrt(252)

# Calculate avg annual bond returns
avg_annual_bond_returns = bond_daily_returns.mean()*252

# Calculate bond sharpe ratio
bond_sharpe_ratio = avg_annual_bond_returns/annualized_bond_std_dev

# Calculate the sharpe ratio of the entire portfolio
portfolio_sharpe_ratio = (stock_weight*stock_sharpe_ratio)+(bond_weight*bond_sharpe_ratio)

# Calculate the amount of BTC owned if it was purchased today
btc_owned = btc_price/btc_amt

# Set the expected return for BTC (historical data would suggest a much higher return, however we are unsure if those returns are sustainable and it would be irresponsible to include returns that high in a retirement equation)
btc_expected_return = .25

# Calculate entire portfolio return
portfolio_mean_return = (mean_return-1)*(percent_stocks+percent_bonds)+btc_expected_return*percent_crypto
# print(percent_stocks,percent_bonds,percent_crypto,mean_return,btc_expected_return)

# Set retirement goal to get the present value of the user's retirement needs using the expected mean returns
pv_retirement_goal = retirement_goal/(1+portfolio_mean_return)**years_to_retirement
# print(pv_retirement_goal)

# Calculate the amount of money the user will need to contribute on a yearly basis
yearly_input = pv_retirement_goal/years_to_retirement
# print(yearly_input)

print(f"""In order to retire in {years_to_retirement} years, you will need an additional ${retirement_goal}. Your portfolio is expected to return {portfolio_mean_return:.2f}
every year.  Given this expected return, you will need to contribute {yearly_input:.2f} every year in order to retire on time.""")




# database_connection_string = 'sqlite:///'

# engine = sql.create_engine(database_connection_string)

# engine.table_names()

# user_data_df = pd.DataFrame([current_age,yearly_retirement_income,retirement_age,current_savings,retirement_goal,portfolio_allocation])
# user_data_df.to_sql('info',engine)