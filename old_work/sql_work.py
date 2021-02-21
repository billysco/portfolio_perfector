import sqlalchemy as sql
import pandas as pd

# CREATE DATABASE userDB;

# CREATE TABLE user_info(
#     'current_age' bigint,
#     'yearly_retirement_income' bigint,
#     'retirement_age' bigint,
#     'current_savings' bigint,
#     'retirement_goal' bigint,
#     'portfolio_allocation' varchar
# )

database_connection_string = 'sqlite:///'

engine = sql.create_engine(database_connection_string)

engine.table_names()



# info = [int(current_age),int(yearly_retirement_income),int(retirement_age),int(current_savings),int(retirement_goal),portfolio_allocation]