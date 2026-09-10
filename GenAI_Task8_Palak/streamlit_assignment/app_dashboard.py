## Task 4: Mini Dashboard (app_dashboard.py)
'''
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
'''

import streamlit as st 
# Title
st.title("Simple Sales Dashboard")
st.text('This is sales dashboard of first quater')

# month selection
months = ["January", "February", "March", "April"]
selected_month = st.selectbox('Select Month to check sales', months, index=None)

sales = {
"January": 1200,
"February": 1500,
"March": 900,
"April": 2000
}

if selected_month is not None:
    st.metric('Sales of %s'%selected_month, sales.get(selected_month, 'January'))

show_chart = st.button('Show Bar Chart')
if show_chart:
    st.bar_chart(list(sales.values()), x_label='Monthly Sales', y_label='Sales Amount')
    