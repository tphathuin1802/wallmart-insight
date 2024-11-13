import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.title("Customer Demographic Analysis Insight")


url = "https://github.com/tphathuin1802/streamlit-python-web-app/blob/main/wall_mart_india.csv"
df = pd.read_csv(url)


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


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

gender_counts = df["Gender"].value_counts()
color_map = ["#bc5090", "#003f5c", "#ffa600"]

fig = make_subplots(
    rows=1,
    cols=2,
    subplot_titles=("<b>Donut Chart", "<b>Bar Chart"),
    specs=[[{"type": "pie"}, {"type": "bar"}]],
)

fig.add_trace(
    go.Pie(
        labels=gender_counts.index,
        values=gender_counts.values,
        hole=0.3,
        marker=dict(colors=color_map),
        showlegend=True,
    ),
    row=1,
    col=1,
)


fig.add_trace(
    go.Bar(
        x=gender_counts.index,
        y=gender_counts.values,
        marker=dict(color=color_map),
        showlegend=False,
    ),
    row=1,
    col=2,
)

# Customize the layout
fig.update_layout(
    title="<b>GENDER DISTRIBUTION OF PURCHASES</b>",
    height=600,
    width=1000,
    legend_title_text="Gender",
)

st.plotly_chart(fig)

st.markdown(
    """The Gender Distribution of Purchases chart shows that Walmart India's customers are almost evenly split across gender groups, with Female customers making up 33.6%, Male customers 32.9%, and the Other category close behind at 33.5%. This balance in purchasing patterns across gender categories suggests that Walmart India's platform resonates equally well with a broad range of customers, reflecting a truly inclusive appeal

            """
)
st.write(
    "This insight into Walmart India's gender distribution aligns well with the company’s goal of building trust and confidence with all of its customers. By acknowledging and embracing the diversity within its customer base, Walmart India is better positioned to create a positive, inclusive shopping experience that strengthens its brand and builds lasting customer relationships."
)

st.write(
    "Walmart India’s customers are nearly equally split across genders (Female: 33.6%, Male: 32.9%, Other: 33.5%), reflecting inclusivity."
)
