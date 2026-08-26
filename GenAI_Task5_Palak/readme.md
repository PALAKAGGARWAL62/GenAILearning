# Assignment 5: Importing, Creating modules and packages

## Task 1: Create a Simple Module (math_utils.py)
path - GenAI-Task5-Palak>modules_assignment>math_utils.py
Create a module math_utils.py with following functions
1. add(a, b) -> return a+b
2. subtract(a, b) -> return a-b
3. square(n) -> return n*n
In main.py import the module in 2 ways
 - import math_utils
 - from math_utils import sqaure 
Test all functions

### Code Execution
Run main.py on terminal 
Output will appear on terminal

## Task 2: Create Module string_utils.py
1. capitalize_words(text) -> return text with each word capitalized
2. reverse_string(text) -> return reversed string
3. word_count(text) -> return number of words in the text
import in main and test all the functions

### Code Execution
Run main.py on terminal 
Output will appear on terminal

## Task 3: Create a package (shop_package)
Directory structure
modules_assignment\shop_package
    shop_package\discount.py
    shop_package\billing.py
    shop_package\__init__.py

### discount.py
1. apply_discount(price, percent) -> returns discounted price
2. flat_discount(price) -> always subtract 50 from price

### billing.py
1. calculate_total(prices) -> return total bill (sum of all prices)
2. apply_tax(amount) -> adds 5% tax

### __init__.py
from .discount import apply_discount, flat_dicount
from .billing import calculate_total, apply_tax
(This will allow calling functions directly from package)

## Task 4: Import Package in main.py
In main.py do the following:
1. import shop_package.discount as disc
2. from shop_package.billing import calculate_total
3. Call every function inside the package
4. Use every function

### Code Execution
Run main.py on terminal 
Output will appear on terminal

We are able to use function as apply_tax or flat_discount because of code in init file
otherwise we need to write like
shop_package.billing.apply_tax()
shop_package.discount.flat_discount()