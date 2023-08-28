#importing csv library to allow working with spreadsheet file

import csv



#reading the data from the spreadsheet with use of dictreader from csv library

with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader



#instaling pandas library with the use of terminal command 'pip install pandas'

import pandas as pd




#printing the title for imported data

print('')
print('Sales and expenditure for each month:')




#import all rows of CSV into DataFrame (variable df)

df = pd.read_csv('sales.csv')
print('')
print(df)





#printing sales column with use of to_string() function which allows to print only the values in the sales column
#double bracket in 'sales' allows to print column header as well

print('')
print(df[['sales']].to_string(index=False))





#printing total amount of sales across all months
#use of dataframe.sum() function

print('')
print('Total sales across all months:')
sales_total = df['sales'].sum()
print(sales_total)





#-------EXTRA-------
#printing average of sales across all months
#use of dataframe.mean() function

sales_mean = df['sales'].mean()
print('')
print('Average sales across all months:')
print(sales_mean)
print('')
