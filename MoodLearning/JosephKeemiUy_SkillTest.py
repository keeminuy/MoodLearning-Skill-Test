#Skill Test of Joseph Keemin Uy for MoodLearning
#September 2023
#Python Version 3.11.5


import pandas as pd

csv_file = 'data_test.csv'
dataframe = pd.read_csv(csv_file)
print(dataframe)
#_______________________________________________________________________________

#ANSWER#1: mean, median, and standard deviation of the price:

print('\nANSWER#1: mean, median, and standard deviation of the price:')

average_price = dataframe['Price'].mean()
print(f"\nAverage of Price: {average_price}")

median_price = dataframe['Price'].median()
print(f"Median of Price: {median_price}")

stdev_price = dataframe['Price'].std()
print(f"Standard deviation of Price: {stdev_price}")
#_______________________________________________________________________________

#ANSWER#2: sum, mean, max, min of the quantity sold of each product:

print('\nANSWER#2: sum, mean, max, min of the quantity sold of each product:')

sum_quantity = dataframe['Quantity'].sum()
print(f"\nSum of Quantity: {sum_quantity}")

average_quantity = dataframe['Quantity'].mean()
print(f"Average of Quantity: {average_quantity}")

max_quantity = dataframe['Quantity'].max()
print(f"Max amount of Quantity: {max_quantity}")

min_quantity = dataframe['Quantity'].min()
print(f"Minimum amount of Quantity: {min_quantity}")
#_______________________________________________________________________________

#ANSWER#3: Total Revenue:

print('\nANSWER#3: Total Revenue:')

total_revenue = dataframe.groupby('Product')['Price'].sum() * dataframe.groupby('Product')['Quantity'].sum()
print(f"\nTotal Revenue of each {total_revenue}")

total_revenue = (dataframe.groupby('Product')['Price'].sum() * dataframe.groupby('Product')['Quantity'].sum()).sum()
print(f"\nTotal Revenue of {total_revenue}")
#_______________________________________________________________________________

#ANSWER#4: More than 10 quantity sold:

print('\nANSWER#4: More than 10 quantity sold:')

entries = dataframe[dataframe['Quantity'] >10]
print('\nProducts with more than 10 Quantity Sold:\n')
print(entries)
#_______________________________________________________________________________

#ANSWER#5: Day of the highest Average Sales:

print('\nANSWER#5: Day of the highest Average Sales:')

average = dataframe.groupby('Date')['Quantity'].mean()
highest_sales_date = average.idxmax()
print(highest_sales_date)
#_______________________________________________________________________________

#ANSWER#6: Total sales for each Month:

print('\nANSWER#6: Total sales for each Month:\n')

dataframe['Date'] = pd.to_datetime(dataframe['Date'], format='%d/%m/%Y')
dataframe['Month'] = dataframe['Date'].dt.strftime('%Y %b')
month_sales = dataframe.groupby('Month')['Price'].sum().reset_index()

print(month_sales)

