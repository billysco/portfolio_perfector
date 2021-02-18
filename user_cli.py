import fire
import questionary
import pandas as pd

# Create main function
def calculate_goals():
    """Calculates how much money the user will need for retirement and how much they will need to save per year"""
    # print a welcome message
    print('Congratulations on taking the first step toward planning your retirement')
    # get user's desired income and store it as a variable
    monthly_retirement_income = questionary.text("What's your desired yearly income in retirement").ask()
    # get user's desired retirement age and store it as a variable
    retirement_age = questionary.text('What age would you like to retire?').ask()
    # get user's current retirement savings
    current_savings = questionary.text('How much money do you currently have saved for retirement').ask()
    # calculate how much money the user needs to retire
    retirement_goal = (100 - float(retirement_age))*float(monthly_retirement_income) - float(current_savings)
    # calculate if the user has enough money to retire 
    if retirement_goal <= float(current_savings):
        print('Congratulations! You already have enough money saved to reach your financial goals.')
    else:
        print(f"You will need ${retirement_goal} more in savings to reach your financial goal for retirement")

# run the program
def run():
    """The main function for running the script"""
    calculate_goals()

if __name__ == "__main__":
    fire.Fire(run)