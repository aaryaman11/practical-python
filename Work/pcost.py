# pcost.py
#
# Exercise 1.27

import csv
import sys

# with open('Data/portfolio.csv', 'rt')  as f:
#     header = next(f).split(',') 
#     for data in f:
#         row = data.strip().split(",")
#         share = int(row[1])
#         prices = float(row[2])
#         j += share*prices
#     print('Total cost', j)

def portfoloio_cost(filename):
    j = 0
    with open(filename, 'rt')  as f:
        row = csv.reader(f)
        # print(row)
        header = next(row)
        # print('Header: ', header)
        for data in row:
            # print('Data: ', data)
            
            try:
                share = int(data[1])
                prices = float(data[2])
            except ValueError:
                print('Missing data', data)
                continue
            # share = int(row[1])
            # prices = float(row[2])
            j += share*prices
    return j

if len(sys.argv)  == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfoloio_cost(filename)
error_cost = portfoloio_cost('Data/missing.csv')
print(sys.argv)
print('Error cost: ', error_cost)
print('Total cost: ', cost)