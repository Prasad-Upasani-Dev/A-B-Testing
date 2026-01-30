"""
Statistical Tests Page
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

from helpers import apply_custom_css, load_data, calculate_metrics

st.set_page_config(page_title="Statistical Tests", page_icon="🔬", layout="wide")
st.markdown(apply_custom_css(), unsafe_allow_html=True)

st.title("Statistical Hypothesis Testing")

# Load data and calculate metrics
data = load_data()
m = calculate_metrics(data)

# Test summary
st.header("Test Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">P-Value</div>
        <div class="metric-value">{m['p_value']:.6f}</div>
        <div class="metric-label">{'SIGNIFICANT' if m['p_value'] < 0.05 else 'NOT SIGNIFICANT'}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Effect Size (Cohen's h)</div>
        <div class="metric-value">{m['cohens_h']:.4f}</div>
        <div class="metric-label">SMALL-MEDIUM</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Relative Lift</div>
        <div class="metric-value">{m['lift']:.1f}%</div>
        <div class="metric-label">IMPROVEMENT</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Test 1: Two-Proportion Z-Test
st.header("1. Two-Proportion Z-Test")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"""
    **Hypotheses:**
    - H₀: p_ad = p_psa
    - H₁: p_ad > p_psa
    
    **Test Statistic:** z = {m['z_stat']:.4f}  
    **P-Value:** {m['p_value']:.6f}  
    **Significance Level:** α = 0.05
    
    **Decision:** {'Reject H₀' if m['p_value'] < 0.05 else 'Fail to reject H₀'}
    """)

with col2:
    if m['p_value'] < 0.05:
        st.markdown("""
        <div class="success-box">
        <strong>Result:</strong><br>
        Strong evidence that ads increase conversion rate.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="warning-box">
        <strong>Result:</strong><br>
        Insufficient evidence of difference.
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Test 2: Confidence Intervals
st.header("2. Confidence Intervals (95%)")

# Create visualization
fig_ci = go.Figure()

groups = ['AD', 'PSA']
rates = [m['ad_rate'] * 100, m['psa_rate'] * 100]
ci_lower = [m['ad_ci'][0] * 100, m['psa_ci'][0] * 100]
ci_upper = [m['ad_ci'][1] * 100, m['psa_ci'][1] * 100]

for i, group in enumerate(groups):
    fig_ci.add_trace(go.Scatter(
        x=[rates[i]],
        y=[group],
        mode='markers',
        marker=dict(size=15, color=['#667eea', '#f093fb'][i]),
        name=group,
        showlegend=False,
        hovertemplate=f'<b>{group}</b><br>Rate: {rates[i]:.2f}%<extra></extra>'
    ))
    
    fig_ci.add_trace(go.Scatter(
        x=[ci_lower[i], ci_upper[i]],
        y=[group, group],
        mode='lines',
        line=dict(color=['#667eea', '#f093fb'][i], width=4),
        showlegend=False,
        hovertemplate=f'95% CI: [{ci_lower[i]:.2f}%, {ci_upper[i]:.2f}%]<extra></extra>'
    ))

fig_ci.update_layout(
    title={'text': 'Conversion Rates with 95% Confidence Intervals', 'x': 0.5, 'xanchor': 'center'},
    xaxis_title='Conversion Rate (%)',
    yaxis_title='Test Group',
    height=350,
    plot_bgcolor='#f8f9fa',
    showlegend=False
)

st.plotly_chart(fig_ci, use_container_width=True)

# CI interpretation
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Ad Group CI", f"[{m['ad_ci'][0]*100:.2f}%, {m['ad_ci'][1]*100:.2f}%]")

with col2:
    st.metric("PSA Group CI", f"[{m['psa_ci'][0]*100:.2f}%, {m['psa_ci'][1]*100:.2f}%]")

with col3:
    st.metric("Absolute Lift CI", f"[{m['lift_ci_lower']*100:.2f}%, {m['lift_ci_upper']*100:.2f}%]")

overlap = not (m['ad_ci'][0] > m['psa_ci'][1])

if not overlap:
    st.markdown("""
    <div class="success-box">
    <strong>Interpretation:</strong> Confidence intervals do not overlap, providing strong evidence that the ad group has a higher conversion rate.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Test 3: Chi-Square Test
st.header("3. Chi-Square Test")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    **Test:** Independence between test group and conversion
    
    **Chi-Square Statistic:** χ² = {m['chi2']:.4f}  
    **P-Value:** {m['chi2_p']:.6f}  
    **Degrees of Freedom:** 1
    
    **Decision:** {'Reject H₀ (variables are related)' if m['chi2_p'] < 0.05 else 'Fail to reject H₀'}
    """)

with col2:
    if m['chi2_p'] < 0.05:
        st.markdown("""
        <div class="success-box">
        <strong>Result:</strong><br>
        Test group and conversion status are significantly related.
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Effect Size
st.header("4. Effect Size Analysis")

st.markdown(f"""
**Cohen's h = {m['cohens_h']:.4f}**

**Interpretation:**
- h < 0.2: Small effect
- 0.2 ≤ h < 0.5: Small to medium effect
- 0.5 ≤ h < 0.8: Medium to large effect
- h ≥ 0.8: Large effect

**Conclusion:** The effect size of {m['cohens_h']:.4f} indicates a **small to medium** but **practically meaningful** difference 
between the ad and PSA groups.
""")

st.markdown("---")
st.info("Next: View the Decision page for final recommendations")
