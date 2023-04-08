# F'String(Python Feature) Vs Normal String

a = 10
b = 11
c = 12
print(f"Hello, The value of a,b,c is {a} {b} {c}")
print("Hello, The value of a,b,c is",a,b,c)

# Unsplash URL API

import requests as re

query = input("Write Something : ")
url = f"https://unsplash.com/nautocomplete/{query}?xp=search-quality-boosting%3Acontrol"

get_request = re.get(url)
data = get_request.json()

print(data)

# Unsplash Search Streamlit Project

import requests as re
import streamlit as st

query=st.text_input("Enter something:")
if (st.button("search")):

    url =f"https://unsplash.com/napi/search?query={query}"
    r = re.get(url)
    da=r.json()
    print(da)

    url_list = []
    name_array = []

    for item in da['photos']['results']:
        name = item['user']['name']
        name_array.append(name)
        url = item['urls']['full']
        url_list.append(url)

    print(name_array)
    print(url_list)
    
    # Display image in a column
    for i in range(len(url_list)):
        st.image(url_list[i],caption=name_array[i])
    
    # # Display image in a row
    # for i in range (len(url_list)):
    #     col1, col2, col3 = st.columns(3)
    #     with col1:
    #         st.image(url_list[i],caption=name_array[i])
    #     with col2:
    #         st.image(url_list[i+1],caption=name_array[i+1])
    #     with col3:
    #         st.image(url_list[i+2],caption=name_array[i+2])





