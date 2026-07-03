import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="🛍️",
    layout="wide"

)


# ---------------------------------------------------
# Load Data
# ---------------------------------------------------

df = pd.read_csv("outputs/customer_segments.csv")

kmeans = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# ---------------------------------------------------
# Segment Names
# ---------------------------------------------------

cluster_map = {
    0: "Balanced Mainstream Customers",
    1: "Premium High-Value Customers",
    2: "Budget Enthusiastic Spenders",
    3: "High Income Low Engagement Customers",
    4: "Low Value Conservative Customers"
}

recommendation_map = {
    0: "Maintain engagement through seasonal offers and reward programs.",
    1: "Offer premium memberships, luxury products, and exclusive discounts.",
    2: "Provide flash sales and attractive combo offers.",
    3: "Increase engagement with personalized marketing campaigns.",
    4: "Target with budget-friendly products and cashback offers."
}

# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.title("🛍️ Customer Segmentation Dashboard")
st.write(
    "Analyze customer behavior using **K-Means Clustering** and predict customer segments."
)

st.markdown("---")

# ---------------------------------------------------
# KPI Cards
# ---------------------------------------------------

col1, col2, col3 = st.columns(3)

col1.metric("👥 Customers", len(df))
col2.metric("📊 Clusters", 5)
col3.metric("📈 Features Used", 2)

st.markdown("---")

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.header("Customer Details")

income = st.sidebar.slider(
    "Annual Income (k$)",
    10,
    140,
    60
)

score = st.sidebar.slider(
    "Spending Score",
    1,
    100,
    50
)

# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

sample = pd.DataFrame({
    "Annual_Income":[income],
    "Spending_Score":[score]
})

sample_scaled = scaler.transform(sample)

cluster = kmeans.predict(sample_scaled)[0]

segment = cluster_map[cluster]

recommendation = recommendation_map[cluster]

# ---------------------------------------------------
# Prediction Result
# ---------------------------------------------------

st.subheader("🎯 Predicted Customer Segment")

st.success(segment)

st.info("💡 Business Recommendation")

st.write(recommendation)

st.markdown("---")

# ---------------------------------------------------
# Interactive Cluster Plot
# ---------------------------------------------------

fig = px.scatter(
    df,
    x="Annual_Income",
    y="Spending_Score",
    color="Cluster",
    hover_data=["Age","CustomerID"],
    title="Customer Segments"
)

centers = scaler.inverse_transform(
    kmeans.cluster_centers_
)

fig.add_trace(

    go.Scatter(

        x=centers[:,0],
        y=centers[:,1],

        mode="markers",

        marker=dict(
            size=20,
            symbol="x",
            color="black"
        ),

        name="Centroids"

    )

)

fig.add_trace(

    go.Scatter(

        x=[income],
        y=[score],

        mode="markers",

        marker=dict(
            size=18,
            color="red"
        ),

        name="Your Customer"

    )

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------------------------
# Cluster Statistics
# ---------------------------------------------------

st.subheader("📊 Cluster Statistics")

cluster_summary = (

    df.groupby("Cluster")

    .agg({

        "Age":"mean",

        "Annual_Income":"mean",

        "Spending_Score":"mean",

        "CustomerID":"count"

    })

    .rename(columns={"CustomerID":"Customers"})

    .round(2)

)

st.dataframe(cluster_summary,use_container_width=True)

st.markdown("---")

# ---------------------------------------------------
# Pie Chart
# ---------------------------------------------------

st.subheader("🥧 Customer Distribution")

pie = px.pie(

    df,

    names="Cluster",

    title="Customers per Cluster"

)

st.plotly_chart(
    pie,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------------------------
# Dataset Preview
# ---------------------------------------------------

st.subheader("📋 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.markdown("---")

# ---------------------------------------------------
# Download Button
# ---------------------------------------------------

csv = df.to_csv(index=False)

st.download_button(

    label="⬇ Download Segmented Dataset",

    data=csv,

    file_name="\customer_segments.csv",

    mime="text/csv"

)

st.markdown("---")

st.caption(
    "Developed by Dhruv Bihani | Machine Learning Project using K-Means Clustering"
)