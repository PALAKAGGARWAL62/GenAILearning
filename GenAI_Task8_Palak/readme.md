# Assignment 8: Streamlit (Basic App Building)

This assignment focuses ONLY on:
Creating Streamlit apps
Text input, number input, buttons, selectbox, sidebar
Displaying results using st.write, st.success, st.error, st.table
Simple calculations & visual display
NO advanced topics such as authentication, sessions, API calls, or dataframes (beyond simple lists)
Keep it beginner-friendly.

Folder structure:
streamlit_assignment/
app_basic.py
app_discount.py
app_product_form.py
app_dashboard.py

Code execution
Create virtualenv using
python -m virtualenv venv
Activate virtual environment - get the parent directory of venv
venv\scripts\activate
Install Streamlit
pip install streamlit
Execute file using
streamlit run <filename>.py

## Task 1: Basic Streamlit App (app_basic.py)
Create a basic Streamlit app that:
1. Displays a title: "Welcome to Streamlit!"
2. Shows a text input box for entering your name.
3. When user clicks a button "Greet Me", display:
"Hello, !"
Use:
st.title()
st.text_input()
st.button()
st.write()

## Task 2: Price Calculator (app_discount.py)
Build a simple price calculator app that:
1. Takes product price (number input)
2. Takes discount percentage (slider from 0 to 50%)
3. On button click, calculates discounted price
4. Shows result using st.success()
Example:
Original Price: 1000
Discount: 10%
Final Price: 900
Extra (optional): Show comparison in a small table:
Before | After
(Use st.table() with a simple list of lists.)

## Task 3: Product Form (app_product_form.py)
Create a simple form UI:
1. Use Streamlit sidebar to enter:
o Product Name
o Category (selectbox with 3–5 options)
o Price
2. When user clicks "Add Product", show:
o A success message
o The product details in a clean format
Use components:
st.sidebar.text_input
st.sidebar.selectbox
st.sidebar.number_input
St.sidebar.button

## Task 4: Mini Dashboard (app_dashboard.py)
Create a small dashboard with:
1. Title + Description
"Simple Sales Dashboard"
2. A selectbox with months:
months = ["January", "February", "March", "April"]
3. A static dictionary of monthly sales:
sales = {
"January": 1200,
"February": 1500,
"March": 900,
"April": 2000
}
4. Display selected month’s sales using:
st.metric() OR st.write()
5. Display a bar chart using:
st.bar_chart(list(sales.values()))
(No pandas required — simple list is allowed.)
