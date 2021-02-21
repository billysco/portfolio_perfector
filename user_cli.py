import fire
import questionary
import pandas as pd
import csv
from pathlib import Path

user_info = []

# Create function to get user's information and goals for retirement
def calculate_goals():
    """Calculates how much money the user will need for retirement and how much they will need to save per year"""
    # print a welcome message
    print('Congratulations on taking the first step toward planning your retirement')
    # get user's current age
    current_age = questionary.text("How old are you?").ask()
    # get user's desired income and store it as a variable
    monthly_retirement_income = questionary.text("What's your desired yearly income in retirement").ask()
    # get user's desired retirement age and store it as a variable
    retirement_age = questionary.text('What age would you like to retire?').ask()
    # get user's current retirement savings 
    current_savings = questionary.text('How much money do you currently have saved for retirement').ask()
    # calculate how much money the user needs to retire
    retirement_goal = (100 - float(retirement_age))*float(monthly_retirement_income) - float(current_savings)
    # store client info in a list
    # info = [current_age,monthly_retirement_income,retirement_age,current_savings,retirement_goal]
    # for x in info:
    #     user_info.append(str(x))
    user_info.append(str(current_age))
    user_info.append(str(monthly_retirement_income))
    user_info.append(str(retirement_age))
    user_info.append(str(current_savings))
    user_info.append(str(retirement_goal)) 
    # calculate if the user has enough money to retire 
    if retirement_goal <= float(current_savings):
        print('Congratulations! You already have enough money saved to reach your financial goals.')
    else:
        print(f"You will need ${retirement_goal} more in savings to reach your financial goal for retirement")
    

print(user_info)


def get_investment_preferences():
    """Get the user's investment preferences"""
    # ask the user if they want to pick their own allocation
    allocation = questionary.confirm('Do you want to pick your own investment allocations?').ask()
    if allocation:
        self_allocation_pct = questionary.text("""Please select the amount of your portfolio to allocate
        to bonds, stocks, and cryptocurrency. Please format your response like the following [.bonds,.stocks,.cryptocurrency]""").ask()
    else:
        allocation_pct = 100-current_age
    




def save_user_info(user_info):
    """Save the user information for use in Jupyter lab portion of application.

    Args:
        user_info (list): The user's information, gathered from the questions above
    """
    header = ['current_age','monthly_retirement_income','retirement_age','current_savings','retirement_goal']
    output_path = Path("data/user_info.csv")
    with open(output_path,'w',newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(user_info)

# run the program
def run():
    """The main function for running the script"""
    calculate_goals()

    save_user_info(user_info)

if __name__ == "__main__":
    fire.Fire(run)


# add in age, desired retirement age, current savings, current income, current monthly expenses
# risk tolerance
# 100-x for portfolio allocation (factor in real estate and crypto)
# Would you  like to select your own risk level or pre calculated
# Warning for bad portfolio selection
# modules 4 and 5
# save csv data at the end
# add .csv file at the end to save csv data