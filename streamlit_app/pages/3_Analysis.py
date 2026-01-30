"""
Analysis Page - Interactive Visualizations
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import sys
import os

# Add utils to path for both local and cloud deployment
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
utils_dir = os.path.join(parent_dir, 'utils')
if utils_dir not in sys.path:
    sys.path.insert(0, utils_dir)

from helpers import apply_custom_css, load_data, calculate_metrics

st.set_page_config(page_title="Analysis", page_icon="📊", layout="wide")
st.markdown(apply_custom_css(), unsafe_allow_html=True)

st.title("Exploratory Data Analysis")

# Load data and metrics
data = load_data()
metrics = calculate_metrics(data)

# Section 1: Conversion Analysis
st.header("1. Conversion Analysis")

col1, col2 = st.columns(2)

with col1:
    # Conversion counts
    conversion_data = data.groupby(['test group', 'converted']).size().reset_index(name='count')
    not_conv = conversion_data[conversion_data['converted'] == False].set_index('test group')['count']
    conv = conversion_data[conversion_data['converted'] == True].set_index('test group')['count']
    
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        name='Not Converted', 
        x=not_conv.index.str.upper(), 
        y=not_conv.values,
        marker=dict(color='#ff6b6b', line=dict(color='#c92a2a', width=2)),
        text=[f'{v:,}' for v in not_conv.values],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Not Converted: %{y:,}<extra></extra>'
    ))
    
    fig1.add_trace(go.Bar(
        name='Converted',
        x=conv.index.str.upper(),
        y=conv.values,
        marker=dict(color='#51cf66', line=dict(color='#2f9e44', width=2)),
        text=[f'{v:,}' for v in conv.values],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Converted: %{y:,}<extra></extra>'
    ))
    
    fig1.update_layout(
        title={'text': 'User Conversion by Test Group', 'x': 0.5, 'xanchor': 'center'},
        xaxis_title='Test Group',
        yaxis_title='Number of Users',
        barmode='group',
        height=450,
        plot_bgcolor='#f8f9fa',
        showlegend=True
    )
    
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    # Conversion rates
    conv_rates = data.groupby('test group')['converted'].mean() * 100
    diff = abs(conv_rates.iloc[0] - conv_rates.iloc[1])
    
    fig2 = go.Figure(data=[go.Bar(
        x=conv_rates.index.str.upper(),
        y=conv_rates.values,
        marker=dict(color=['#4facfe', '#00f2fe'], line=dict(color='#0077b6', width=2)),
        text=[f'{v:.2f}%' for v in conv_rates.values],
        textposition='outside',
        hovertemplate='<b>%{x}</b><br>Rate: %{y:.2f}%<extra></extra>'
    )])
    
    fig2.add_annotation(
        x=0.5, y=max(conv_rates.values) * 0.5,
        xref='paper', yref='y',
        text=f'Difference: {diff:.2f}%',
        showarrow=False,
        font=dict(size=14, color='#2c3e50'),
        bgcolor='#ffd93d',
        bordercolor='#f59f00',
        borderwidth=2,
        borderpad=10
    )
    
    fig2.update_layout(
        title={'text': 'Conversion Rate Comparison', 'x': 0.5, 'xanchor': 'center'},
        xaxis_title='Test Group',
        yaxis_title='Conversion Rate (%)',
        height=450,
        plot_bgcolor='#f8f9fa',
        showlegend=False
    )
    
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# Section 2: Temporal Consistency
st.header("2. Temporal Consistency")

st.markdown("Checking if ad advantage holds across all days and hours:")

col1, col2 = st.columns(2)

with col1:
    # By day
    day_conv = data.groupby(['test group', 'most ads day'])['converted'].mean() * 100
    day_conv_pivot = day_conv.unstack(level=0)
    
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=day_conv_pivot.index,
        y=day_conv_pivot['ad'],
        mode='lines+markers',
        name='Ad Group',
        line=dict(color='#667eea', width=3),
        marker=dict(size=10, symbol='circle'),
        hovertemplate='<b>%{x}</b><br>Ad: %{y:.2f}%<extra></extra>'
    ))
    fig3.add_trace(go.Scatter(
        x=day_conv_pivot.index,
        y=day_conv_pivot['psa'],
        mode='lines+markers',
        name='PSA Group',
        line=dict(color='#f093fb', width=3, dash='dash'),
        marker=dict(size=10, symbol='diamond'),
        hovertemplate='<b>%{x}</b><br>PSA: %{y:.2f}%<extra></extra>'
    ))
    
    fig3.update_layout(
        title={'text': 'Conversion Rate by Day of Week', 'x': 0.5, 'xanchor': 'center'},
        xaxis_title='Day',
        yaxis_title='Conversion Rate (%)',
        height=450,
        plot_bgcolor='#f8f9fa'
    )
    
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    # By hour
    hour_conv = data.groupby(['test group', 'most ads hour'])['converted'].mean() * 100
    hour_conv_pivot = hour_conv.unstack(level=0)
    
    fig4 = go.Figure()
    fig4.add_trace(go.Scatter(
        x=hour_conv_pivot.index,
        y=hour_conv_pivot['ad'],
        mode='lines+markers',
        name='Ad Group',
        line=dict(color='#4facfe', width=3),
        marker=dict(size=8),
        hovertemplate='<b>Hour %{x}</b><br>Ad: %{y:.2f}%<extra></extra>'
    ))
    fig4.add_trace(go.Scatter(
        x=hour_conv_pivot.index,
        y=hour_conv_pivot['psa'],
        mode='lines+markers',
        name='PSA Group',
        line=dict(color='#00f2fe', width=3, dash='dash'),
        marker=dict(size=8, symbol='diamond'),
        hovertemplate='<b>Hour %{x}</b><br>PSA: %{y:.2f}%<extra></extra>'
    ))
    
    fig4.update_layout(
        title={'text': 'Conversion Rate by Hour of Day', 'x': 0.5, 'xanchor': 'center'},
        xaxis_title='Hour',
        yaxis_title='Conversion Rate (%)',
        height=450,
        plot_bgcolor='#f8f9fa'
    )
    
    st.plotly_chart(fig4, use_container_width=True)

days_ad_higher = (day_conv_pivot['ad'] > day_conv_pivot['psa']).sum()
hours_ad_higher = (hour_conv_pivot['ad'] > hour_conv_pivot['psa']).sum()

st.markdown(f"""
<div class="success-box">
<strong>Consistency Check:</strong><br>
Ad conversion rate is higher on {days_ad_higher}/{len(day_conv_pivot)} days 
and in {hours_ad_higher}/{len(hour_conv_pivot)} hours.<br>
The ad advantage is <strong>consistent across temporal dimensions</strong>.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Section 3: Dose-Response
st.header("3. Dose-Response Analysis")

st.markdown("Exploring the relationship between ad frequency and conversion rate:")

# Prepare dose-response data
ad_data = data[data['test group'] == 'ad'].copy()
bins = [0, 25, 50, 100, 150, 200, 250, 300, 400, 2500]
labels = ['1-25', '26-50', '51-100', '101-150', '151-200', '201-250', '251-300', '301-400', '400+']
ad_data['ad_bin'] = pd.cut(ad_data['total ads'], bins=bins, labels=labels)

dose_response = ad_data.groupby('ad_bin').agg({
    'converted': ['sum', 'count', 'mean']
}).round(4)
dose_response.columns = ['Conversions', 'Total_Users', 'Conversion_Rate']
dose_response['Conversion_Rate_Pct'] = dose_response['Conversion_Rate'] * 100

dose_response_filtered = dose_response[dose_response['Total_Users'] >= 100]

fig5 = go.Figure()
fig5.add_trace(go.Scatter(
    x=dose_response_filtered.index.astype(str),
    y=dose_response_filtered['Conversion_Rate_Pct'],
    mode='lines+markers',
    line=dict(color='#667eea', width=4),
    marker=dict(size=12, color='#764ba2', line=dict(color='white', width=2)),
    fill='tozeroy',
    fillcolor='rgba(102, 126, 234, 0.2)',
    hovertemplate='<b>%{x} ads</b><br>Conversion: %{y:.2f}%<extra></extra>'
))

fig5.update_layout(
    title={'text': 'Ad Frequency vs Conversion Rate', 'x': 0.5, 'xanchor': 'center'},
    xaxis_title='Number of Ads Shown',
    yaxis_title='Conversion Rate (%)',
    height=450,
    plot_bgcolor='#f8f9fa'
)

st.plotly_chart(fig5, use_container_width=True)

optimal_bin = dose_response_filtered['Conversion_Rate_Pct'].idxmax()
optimal_rate = dose_response_filtered['Conversion_Rate_Pct'].max()

st.markdown(f"""
<div class="info-box">
<strong>Optimal Frequency:</strong> The {optimal_bin} ads range shows the highest conversion rate ({optimal_rate:.2f}%).
This suggests diminishing returns beyond a certain ad exposure threshold.
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.info("Next: View Statistical Tests for hypothesis validation")
