# 2.1 Datatypes




# 2.2 Containers
portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.3),
    ('CAT', 150, 83.44)
]

# print(portfolio[0], portfolio[2])

# List Construction
records = []
records.append(('GOOG', 100, 490.10))
records.append(('IBM', 50, 91.3))

records = []
with open('Data/portfolio.csv', 'rt') as f:
    next(f)
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))
# print(records)

# Dictionary Contruction
prices = {}
prices['GOOG'] = 513.25
prices['CAT'] = 87.22
prices['IBM'] = 93.37
# print(prices)

prices = {}
with open('Data/prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        prices[row[0]] = float(row[1])
print(prices)