import sys
import streamlit as st
from main import fetch_price
from main import send_mail
from fake_useragent import UserAgent

sys.path.append("C:\\Users\\nihaa\PycharmProjects\PythonProject")

st.title("Flipkart price tracker")
url = st.text_input("Enter the product url")
email = st.text_input("Enter ur email")
target_price = st.number_input("Enter target price",min_value=0.0,step=1.0)
st.text("You will be notified via email if price falls below this price")

ua=UserAgent()
headers = {
    "User-Agent":ua.random
}

if st.button("Track price:"):
    if email and target_price and url:
        with st.spinner("fetching price..."):
            try:
                title,price = fetch_price(url,headers)
                print(f"Product name:{title}")
                print(f"Price:{price}")
                if price <= target_price:
                    send_mail(url,title,email)
                    st.success(f"Price dropped to {price}Rs \n Email has been sent")
                else:
                    st.info(f"Price is {price}Rs. \nStill higher than target price")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in all the fields.")
