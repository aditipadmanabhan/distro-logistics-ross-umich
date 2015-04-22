'''
test cases
'''

from StoreTransactions import *

i = InventoryItem(1, True, 5, 5)
print i.decrease_inv(True, 8), i

i = InventoryItem(1, True, 5, 5)
print i.decrease_inv(True, 3), i

i = InventoryItem(1, True, 5, 5)
print i.decrease_inv(True, 5), i

i = InventoryItem(1, True, 5, 0)
print i.decrease_inv(True, 3), i

i = InventoryItem(1, False, 5, 3)
print i.decrease_inv(False, 3), i

i = InventoryItem(1, False, 0, 4)
print i.decrease_inv(False, 3), i

i = InventoryItem(1, True, 5, 5)
print i.decrease_inv(False, 8), i

i = InventoryItem(1, True, 5, 3)
print i.decrease_inv(True, 10), i

