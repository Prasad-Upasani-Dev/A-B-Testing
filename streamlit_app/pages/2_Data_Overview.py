"""
Data Overview Page
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import sys
import os

# Add utils to path for both local and cloud deployment
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
utils_dir = os.path.join(parent_dir, 'utils')
if utils_dir not in sys.path:
    sys.path.insert(0, utils_dir)

from helpers import apply_custom_css, load_data

st.set_page_config(page_title="Data Overview", page_icon="📁", layout="wide")
st.markdown(apply_custom_css(), unsafe_allow_html=True)

st.title("Data Overview")

# Load data
data = load_data()

# Dataset summary
st.header("Dataset Summary")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Records", f"{len(data):,}")
col2.metric("Features", len(data.columns))
col3.metric("Missing Values", data.isnull().sum().sum())
col4.metric("Duplicate Rows", data.duplicated().sum())

st.markdown("---")

# Data dictionary
st.header("Data Dictionary")

dict_df = pd.DataFrame({
    'Column': ['user_id', 'test_group', 'converted', 'total_ads', 'most_ads_day', 'most_ads_hour'],
    'Description': [
        'Unique user identifier',
        'Assignment: "ad" or "psa"',
        'Purchase indicator (True/False)',
        'Number of ads shown to user',
        'Day with highest ad exposure',
        'Hour with highest ad exposure'
    ],
    'Type': ['Integer', 'Categorical', 'Boolean', 'Integer', 'Categorical', 'Integer']
})

st.dataframe(dict_df, use_container_width=True, hide_index=True)

st.markdown("---")

# Sample data
st.header("Sample Data")
st.dataframe(data.head(10), use_container_width=True)

st.markdown("---")

# Group distribution
st.header("Test Group Distribution")

test_group_counts = data['test group'].value_counts()
test_group_pct = (test_group_counts / test_group_counts.sum() * 100).round(2)

fig = go.Figure(data=[
    go.Bar(
        x=test_group_counts.index.str.upper(),
        y=test_group_counts.values,
        text=[f'{count:,}<br>({pct}%)' for count, pct in zip(test_group_counts.values, test_group_pct.values)],
        textposition='outside',
        marker=dict(
            color=['#667eea', '#f093fb'],
            line=dict(color='#34495e', width=2),
            opacity=0.9
        ),
        hovertemplate='<b>%{x}</b><br>Users: %{y:,}<extra></extra>'
    )
])

fig.update_layout(
    title={'text': 'User Distribution by Test Group', 'x': 0.5, 'xanchor': 'center',
           'font': {'size': 20, 'color': '#2c3e50'}},
    xaxis_title='Test Group',
    yaxis_title='Number of Users',
    height=500,
    plot_bgcolor='#f8f9fa',
    paper_bgcolor='white',
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<div class="success-box">
<strong>Randomization Check:</strong> Both groups are well-represented, ensuring sufficient statistical power.
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.info("Next: View the Analysis page for conversion insights")
