## Task 3: Product Form (app_product_form.py)
'''
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
'''

import streamlit as st 
products = []

# without using st.form
name = st.sidebar.text_input(label = 'Product Name')
category = st.sidebar.selectbox('Category', ['FnB', 'Bakery', 'Fruits', 'Grocery'])
price = st.sidebar.number_input('Price')
if st.sidebar.button('Add Product'):
    products.append([name, category, str(price)])
    st.success('Product added')

# using st.form
# '''with st.sidebar:
#     with st.form("product_form", clear_on_submit = True):
#         name = st.text_input(label = 'Product Name')
#         category = st.selectbox('Category', ['FnB', 'Bakery', 'Fruits', 'Grocery'])
#         price = st.number_input('Price')
#         submit = st.form_submit_button('Add Product')

#         if submit:
#             products.append([name, category, str(price)])
#             st.success('Product added')'''

products.insert(0, ['Name', 'Category', 'Price'])
st.table(products)