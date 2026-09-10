# Assignment 9: NumPy (Mathematical & Statistical Operations)

All the code is in file Assignment9.ipynb
You can execute the cells to check the output

## Task 1: Creating NumPy Arrays
Cell 3 demonstrates the below code
1. Import NumPy as np.
2. Create the following arrays:
o A 1D array of integers from 1 to 10
o A 2D array of shape (3, 3) with values from 1 to 9
o A NumPy array from the list: [10, 20, 30, 40, 50]
3. Print:
o Shape of each array
o Data type of each array

## Task 2: Important Mathematical Operations
Cell 5 demonstrates the below code
Given two arrays:
A = np.array([10, 20, 30, 40])
B = np.array([1, 2, 3, 4])
Perform and print results for:
1. Addition (A + B)
2. Subtraction (A - B)
3. Multiplication (A * B)
4. Division (A / B)
5. Power (A ** 2)
Extra (optional): Use NumPy functions: np.add(), np.subtract() for the same operations.

## Task 3: Important NumPy Mathematical Formulas
Cell 7 demonstrates the below code
Given:
values = np.array([2, 4, 6, 8, 10])
Calculate:
1. Square root of each element
2. Exponential of each element
3. Natural logarithm of each element
4. Sum of all elements
5. Cumulative sum of elements
Use NumPy functions only.

## Task 4: Aggregation Operations
Cell 9 demonstrates the below code
Given a 2D array:
data = np.array([
[10, 20, 30],
[40, 50, 60],
[70, 80, 90]
])
Find:
1. Row-wise sum
2. Column-wise sum
3. Minimum value
4. Maximum value
5. Overall mean

## Task 5: Statistical Operations (Core Focus)
Cell 11 demonstrates the below code
Given:
marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])
Calculate and print:
1. Mean
2. Median
3. Variance
4. Standard Deviation
5. Minimum & Maximum
6. Range (max - min)

## Task 6: Percentiles & Sorting
Cell 13 demonstrates the below code
Using the same marks array:
1. Sort the array
2. Find:
o 25th percentile
o 50th percentile
o 75th percentile
3. Count how many students scored above the average marks

## Task 7: Mini Use Case: Sales Analysis
Cell 15 demonstrates the below code
Given daily sales data:
sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])
Perform:
1. Total weekly sales
2. Average daily sales
3. Highest and lowest sales day
4. Standard deviation of sales
5. Identify days where sales were above average
