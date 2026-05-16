# report.py
#
# Exercise 2.4
import csv

# def portfolio_cost(filename):
#     '''Computes the total cost (shares*price) of a portfolio file'''
#     total_cost = 0.0

#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             nshares = int(row[1])
#             price = float(row[2])
#             total_cost += nshares * price
#     return total_cost

# Exercise 2.4 List of Tuples
# def read_portfolio(filename):
#     portfolio = []
#     with open(filename, 'rt') as f:
#         next(f)
#         rows = csv.reader(f)
#         for row in rows:
#             holding = (row[0], int(row[1]), float(row[2]))
#             portfolio.append(holding)
#     return portfolio

# Exercise 2.5 List of Dictionaries
def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        headers = next(f).strip().split(',')
        rows = csv.reader(f)
        for row in rows:
            holding = {
                headers[0]:row[0], 
                headers[1]:int(row[1]), 
                headers[2]:float(row[2])
            }
            portfolio.append(holding)
    return portfolio


# print(read_portfolio('Data/portfolio.csv'))

# Exercise 2.6: Dictionaries as a container
def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as p:
        rows = csv.reader(p)
        for row in rows:
            if row:
                try:
                    name = row[0]
                    price = float(row[1])
                    prices[name] = price # inserts into the dictionary
                except ValueError:
                    print(f'Skipping bad data: {row}')
            
    return prices

# print(read_prices('Data/prices.csv'))

# Exercise 2.7 Finding out if you can retire
# def retirement(portfolio_file, prices_file):
#     portfolio = read_portfolio(portfolio_file)
#     prices = read_prices(prices_file)
#     total_cost = 0.0
#     total_value = 0.0
#     for stock in portfolio:
#         name = stock['name']
#         shares = stock['shares']
#         purchase_price = stock['price']

#         current_price = prices[name]

#         total_cost += shares * purchase_price
#         total_value += shares * current_price
#     print(f'Total cost: {total_cost:0.2f}')
#     print(f'Current value: {total_value:0.2f}')
#     print(f'Profit/Loss: {total_value - total_cost}')

# retired = retirement('Data/portfolio.csv', 'Data/prices.csv')
# if retired:
#     print('Yayy!! I can retire now')
# else:
#     print('Not yet, Stay focused')

# Exercise 2.9 Collecting Data
def make_report(file1, file2):
    report = []
    