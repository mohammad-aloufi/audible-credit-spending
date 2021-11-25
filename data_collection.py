import datetime
import pandas as pd

df = pd.read_csv('data.csv')
df.columns = ['price', 'hours', 'minutes', 'credit_spent']
price = float(input('Enter the price of the book'))
duration = input(
    'Enter the book duration.\nFor example:\nIf the book duration was 3 hours and 30 minutes, enter 3:30')
credit_spent = int(
    input('Did you end up buying the book?\n0 for no, 1 for yes'))
df = df .append({'price': price, 'hours': int(duration.split(':')[0]), 'minutes': int(
    duration.split(':')[1]), 'credit_spent': credit_spent}, ignore_index=True)
df.to_csv('data.csv', index=False)
