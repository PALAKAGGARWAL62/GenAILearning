## Task 2: Price Calculator (app_discount.py)
'''
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
'''

import streamlit as st 
price = st.number_input("Enter the Product Price")
discount = st.slider('Discount Percentage', min_value=0, max_value=50)
dp = price
if st.button('Calculate Discounted Price'):
    dp = price * (1-0.01*discount)
    st.success(dp)
st.write("Original Price: %d"%price)
st.write("Discount: %d"%discount)
st.write("Final Price: %d"%dp)
data = [['Original Price', 'Final Price'],[price, dp]]
st.table(data)