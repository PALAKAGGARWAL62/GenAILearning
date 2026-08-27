# Assignment 7: Object-Oriented Programming (OOP)


## Task 1: Basic Class & Object Creation
Create a class Product with:
Attributes: name, price, category
Method: get_info() → prints product details
Create two objects and call get_info().
Extra (optional): Add a method apply_discount(percent) that returns the discounted price.

## Task 2: Constructor & Encapsulation
Modify the Product class:
Make price a private attribute (__price).
Create getter & setter methods:
o get_price()
o set_price(new_price) → should update only if new_price > 0
Test modifying price using the setter.

## Task 3: Inheritance (Single-Level)
Create a subclass ElectronicProduct that inherits from Product.
Additional attribute:
warranty_years
Override the get_info() method to include warranty info.
Create an object and demonstrate inheritance + overriding.

## Task 4: Polymorphism
Create two classes:
Laptop(Product)
Mobile(Product)
Both override:
def get_info(self):
Print details in their own style
Write a loop that iterates over objects of Laptop and Mobile and calls get_info() on each to
show polymorphism.

## Task 5: Abstraction (Using Abstract Base Class)
Create an abstract class Payment with abstract method:
process_payment(amount)
Then create two subclasses:
CreditCardPayment
UPIPayment
Both override process_payment() with simple print statements.
Test all classes.

## Task 6: Magic Methods & Operator Overloading
Add the following to your Product class:
1. __str__ method
Returns a readable string:
Product(name, price, category)
2. Operator Overloading (__add__)
Allow:
product1 + product2
To return the total combined price.
Test this with two product objects.

## Task 7: Mini Project: Simple Inventory System (OOP Only)
Create two classes:
Class: Inventory
Attributes:
products → list to store product objects
Methods:
add_product(product)
remove_product(name)
get_total_value() → sums prices of all products
show_all_products() → prints info for each product
Class: Store
Attributes:
store_name
inventory → an Inventory object
Methods:
add_new_product() → takes input & creates Product object
show_summary() → prints total items & value
Important: Use only OOP concepts — no file handling, no exceptions, no packages.

Test the system by:
1. Creating a Store object
2. Adding 3 products
3. Showing summary
4. Using __add__ to combine prices of two products
