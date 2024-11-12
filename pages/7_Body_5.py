import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Title for the Streamlit app
st.title("5. Location-Based Sales Analysis")


import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv("C:/Users/phath/Downloads/archive (61)/project1_df.csv")

import pandas as pd
import plotly.graph_objects as go

# Group and sort data
location_sales = df.groupby('Location')['Net Amount'].sum().reset_index()
location_sales = location_sales.sort_values(by='Net Amount', ascending=True)

# Round the Net Amount values to integers
location_sales['Net Amount'] = location_sales['Net Amount'].round(0).astype(int)

# Create figure
fig = go.Figure(data=[
    go.Bar(
        x=location_sales['Net Amount'],
        y=location_sales['Location'],
        orientation='h',
        marker=dict(color='orange'),
        text=location_sales['Net Amount'],  # Add integer values to bars
        textposition='auto'  # Position text automatically
    )
])

# Update layout
fig.update_layout(
    title='<b>Total Sales by Location</b>',
    xaxis_title='Total Sales (Net Amount in INR)',
    yaxis_title='Location',
    autosize=False,
    width=1000,
    height=600
)

# Show figure
st.plotly_chart(fig)
st.markdown("""

Mumbai: Leading the chart with sales exceeding 32 million INR, Mumbai is a major economic hub with high consumer demand and purchasing power.
Delhi: Closely following Mumbai, Delhi also generates substantial sales of over 31 million INR, reflecting its status as a key market.
Bangalore: As a technology hub, Bangalore contributes significantly to overall sales with figures reaching 23.6 million INR.
Mid-Range Performers:

Hyderabad: With sales of 15.8 million INR, Hyderabad represents a growing market with potential for further expansion.
Chennai: Generating 12.6 million INR in sales, Chennai is another mid-range performer with a stable consumer base.
Pune: With sales of 10.9 million INR, Pune showcases steady consumer activity, driven by its industrial and economic development.
Lower-Performing Locations:

Ahmedabad: While generating 8.1 million INR in sales, Ahmedabad presents opportunities for enhanced consumer engagement to boost performance.
Kolkata: With sales of 7.8 million INR, Kolkata also has potential for growth through targeted marketing and sales strategies.
Dehradun, Srinagar, and Varanasi: These locations, with sales below 2 million INR, represent smaller markets or areas with lower consumer engagement. Increased marketing efforts and promotions could help drive growth in these regions.
            """)
