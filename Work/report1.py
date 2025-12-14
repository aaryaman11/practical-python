import csv
from pprint import pprint

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            # try:
            #     prices[row[0]] = float(row[1])
            # except IndexError:
            #     continue
            if not row:
               continue
            prices[row[0]] = float(row[1])
    return prices
pprint(read_prices('Data/prices.csv'))