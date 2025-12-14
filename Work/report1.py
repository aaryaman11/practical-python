import csv

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            prices[row[0]] = row[1]
        print(prices)
print(read_prices('Data/prices.csv'))