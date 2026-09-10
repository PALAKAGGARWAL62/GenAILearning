# Assignment 10: Pandas (Series, DataFrame, Functions, Filtering & Analysis)

All Code related to below tasks is in Assignment10.ipynb

## Task 1: Pandas Series Basics
Cell 3 demonstrates the below code
1. Import pandas as pd.
2. Create a Pandas Series from the list:
3. marks = [78, 85, 90, 66, 72]
4. Print:
o Series values
o Index
o Data type
5. Access:
o First element
o Last two elements

## Task 2: Mathematical Operations on Series
Cell 5 demonstrates the below code
Using the marks Series:
1. Add 5 grace marks to all students.
2. Subtract 2 marks from all values.
3. Multiply all marks by 1.05.
4. Divide all marks by 2.
Print results for each operation.

## Task 3: Python Functionalities on Series
Cell 7 demonstrates the below code
Using the same Series:
1. Find:
o Maximum marks
o Minimum marks
o Sum of marks
o Mean marks
2. Apply a lambda function to check whether each student has passed (>= 70).
3. Count how many students passed.

## Task 4: Create a DataFrame
Cell 9 demonstrates the below code
Create a DataFrame students:
students = {
'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
'Marks': [78, 85, 90, 66, 72],
'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}
1. Convert it into a DataFrame.
2. Print first 3 rows.
3. Print last 2 rows.
4. Print DataFrame shape and column names.

## Task 5: Important DataFrame Functions
Cell 11 demonstrates the below code
Using the students DataFrame:
1. Use and print output of:
o .info()
o .describe()
o .head()
o .tail()
2. Sort students by Marks in descending order.
3. Reset index after sorting.

## Task 6: Filtering & Conditional Selection
Cell 13 demonstrates the below code
Perform the following filters:
1. Students who scored more than 75 marks.
2. Students belonging to subject Math.
3. Students who scored more than average marks.
4. Students who failed (marks < 70).

## Task 7: Grouping & Basic Analysis
Cell 15 demonstrates the below code
1. Find average marks per subject using groupby().
2. Count number of students per subject.
3. Find maximum marks per subject.

## Task 8: Pandas Plotting (Simple Graphs)
Cell 17, 18, 19, 20 demonstrates the below code
Using Pandas built-in plotting:
1. Plot a bar graph of student names vs marks.
2. Plot a line graph of marks.
3. Plot a histogram of marks.
Note: Use only:
DataFrame.plot()
Series.plot()
(No matplotlib customization required.)

## Task 9:  Mini Use Case: Sales Data Analysis
Cell 22 demonstrates the below code
Create a DataFrame:
sales = {
'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
'Revenue': [1200, 1500, 900, 2000, 1800]
}
Perform:
1. Total revenue
2. Average daily revenue
3. Day with highest revenue
4. Days where revenue > average
5. Plot revenue vs day
