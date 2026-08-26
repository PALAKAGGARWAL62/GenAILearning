"""
1. apply_discount(price, percent) -> returns discounted price
2. flat_discount(price) -> always subtract 50 from price
"""

def apply_discount(price, percent):
    return price*(1-0.01*percent)

def flat_discount(price):
    return price-50

