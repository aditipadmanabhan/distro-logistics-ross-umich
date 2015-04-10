'''
transaction file
'''

import csv

inventory1 = {}
with open('inventory.csv', 'rU') as infile:
    reader = csv.reader(infile)
    reader.next()
    inventory1 = {rows[0]:rows[1] for rows in reader}

for inventory in inventory1:
    for k in inventory1:
        inventory1[k] = int(inventory1[k])

transactions = []
with open('transactions.csv', 'rU') as infile:
    reader = csv.reader(infile)
    reader.next()
    transactions = [ [ rows[1],int(rows[2]) ] for rows in reader]


for transaction in transactions:
    inventory1[transaction[0]] -= transaction[1]

with open('inventory_new.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(inventory1.iteritems())