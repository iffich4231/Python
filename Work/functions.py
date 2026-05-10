def sumcount(n):
    # Returns the sum of the first n integers
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

# a= sumcount(100)
# print(a)

# import math
# x = math.sqrt(16)
# print(x)

# import urllib.request
# u = urllib.request.urlopen('https://www.python.org/')
# data = u.read()
# print(data)

# for line in file:
#     fields = line.split(',')
#     try:
#         shares = int(fields[1])
#     except ValueError:
#         print("Couldn't parse", line)

# raise RuntimeError('What a kerfuffle')

# def greeting(name):
#     'Issues a greeting' # this first string statement serves as docu
#     print('Hello', name)

# greeting('iffi')
# help(greeting)

# def portfolio_cost(filename):
#     "calculates the total cost of all the shares"
#     total_cost = 0
#     with open(filename, 'rt') as f:
#         headers = next(f)
#         for line in f:
#             row = line.split(',')
#             try:
#                 num_shares = int(row[1]) #second item in the row
#                 price = float(row[2]) #third item in the row
#             except ValueError:
#                 print("Couldn't parse", line)
#             total_cost = total_cost + (num_shares * price)

#     print(f'Total cost {total_cost}')
#     print("_" * 20)

# help(portfolio_cost)
import csv
# def portfolio_cost(filename):
#     total_cost = 0
#     with open(filename) as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             try:
#                 num_shares = int(row[1]) #second item in the row
#                 price = float(row[2]) #third item in the row
#             except ValueError:
#                 print("Couldn't parse", row)
#             total_cost = total_cost + (num_shares * price)

#     print(f'Total cost {total_cost}')
#     print("_" * 20)

import sys

def portfolio_cost(filename):
    total_cost = 0
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                num_shares = int(row[1]) #second item in the row
                price = float(row[2]) #third item in the row
            except ValueError:
                print("Couldn't parse", row)
            total_cost = total_cost + (num_shares * price)
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else: 
        filename = 'Data/portfolio.csv'
        
    print(f'Total cost {total_cost}')
    print("_" * 20)

portfolio_cost('Data/portfolio.csv')