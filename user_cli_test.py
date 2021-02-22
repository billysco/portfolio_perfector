import fire
import questionary
import pandas as pd
import csv
from pathlib import Path
import sqlalchemy as sql

# user_info = []

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

# allocation = questionary.confirm('Do you want to pick your own investment allocations?').ask()
# if allocation:
#     self_allocation_pct = questionary.text("""Please select the amount of your portfolio to allocate
#     to bonds, stocks, and cryptocurrency. Please format your response like the following [.bonds,.stocks,.cryptocurrency]""").ask()
# else:
#     allocation_pct = 100-current_age

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
    Would you like to accept this allocation or pick your own portfolio allocation?""").ask()
if allocation:
    portfolio_allocation = allocation_pct
else:
    custom_bond = questionary.text('What percentage of your portfolio would you like to invest in bonds?').ask()
    custom_stock =  questionary.text('What percentage of your portfolio would you like to invest in stocks?').ask()
    custom_crypto = questionary.text('What percentage of your portfolio would you like to invest in cryptocurrency?').ask()
    #set the variable for custom allocation
    portfolio_allocation = [custom_bond,custom_stock,custom_crypto]


# store client info in a list
info = [int(current_age),int(yearly_retirement_income),int(retirement_age),int(current_savings),int(retirement_goal),portfolio_allocation]

header = ['current_age','yearly_retirement_income','retirement_age','current_savings','retirement_goal','portfolio_allocation']
output_path = Path("data/user_info.csv")
with open(output_path,'w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerow(info)


# database_connection_string = 'sqlite:///'

# engine = sql.create_engine(database_connection_string)

# engine.table_names()

# user_data_df = pd.DataFrame([current_age,yearly_retirement_income,retirement_age,current_savings,retirement_goal,portfolio_allocation])
# user_data_df.to_sql('info',engine)