'''
1. calculate_total(prices) -> return total bill (sum of all prices)
2. apply_tax(amount) -> adds 5% tax
'''

def calculate_total(prices):
    total = 0
    for x in prices: total+=x
    return total

def apply_tax(amount):
    return amount*1.05
