# Uber data Analytics — Python, Streamlit, Power BI (Synthetic 50k+)

This project analyzes **55,000+ synthetic Uber trips** (NYC-style zones) to demonstrate demand patterns, customer concentration, and operational insights. It includes a **Streamlit dashboard**, reproducible **Python analysis**, and exportable **visuals** for your portfolio.

## Highlights (matches resume bullets)

- **Analyzed 50,000+ Uber trip records** using Python to identify demand trends and **top 15% customer segments** generating **~81.7%** of rides.
- **Built dashboards** revealing **5 high-demand zones** covering **~46.3%** of rides, enabling smarter driver allocation and improving peak-hour coverage.
- **Segmented rides by time and season**, revealing demand surges and **key trips generating 45% of revenue** (see cumulative revenue curve; top **~15.8%** of trips).
- **Recommended operational changes and optimized workflows**, modeling a **12% reduction in driver idle time** and **25% boost in peak-hour coverage** via reallocation strategies (simulated scenario).

> ⚠️ Note: Data is **synthetic** but realistic; zone names are NYC-style for better storytelling.

## Repository Structure

```
data/
  uber_trips_50k.csv
visuals/
  pareto_customers.png
  top5_zones.png
  season_hour_heatmap.png
  zones_bubble_map.png
  cumulative_revenue_curve.png
app.py
metrics.json
```

## Getting Started

### 1) Environment
```bash
pip install -r requirements.txt
# Minimal set:
# pandas, numpy, matplotlib, streamlit
```

### 2) Run Streamlit App
```bash
streamlit run app.py
```

### 3) Explore the Data
```python
import pandas as pd
df = pd.read_csv("data/uber_trips_50k.csv", parse_dates=["pickup_datetime","dropoff_datetime"])
df.head()
```

## Visuals

Below are sample outputs saved in `visuals/` (add to your README screenshots):

- **Customer Pareto Curve**: `visuals/pareto_customers.png`  
- **Top 5 Pickup Zones**: `visuals/top5_zones.png`  
- **Season-Hour Heatmap**: `visuals/season_hour_heatmap.png`  
- **Zones Bubble Map**: `visuals/zones_bubble_map.png`  
- **Cumulative Revenue Curve**: `visuals/cumulative_revenue_curve.png`  

## Reproducibility

- Random seed is fixed for data generation in the script that produced `uber_trips_50k.csv`.
- Metrics saved to `metrics.json` are referenced by the Streamlit app and README.

## Notes

- The idle time reduction and peak coverage improvement are **scenario simulations** based on modeled reallocations during peak hours. They demonstrate how analytics can inform operations.
- Replace the synthetic dataset with a real public dataset later to strengthen the project (e.g., TLC trip data).

---

**Author**: tanvita-v  
**License**: MIT
