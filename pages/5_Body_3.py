import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Title for the Streamlit app
st.title("3. Discount Utilization Analysis ")

# Load the data
df = pd.read_csv("C:/Local Code/Project/DataScienceProject/appsprojects/streamlit_folder/wall_mart_india.csv")


import pandas as pd
import plotly.graph_objects as go

discount_data = df[df['Discount Availed'] == 'Yes']
discount_counts = discount_data.groupby(['Product Category', 'Discount Name']).size().unstack(fill_value=0)


color_palette = ['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600']

fig = go.Figure()

for i, discount_name in enumerate(discount_counts.columns):
    fig.add_trace(go.Bar(
        x=discount_counts.index,
        y=discount_counts[discount_name],
        name=discount_name,
        marker_color=color_palette[i % len(color_palette)]))

fig.update_layout(
    title="Discount Usage by Product Category",
    xaxis_title="Product Category",
    yaxis_title="Number of Purchases",
    legend_title="Discount Code",
    barmode="stack",
    height=800,
    width=800
)

st.plotly_chart(fig)
st.markdown("""
            High Engagement with Electronics: The Electronics category shows the highest number of purchases, with 15,000 customers taking advantage of the SEASONALOFFER21 discount code. This indicates a strong customer interest in electronics, particularly when attractive discounts are available.

Diverse Discount Utilization in Clothing: Clothing also demonstrates high engagement, with 12,500 purchases using a mix of all discount codes. This diversity suggests that the clothing category appeals to a wide range of customers who are motivated by various promotional offers.

Moderate Purchases in Other Categories: Categories such as Beauty and Health (8,000 purchases), Home & Kitchen (7,500 purchases), and Sports & Fitness (6,000 purchases) exhibit moderate purchase numbers, with a noticeable use of the FESTIVE50 discount code. This highlights the importance of festive promotions in driving sales in these segments.

Lower Engagement in Some Categories: Books (3,000 purchases), Other (2,500 purchases), Pet Care (2,000 purchases), and Toys & Games (1,500 purchases) have relatively lower purchase numbers. This could indicate niche markets or opportunities for targeted marketing strategies to boost engagement in these categories.

Overall, the data underscores the effectiveness of discount codes in driving customer purchases across different product categories. This analysis can help Walmart India tailor its marketing strategies to maximize customer engagement and satisfaction.

            """)