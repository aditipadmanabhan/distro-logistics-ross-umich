'''
transaction file
'''

import csv

class LineItem:
    def __init__(self, sku, quantity):
        self.sku = sku
        self.quantity = int(quantity)
    def __repr__(self):
        return "(sku:{0} quantity:{1})".format(self.sku, self.quantity)

class Transaction:
    def __init__(self, is_online, line_items):
        self.is_online = is_online
        self.line_items = line_items

    def __repr__(self):
        return "Online:{0} Line Item: {1}".format(self.is_online, self.line_items)

class InventoryItem:
    def __init__(self, sku, is_online, regular_inv, wareroom_inv):
        self.sku = sku
        self.is_online = is_online
        self.regular_inv = int(regular_inv)
        self.wareroom_inv = int(wareroom_inv)
    def total_inv(self):
        return self.regular_inv + self.wareroom_inv

    def decrease_inv(self, is_online, quantity):
        if (is_online):
            temp_quantity = min(quantity, self.wareroom_inv)
            self.wareroom_inv -= temp_quantity
            quantity -= temp_quantity
            if (quantity > 0):
                self.regular_inv -= quantity
        else:
            self.regular_inv -= quantity
    def __repr__(self):
        return "sku:{0} Online:{1} Regular Inventory:{2} Wareroom Inventory:{3}".format(self.sku, self.is_online, self.regular_inv, self.wareroom_inv)


inventory = {}
with open('WareroomInv.csv', 'rU') as infile:
    reader = csv.reader(infile)
    reader.next()
    for row in reader:
        i = InventoryItem(row[0], row[4]=='1', row[2], row[3])
        inventory[i.sku] = i
    #print inventory

transactions = []
with open('MultTrans.csv', 'rU') as infile:
    reader = csv.reader(infile)
    reader.next()
    for row in reader:
        lineItems = []
        for i in range (2, int(row[1]) * 2 + 1, 2):
            lineItems.append( LineItem( row[i] , row[i+1]) )
        t = Transaction(row[22]=='1', lineItems)
        transactions.append(t)
    #print transactions

for transaction in transactions:
    for line_item in transaction.line_items:
        i = inventory[line_item.sku]
        i.decrease_inv(transaction.is_online, line_item.quantity)

with open('inventory_new.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    for item in inventory.values():
        writer.writerow([item.sku, item.total_inv(), item.regular_inv, item.wareroom_inv])
