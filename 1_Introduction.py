import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Group 4: Datavisualization Presentation",
    page_icon="👋",
)

st.title("Group 4: Datavisualization Presentation")
st.sidebar.success("Select a page above.")
st.header("1. Reason of choosing that topics")
st.markdown(
    """ In the era of Industry 4.0, e-commerce has grown rapidly, completely changing the way of shopping and traditional business models. Businesses of all sizes are taking advantage of digital platforms to reach customers more quickly and effectively. Sales in e-commerce have become fiercely competitive, requiring sellers to be creative, flexible and use optimal tools to attract and retain customers. Through this overview, we will better understand the role of technology and data in increasing business efficiency and creating competitive advantages.

Walmart is the world's leading retail brand, known for its "Always Low Prices" strategy that helps attract customers and maintain a competitive advantage. Heavy investment in technology has helped Walmart optimize its supply chain and enhance the user experience, affirming the role of technology in modern retail. Walmart also has a large economic and social impact in the markets in which it operates. Notably, in India, Walmart acquired e-commerce company Flipkart in 2018, expanding its influence and strongly participating in this potential e-commerce market. However, Walmart also faces policy challenges and competition from big rivals like Amazon, requiring flexible strategies to maintain its position.

Hence, this is the reason why our group choose this topic.
"""
)
st.header("2. Overview about dataset")
url = "https://raw.githubusercontent.com/tphathuin1802/streamlit-python-web-app/refs/heads/main/wall_mart_india.csv"
df = pd.read_csv(url)

st.dataframe(df)
st.write("This dataset contains 14 field of data")
st.write("Detail:")
st.write("CID (Customer ID): A unique identifier for each customer.")
st.write("TID (Transaction ID): A unique identifier for each transaction.")
st.write("Gender: The gender of the customer, categorized as Male or Female.")
st.write("Age Group: Age group of the customer, divided into several ranges.")
st.write("Purchase Date: The timestamp of when the transaction took place.")
st.write(
    "Product Category: The category of the product purchased, such as Electronics, Apparel, etc."
)
st.write(
    "Discount Availed: Indicates whether the customer availed any discount (Yes/No)."
)
st.write("Discount Name: Name of the discount applied (e.g., FESTIVE50).")

st.write(
    "Discount Amount (INR): The amount of discount availed by the customer."
)
st.write("Gross Amount: The total amount before applying any discount.")
st.write("Net Amount: The final amount after applying the discount.")
st.write(
    "Purchase Method: The payment method used (e.g., Credit Card, Debit Card, etc"
)
st.write("Location: The city where the purchase took place.")
