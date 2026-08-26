# Assignment 6 - Exception Handling

Note: All the tasks are there in Assignment6.ipynb

## Basic instuctions to run the code
Python notebook contains following type of cells
1. markdown cells for task heading
2. code cells for the task logic

You can open the task folder in JupyterLab or VS code
1. Complete notebook can be executed in 1 shot using Run All option in the Jupyter Notebook
2. You can execute each cell 1 by using play button against it


## Task 1: Safe Division Utility
Cell 3 demonstrates the following code 
Write a Program 
1. Takes 2 inputs from the user: numerator and denominator
2. Uses try-except to handle:
 - ValueError (if input is not a number)
 - ZeroDivisionError (if denominator = 0)
3.If no error occurs, print the result inside the else block
4. In finally block print('Operation Complete')

## Task 2: Bill Calculator with Error Handling
Cell 5 Demonstrates the following code
Given a list of product prices:
prices = [120, 350, 'abc', 500, -200, 800]
Write a Program 
1. Iterate through the list
2. Tries to add only valid(+ive num) prices to the total
3. Handles
- TypeError if value is not a number
- Custom exeception using raise ValueError ('Negative price not allowed')
4. Prints the running Total.
Expected Behaviour: 
Skip invalid items but continue processing

##  Task 3: Custom Exception: Age Validator
Cell 7 demonstrates the following code
1. Write function to check_age(age) that:
- Raise a custom Exception ValueError("Age must be between 1 and 120) if age is out of range
2. In your main code:
- Take age input from the user
- Use try-except to catch and print the custom error message

## Task 4: File Reader with Exception Handling
1. Ask the user for a filename
2. Try to open and read the file
3. Handle:
- FileNotFoundError
- PermissionError
4. If successful, print first 3 lines of the file
5. Use finally to print - 'File operation attempted'

## Task 5: Mini Program: Safe Shopping Cart
Create a program
1. Has cart list -> cart = []
2. Runs a loop asking user to enter prices
3. stops when user enters 'q'
4. Inside the loop:
- Convert unpirt to a float
- Handle ValueError if user enters invalid input
- Raise custom exception if price is negative
5. At it end print:
- Total items
- Total bill
