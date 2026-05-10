# pcost.py
#
# Exercise 1.27
total_cost = 0
with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    # print(f"HEADER: {headers.strip()}")
    # print("_" * 15)

    for line in f:
        row = line.split(',')
        num_shares = int(row[1]) #second item in the row
        price = float(row[2]) #third item in the row
        total_cost = total_cost + (num_shares * price)
        #print(line.strip())

print(f'Total cost {total_cost}')
print("_" * 20)

# import gzip
# with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
#     for line in f:
#         print(line, end='')
