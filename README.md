# portfolio_perfector


# Planning for Retirement with APIs and Simulations

This is a python application. The CLI portion is written in VS Code, and the rest in written with Pandas in Jupyter Lab. The program uses the Requests library and makes an Alpaca API call in to retrieve the required data. Beginning with the CLI, the user is asked a series of questions regarding their personal information and retirement goals. The user input is written into a .csv file that is used by the Pandas application in jupyter lab. Using the imported data, the program runs risk analysis and forecasts for the portfolio that was tauilored to the user's risk tolerance, which was determined based on either their age or explicit preference.

![CLI Image](/Screenshots/CLI.jpg)

![Stocks vs Bonds](/Screenshots/stocks_vs_bonds_dr.jpg)

![MS Sim graph](/Screenshots/mc_sim_line.jpg)

---

## Technologies

The application is written using Pandas

The following packages are used:

Pandas - to write and run the program [Pandas documentation](https://pandas.pydata.org/docs/)

Json - as an encoder and decoder [Json documentation](https://docs.python.org/3/library/json.html)

os - miscellaneous operating system interfaces [os documentation](https://docs.python.org/3/library/os.html)

NumPy - for mathematical functions [NumPy documentation](https://numpy.org/doc/)

Requests - to send http requests [Requests documentation](https://requests.readthedocs.io/en/master/)

sqalchemy - to make SQL queries and read a database we use to make pandas dataframes - [sqalchemy documentation](https://docs.sqlalchemy.org/en/13/)

Alpaca Trade API - to retrieve real-time stock and bond data [Alpaca documentation](https://alpaca.markets/docs/api-documentation/)

MCForecastTools - to use Monte Carlo simulations [MC Simulation documentation](https://pythonprogramming.net/monte-carlo-simulator-python/)

Dotenv - to read and add a key-value pair to an environment [Dotenv documentation](https://pypi.org/project/python-dotenv/)

Pathlib - to create file paths [Pathlib documentation](https://docs.python.org/3/library/pathlib.html)

Datetime - to manipulate dates and times [Datetime documentation](https://docs.python.org/3/library/datetime.html)

Fastquant - to backtest investments [Fastquant documentation](https://pypi.org/project/fastquant/0.1.2.12/)

hvPlot - to create graphs [hvPlot documentation](https://hvplot.holoviz.org/)

Matplotlib - to create graphs [Matplotlib documentation](https://matplotlib.org/3.3.3/contents.html)


---

## Installation Guide

Install the Pandas package using the following command: 'import pandas as pd'

Install the json library using the following command: 'import json'

Install the os library using the following command: 'import os'

Install the numpy library using the following command: 'import numpy as np'

Install the Requests library using the following command: 'import requests'

Install sqlalchemy using the following command: 'import sqlalchemy'

Install the Alpaca Trade API using the following command: 'import alpaca_trade_api as tradeapi'

Install the Monte Carlo Simulation package using the following command: 'from MCForecastTools import MCSimulation'

Install the dotenv library using the following command: 'from dotenv import load_dotenv'

Install the Pathlib module using the following command: 'from pathlib import Path'

Install the Datetime module using the following command: 'import datetime'

Install the fastquant library using the following command: 'from fastquant import backtest,get_stock_data'

Install the hvPlot library using the following command: 'import hvplot.pandas'

Install the Matplotlib library using the following command: '%matplotlib inline'


--- 

## Usage

To run this program, clone the repository onto your computer, navigate to its source folder in your terminal and launch it using VS Code to access the CLI. Next, in tour command line run the command 'jupyter lab' then either run the entire program at once, or run the cells individually (in order) as you move through the file.

---

## Contributors

Billy Scolinos billyscolinos1@gmail.com

Susannah Slocum suzyslocum@gmail.com

Norman Chen normanc529@gmail.com

Ryan Felder rfelder@mail.sfsu.edu

---

## License

None
