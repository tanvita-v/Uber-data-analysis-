
import streamlit as st
import pandas as pd
import numpy as np
import json

st.set_page_config(page_title="Uber Mini Analytics", layout="wide")

@st.cache_data(show_spinner=False)
def load_data():
    df = pd.read_csv("data/uber_trips_50k.csv", parse_dates=["pickup_datetime","dropoff_datetime"])
    return df

@st.cache_data(show_spinner=False)
def load_metrics():
    with open("metrics.json","r") as f:
        return json.load(f)

df = load_data()
metrics = load_metrics()

st.title("🚕 Uber Mini Analytics — Synthetic (50k+)")
st.caption("Synthetic dataset with NYC-style zones for portfolio demonstration")

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Trips", f"{len(df):,}")
col2.metric("Total Revenue", f"${df['fare_amount'].sum():,.0f}")
col3.metric("Avg Fare", f"${df['fare_amount'].mean():.2f}")
idle_base = metrics.get("avg_idle_baseline_min")
idle_after = metrics.get("avg_idle_after_min")
if idle_base and idle_after:
    col4.metric("Avg Idle Time (simulated)", f"{idle_after} min", delta=f"-{round((idle_base-idle_after)/idle_base*100,1)}%")

st.subheader("Key Highlights")
c1, c2, c3 = st.columns(3)
c1.write(f"**Top 15% customers share of rides:** {metrics['top15_customers_share_rides']*100:.1f}%")
c2.write(f"**Top 5 zones share of rides:** {metrics['top5_zones_share_rides']*100:.1f}%")
c3.write(f"**Trips share to reach 45% revenue:** {metrics['trips_share_making_45pct_revenue']*100:.1f}%")

st.divider()

# Filters
with st.expander("Filters"):
    season = st.multiselect("Season", sorted(df["season"].unique()), default=list(sorted(df["season"].unique())))
    zones = st.multiselect("Pickup Zones", sorted(df["pickup_zone"].unique()), default=[])
    hour_range = st.slider("Hour of Day", 0, 23, (0,23))
    
dff = df.copy()
if season:
    dff = dff[dff["season"].isin(season)]
if zones:
    dff = dff[dff["pickup_zone"].isin(zones)]
dff = dff[(dff["pickup_datetime"].dt.hour >= hour_range[0]) & (dff["pickup_datetime"].dt.hour <= hour_range[1])]

st.write(f"Filtered trips: **{len(dff):,}**; Revenue: **${dff['fare_amount'].sum():,.0f}**; Avg Fare: **${dff['fare_amount'].mean():.2f}**")

# Charts
st.subheader("Demand by Hour")
hourly = dff.groupby(dff["pickup_datetime"].dt.hour).size()
st.line_chart(hourly)

st.subheader("Top 10 Pickup Zones")
topzones = dff["pickup_zone"].value_counts().head(10)
st.bar_chart(topzones)

st.subheader("Season vs Hour Heatmap (Counts)")
heat = dff.groupby(["season", dff["pickup_datetime"].dt.hour]).size().unstack(fill_value=0)
st.dataframe(heat)

st.subheader("Revenue Concentration (Cumulative)")
fare_sorted = dff["fare_amount"].sort_values(ascending=False).reset_index(drop=True)
cum_rev = (fare_sorted.cumsum() / fare_sorted.sum()).reset_index().rename(columns={"index":"trip_rank",0:"cum_revenue_share"})
st.line_chart(cum_rev.set_index("trip_rank"))

st.caption("Idle time reduction (-12%) and peak coverage (+25%) are simulated scenario KPIs based on modeled reallocation strategies.")
