# Main file to execute all the modules and packages defined 
"""
In main.py import the module in 2 ways
 - import math_utils
 - from math_utils import sqaure 
""" 
print('\n\n Task 1')

import math_utils
print("Using import math_utils")
print('Adding 10 and 20: ', math_utils.add(10, 20))
print('Subtracting 10 and 20: ', math_utils.subtract(10, 20))
print('Square 10: ', math_utils.square(10))

from math_utils import add, subtract, square
print("Using from math_utils import add, subtract, square")
# the difference here is we do not need to write math_utils and also instead of impporting complete module we can import specific functions of choice
print('Adding 10 and 20: ', add(10, 20))
print('Subtracting 10 and 20: ', subtract(10, 20))
print('Square 10: ', square(10))

print('\n\n Task 2')

# import string_utils in main and test all the functions
from string_utils import capitalize_words, word_count, reverse_string
print('Capitalized text- Hello TuteDude: ',capitalize_words('Hello TuteDude'))
print('Reverse text- Hello TuteDude: ',reverse_string('Hello TuteDude'))
print('Word count - Hello TuteDude: ',word_count('Hello TuteDude'))

# Task 4 - usage of functions from the package
print('\n\n Task 4')
import shop_package.discount as disc
from shop_package.billing import calculate_total
# import all functions from shop_package

print('Apply Discount 30% to price of 3500: ', disc.apply_discount(3500, 30))
print('Calculate Total Price [1000, 3000, 200, 4500, 234, 454, 6300] : ', calculate_total([1000, 3000, 200, 4500, 234, 454, 6300]))

from shop_package import *
print('Apply Flat Discount to price of 3500: ', flat_discount(3500))
print('Apply Discount 25% to price of 5000: ', apply_discount(3500, 30))

print('Calculate Total Price [1000, 3000, 200, 4500, 234, ] : ', calculate_total([1000, 3000, 200, 4500, 234, ]))
print('Apply tax to the amount of 5000: ', apply_tax(5000))

