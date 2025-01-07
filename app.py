import sys
import streamlit as st
from main import fetch_price
from main import send_mail

sys.path.append("C:\\Users\\nihaa\PycharmProjects\PythonProject")

st.title("Flipkart price tracker")
url = st.text_input("Enter the product url")
email = st.text_input("Enter ur email")
target_price = st.number_input("Enter target price",min_value=0.0,step=1.0)
st.text("You will be notified via email if price falls below this price")

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
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
                    st.success(f"Price dropped to {price}Rs\nEmail has been sent")
                else:
                    st.info(f"Price is {price}Rs. \nStill higher than target price")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in all the fields.")
