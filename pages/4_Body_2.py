import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.title("Product insight")


url = "https://github.com/tphathuin1802/streamlit-python-web-app/blob/main/wall_mart_india.csv"
df = pd.read_csv(url)


import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

gender_category_counts = (
    df.groupby(["Product Category", "Gender"]).size().reset_index(name="Count")
)

color_map = {"Female": "#003f5c", "Male": "#bc5090", "Other": "#ffa600"}

fig = go.Figure()

for gender in gender_category_counts["Gender"].unique():
    gender_data = gender_category_counts[
        gender_category_counts["Gender"] == gender
    ]
    fig.add_trace(
        go.Bar(
            x=gender_data["Product Category"],
            y=gender_data["Count"],
            name=gender,
            marker_color=color_map[gender],
        )
    )


fig.update_layout(
    title="<b>PURCHASE BY GENDER AND PRODUCT CATEGORY",
    xaxis_title="Product Category",
    yaxis_title="Number of Purchases",
    barmode="group",  # Group bars side by side
    legend_title="Gender",
    height=700,
    width=1000,
)

st.plotly_chart(fig)
st.markdown(
    """
            Electronics and Clothing stand out as the top categories, appealing broadly across all genders on Walmart India's platform. Female customers show particular interest in Electronics and have a strong engagement in both Sports & Fitness and Beauty & Health categories, highlighting their diverse shopping preferences. Male customers exhibit high engagement in Clothing, making it the most popular category for this group. Meanwhile, customers identifying as Other demonstrate a high level of interest in Electronics, aligning with the category's broad appeal. This distribution offers valuable insights for Walmart India to tailor marketing efforts toward each gender's specific interests.
            Electronics: Most popular across all genders (Female: 5,200, Male: 5,300, Other: 5,100).
Clothing: Strong interest from Female (3,800) and Male (3,500) customers, with Other at 3,700.
Beauty & Health: Slightly favored by Female (2,800), but balanced across genders (Male: 2,500, Other: 2,600).
Books: Low engagement, around 1,000 purchases across all genders.
Home & Kitchen: Popular with Female (800), moderate interest from Male (600) and Other (700).
Other Categories: Moderate or low engagement, with Female leading in Sports & Fitness.
Electronics and Clothing are the top categories, with insights for targeted, gender-specific marketing. (show only on slide not report)

            """
)


prod_cat_sales = (
    df.groupby("Product Category")["Net Amount"].sum().reset_index()
)

color_palette = [
    "#003f5c",
    "#2f4b7c",
    "#665191",
    "#a05195",
    "#d45087",
    "#f95d6a",
    "#ff7c43",
    "#ffa600",
]

fig = go.Figure()


for i, category in enumerate(prod_cat_sales["Product Category"].unique()):
    fig.add_trace(
        go.Bar(
            x=[category],
            y=[
                prod_cat_sales.loc[
                    prod_cat_sales["Product Category"] == category, "Net Amount"
                ].values[0]
            ],
            marker=dict(color=color_palette[i % len(color_palette)]),
            name=category,
        )
    )


fig.update_layout(
    title="<b>TOTAL SALES BY PRODUCT CATEGORY",
    xaxis_title="Product Category",
    yaxis_title="Total Sales (Net Amount)",
    xaxis=dict(tickangle=45),
    autosize=False,
    width=800,
    height=600,
)

st.plotly_chart(fig)
st.markdown(
    """
            The chart highlights that Electronics and Clothing are the top revenue-generating categories, followed closely by Beauty and Health. Home & Kitchen and Sports & Fitness also contribute significantly but to a lesser extent. Other categories like Books, Pet Care, and Toys & Games have lower sales volumes, indicating they may not be primary interests for Walmart India’s customer base. Walmart India could use these insights to prioritize investment and marketing in high-demand categories while exploring strategies to boost engagement in underperforming areas.

            """
)


df["Purchase Date"] = pd.to_datetime(df["Purchase Date"], dayfirst=True)


monthly_sales = (
    df.groupby(df["Purchase Date"].dt.month)["Net Amount"].sum().reset_index()
)
monthly_sales = monthly_sales.rename(columns={"Purchase Date": "Month"})

monthly_sales = monthly_sales.sort_values(by="Month", ascending=True)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=monthly_sales["Month"],
        y=monthly_sales["Net Amount"],
        mode="lines+markers",
        name="Net Purchase Amount",
        line=dict(color="orange"),
        marker=dict(
            color="darkblue",
            size=10,
            symbol="circle",
            line=dict(color="MediumPurple", width=2),
        ),
    )
)

fig.update_layout(
    title="<b>MONTHLY SALES",
    xaxis_title="Months",
    yaxis_title="Net Purchase Amount",
    xaxis=dict(tickmode="linear"),
    width=1000,
    height=600,
)

# Show the plot
st.plotly_chart(fig)
st.markdown(
    """
            Seasonal Fluctuations: Sales start at around 12 million in January but dip to the lowest point of 10 million in February. After that, there is a gradual recovery in March and April, with sales stabilizing between 13 million to 14 million from April to September.
Mid-Year Drop: A noticeable decline occurs in June, where sales drop to nearly 11 million, making it one of the lower-performing months of the year. This could indicate a seasonal slowdown in purchases during the middle of the year.
Year-End Surge: Starting in October, there is a steady and significant increase in sales each month, culminating in the highest sales of the year in December at around 18 million. This sharp rise towards the end of the year likely reflects increased consumer spending due to holiday seasons and end-of-year promotions.
The chart highlights a cyclical sales pattern, with a low point in February, steady sales through mid-year, and a strong surge in the final quarter. This pattern could be valuable for Walmart India in planning seasonal promotions, inventory management, and marketing strategies to maximize sales during peak months like December.

            """
)


df["Purchase Date"] = pd.to_datetime(df["Purchase Date"])

color_hex = ["#665191", "#d45087", "#a05195", "#ff7c43", "#ffa600"]

df["Year-Month"] = df["Purchase Date"].dt.to_period("M")
df_grouped = (
    df.groupby(["Year-Month", "Product Category"])["Net Amount"]
    .sum()
    .reset_index()
)

df_grouped["Rank"] = df_grouped.groupby("Year-Month")["Net Amount"].rank(
    method="first", ascending=False
)

df_top5 = df_grouped[df_grouped["Rank"] <= 5]

category_colors = dict(zip(df_top5["Product Category"].unique(), color_hex))

fig = px.bar(
    df_top5,
    x="Net Amount",
    y="Product Category",
    color="Product Category",
    animation_frame="Year-Month",
    animation_group="Product Category",
    title="<b>TOP 5 PRODUCT CATEGORIES BY NET SALES OVER TIME</b>",
    labels={
        "Net Amount": "Net Sales (INR)",
        "Product Category": "Product Category",
    },
    orientation="h",
    text="Net Amount",
    text_auto=True,
    color_discrete_map=category_colors,
)

fig.update_layout(
    xaxis_title="Net Sales (INR)",
    yaxis_title="Product Category",
    xaxis=dict(range=[0, df_top5["Net Amount"].max() * 1.1]),
    yaxis={"categoryorder": "total ascending"},
    showlegend=True,
    title_x=0.5,
    title_y=0.95,
    width=1005,
    height=900,
)
st.plotly_chart(fig)
st.markdown(
    """
            Electronics: Dominates with 441,456 INR in net sales, showing strong demand.

Clothing: Follows with 338,878 INR, indicating high customer spending.

Beauty & Health: Generates 275,580 INR, reflecting substantial interest in personal care.

Home & Kitchen: Net sales of 178,522 INR, showing moderate demand.

Sports & Fitness: Generates 165,710 INR, representing significant interest but lower sales.

Solution:

Focus on Electronics and Clothing for stock and promotional strategies, while also considering growth opportunities in Beauty & Health, Home & Kitchen, and Sports & Fitness.

            """
)
