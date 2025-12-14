# report.py
#
# Exercise 2.4
import csv
from pprint import pprint
def read_portfolio(filename):
    portfolio =  []
    # total_value = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holdings = {
                'name': row[0], 
                'share': int(row[1]), 
                'price': float(row[2])
                }
            portfolio.append(holdings)
            # total_value += holdings['share'] * holdings['price']

    # print('Total value of portfolio: ', total_value)
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if not row:
               continue
            prices[row[0]] = float(row[1])
    return prices


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
def compute_value(portfolio, prices):
    total_value = 0.0
    gain_loss = 0.0
    for holding in portfolio:
        total_value += holding['price'] * holding['share']
        gain_loss += (prices[holding['name']] - holding['price']) * holding['share']
    return total_value, gain_loss

total_value, gain_loss = compute_value(portfolio, prices)
print('Total value of portfolio: ', total_value, ' Gain/Loss: ', gain_loss)
#pprint(portfolio)


