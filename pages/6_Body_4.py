import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Title for the Streamlit app
st.title("4. Transaction Insights")


url = "https://github.com/tphathuin1802/streamlit-python-web-app/blob/main/wall_mart_india.csv"
df = pd.read_csv(url)

purchase_method_counts = df['Purchase Method'].value_counts()
color_sequence = [
    '#003f5c', '#2f4b7c', '#665191', '#a05195',
    '#d45087', '#f95d6a', '#ff7c43', '#ffa600'
]

pull_values = [0.05 if method == "Credit Card" else 0 for method in purchase_method_counts.index]

fig = go.Figure(
    data=[go.Pie(
        labels=purchase_method_counts.index,
        values=purchase_method_counts.values,
        marker=dict(colors=color_sequence),
        pull=pull_values,
    )]
)


fig.update_layout(
    title='Distribution of Purchase Methods with Exploded Credit Card',
    width=800,
    height=600
)

st.plotly_chart(fig)


df['Purchase Date'] = pd.to_datetime(df['Purchase Date'], dayfirst=True)
df['YearMonth'] = df['Purchase Date'].dt.to_period('M')


top_purchase_methods = df['Purchase Method'].value_counts().nlargest(3).index


top_methods_df = df[df['Purchase Method'].isin(top_purchase_methods)]


monthly_top_methods_counts = top_methods_df.groupby(['YearMonth', 'Purchase Method']).size().reset_index(name='Transaction Count')
monthly_top_methods_counts['YearMonth'] = monthly_top_methods_counts['YearMonth'].dt.to_timestamp()

color_map = {
    "Credit Card": "#003f5c",
    "Debit Card": "#bc5090",
    "Net Banking": "#ffa600"
}

fig2 = px.line(
    monthly_top_methods_counts,
    x='YearMonth',
    y='Transaction Count',
    color='Purchase Method',
    title='Monthly Transaction Trends for Top 3 Purchase Methods',
    labels={'YearMonth': 'Date', 'Transaction Count': 'Number of Transactions'},
    color_discrete_map=color_map  # Apply custom colors
)

fig.update_layout(width=1000, height=700)

# Display the plot
st.plotly_chart(fig2)
st.markdown("""
            Credit Cards: Most dominant payment method, accounting for over 40% of transactions, reflecting customer preference for convenience and rewards.

Debit Cards: Second most popular at 25.1%, favored for direct transactions and simplicity.

Net Banking: Used by 9.97%, indicating a preference for secure, bank-mediated online payments.

International Cards: 5.12%, showing demand for global transactions.

Cash on Delivery (CoD): 5.03%, appealing to customers seeking payment assurance.

Digital Wallets & UPI: Combined, account for 14.59%, with PhonePe, Paytm, and Google Pay UPI being equally popular.

->
Credit and Debit Cards dominate, while digital wallets and UPI are gaining ground. Offering diverse payment options is key to meeting customer preferences and enhancing satisfaction.

            """)







agegroup_summary = df.groupby('Age Group').agg(
    total_purchases=('CID', 'count'),
    total_revenue=('Net Amount', 'sum'),
    total_discount=('Discount Amount (INR)', 'sum')
).reset_index()

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=agegroup_summary['Age Group'],
    y=agegroup_summary['total_purchases'],
    mode='lines+markers',
    name='Total Purchases',
    line=dict(color='#bc7f00')
))

# Add the Total Revenue line chart
fig.add_trace(go.Scatter(
    x=agegroup_summary['Age Group'],
    y=agegroup_summary['total_revenue'],
    mode='lines+markers',
    name='Total Revenue (INR)',
    line=dict(color='#008f8c')
))

fig.add_trace(go.Scatter(
    x=agegroup_summary['Age Group'],
    y=agegroup_summary['total_discount'],
    mode='lines+markers',
    name='Total Discount (INR)',
    line=dict(color='maroon')
))

fig.update_layout(
    title='<b>TOTAL PURCHASE, REVENUE AND DISCOUNT BY AGE GROUP</b>',
    xaxis_title='Age Group',
    yaxis_title='Amount',
    xaxis=dict(tickangle=45),
    width=1000,
    height=600,
    legend=dict(x=0.1, y=1.1, orientation='h')
)

st.plotly_chart(fig)
st.markdown("""
            25-45 Age Group: Highest revenue (>60 million INR), making it the most profitable segment.

45-60 Age Group: Revenue of 20 million INR, showing a significant drop in purchasing power.

60+ Age Group: Revenue of 10 million INR, suggesting a decline in e-commerce interest among older customers.

Under 18 Age Group: Lowest revenue (10 million INR), likely due to limited financial independence.

The 25-45 group is the most profitable. Walmart India could focus on tailored marketing and introduce targeted discounts for older and younger age groups to increase sales


            """)


df_filtered = df[df['Age Group'] == '25-45']

color_palette = ['#003f5c', '#2f4b7c', '#665191', '#a05195', '#d45087', '#f95d6a', '#ff7c43', '#ffa600']


fig = go.Figure()

for i, category in enumerate(df_filtered['Product Category'].unique()):
    fig.add_trace(go.Box(
        x=[category] * len(df_filtered[df_filtered['Product Category'] == category]['Discount Amount (INR)']),
        y=df_filtered[df_filtered['Product Category'] == category]['Discount Amount (INR)'],
        name=category,
        marker_color=color_palette[i % len(color_palette)],
        boxmean=True
    ))

fig.update_layout(
    title='<b>DISCOUNT AMOUNTS BY AGE GROUP (25-45) AND PRODUCT CATEGORY',
    xaxis_title='Product Category',
    yaxis_title='Discount Amount (INR)',
    width=1000,
    height=600,
    showlegend=True
)

st.plotly_chart(fig)

st.markdown("""
           Electronics & Clothing: Higher median discounts (~300 INR for Electronics, ~250 INR for Clothing), indicating aggressive discount strategies to attract this age group.

Beauty & Health, Home & Kitchen, Sports & Fitness: Moderate median discounts (~150-200 INR), reflecting a balanced approach.

Books: Lowest median discount (~50 INR), possibly due to lower margin flexibility or different pricing strategies.

            """)