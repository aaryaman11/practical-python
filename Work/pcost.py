# pcost.py
#
# Exercise 1.27
j = 0
with open('Data/portfolio.csv', 'rt')  as f:
    header = next(f).split(',') 
    for data in f:
        row = data.strip().split(",")
        share = int(row[1])
        prices = float(row[2])
        j += share*prices
    print('Total cost', j)