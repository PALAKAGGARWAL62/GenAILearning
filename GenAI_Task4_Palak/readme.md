# This Assignment includes File handling operations (Read, Write, Append, Modes) 
Note: All the tasks are there in Assignment4.ipynb

## Basic instuctions to run the code
Python notebook contains following type of cells
1. markdown cells for task heading
2. code cells for the task logic

You can open the task folder in JupyterLab or VS code
1. Complete notebook can be executed in 1 shot using Run All option in the Jupyter Notebook
2. You can execute each cell 1 by using play button against it

## Task 1
Cell 3 contains task 1
It demonstrate writing data to the file
1. open file
2. write the data
3. close the file

Data is written in new line as well as comma separated. Code can be uncommented as per need

## Task 2
Cell 5
It deals with reading file in different ways
1. read(): Read the complete file as a string
2. readline(): Reads the first line of the file
3. readlines(): Reads the file in the form of list. Each row is the element in the list.

## Task 3
Cell 7
It deals with appending data to the exisiting file
Open file in a+ mode
It will help in appending and reading the existing file with curser at the end of the file

## Task 4
Cell 9
1. Reading data from file using readlines
2. Coversion of data to integer format using map and lambda function
3. loop over data to find the parameters asked

## Task 5
Cell 11
1. Taking user input in the loop to take it 3 times. Range us specified from 1 to 4 to show the input counter
2. Formatted the data taken and entered to the file
Cell 12
Read and format the data written in the file in the above step

## Task 6
Cell 14
1. Take user input for the file name
2. Checking if the file exisits in the same folder as that of code file, to check in other folder path needs to be specifieed
3. If file exists read file content and formatted display

## Task 7
Cell 16
1. Take input for discount percentage and converted it to the integer
2. Calcutate discount price for the given data and formatte the data to be written in the file
3. Written data to the file using writelines() which can write list to the file
4. Read the file after writing
5. Iterate over the data for calcutations and formatted data display
