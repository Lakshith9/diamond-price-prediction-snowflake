import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Diamond Price Prediction",
    page_icon="💎",
    layout="wide"
)

st.title("💎 Diamond Price Prediction")
st.write("Machine Learning Regression Project using Snowflake")

# Connect to Snowflake
conn = st.connection("snowflake")
session = conn.session()

# Load diamond dataset
df = session.sql("""
    SELECT *
    FROM DIAMOND_PRICE_ML.ML_WORKFLOW.DIAMONDS_RAW
""").to_pandas()

# Dataset Overview
st.subheader("Dataset Overview")

c1, c2, c3 = st.columns(3)

c1.metric("Total Diamonds", f"{len(df):,}")
c2.metric("Average Price", f"${df['PRICE'].mean():,.2f}")
c3.metric("Maximum Price", f"${df['PRICE'].max():,.2f}")

# Model Performance
st.subheader("Model Performance")

metrics = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Random Forest Regressor"
    ],
    "MAE": [
        735.41,
        276.79
    ],
    "RMSE": [
        1131.67,
        560.30
    ],
    "R2": [
        0.9195,
        0.9803
    ]
})

st.dataframe(metrics, use_container_width=True)

st.success(
    "Best Model: Random Forest Regressor | "
    "Test R²: 0.9803 | RMSE: 560.30 | MAE: 276.79"
)

# Diamond Price Explorer
st.subheader("Diamond Price Explorer")

col1, col2, col3 = st.columns(3)

with col1:
    carat = st.slider(
        "Carat",
        float(df["CARAT"].min()),
        float(df["CARAT"].max()),
        1.0,
        0.01
    )

with col2:
    cut = st.selectbox(
        "Cut",
        sorted(df["CUT"].dropna().unique())
    )

with col3:
    clarity = st.selectbox(
        "Clarity",
        sorted(df["CLARITY"].dropna().unique())
    )

# Find similar diamonds
similar = df[
    (df["CARAT"].between(carat - 0.05, carat + 0.05)) &
    (df["CUT"] == cut) &
    (df["CLARITY"] == clarity)
]

if len(similar) > 0:
    estimated_price = similar["PRICE"].median()

    st.metric(
        "Estimated Diamond Price",
        f"${estimated_price:,.2f}"
    )

    st.caption(
        f"Based on {len(similar):,} similar diamonds."
    )
else:
    st.warning("No similar diamonds found.")

# Sample Data
st.subheader("Sample Diamond Data")
st.dataframe(df.head(20), use_container_width=True)
