'''
test cases
'''

from StoreTransactions import *
#
# i = InventoryItem(1, True, 5, 5)
# i.decrease_inv(True, 8)
# print i
#
# i = InventoryItem(1, True, 5, 5)
# i.decrease_inv(True, 3)
# print i
#
# i = InventoryItem(1, True, 5, 5)
# i.decrease_inv(True, 5)
# print i
#
# i = InventoryItem(1, True, 5, 0)
# i.decrease_inv(True, 3)
# print i


i = InventoryItem(1, False, 5, 3)
i.decrease_inv(False, 3)
print i

i = InventoryItem(1, False, 0, 4)
i.decrease_inv(False, 3)
print i
