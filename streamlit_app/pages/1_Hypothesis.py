"""
Hypothesis Form Page
"""
import streamlit as st
import sys
import os

# Add utils to path for both local and cloud deployment
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
utils_dir = os.path.join(parent_dir, 'utils')
if utils_dir not in sys.path:
    sys.path.insert(0, utils_dir)

from helpers import apply_custom_css

st.set_page_config(page_title="Hypothesis", page_icon="🔬", layout="wide")
st.markdown(apply_custom_css(), unsafe_allow_html=True)

st.title("A/B Testing Hypothesis Form")

# 1. The Concept
st.header("1. The Concept")
st.markdown("""
Marketing companies run randomized experiments to determine which version of a campaign drives better results. 
In this test, the majority of users see **ads** (experimental group) while a smaller portion sees a **PSA** (control group) 
in the exact same size and placement.
""")

st.markdown("---")

# 2. Research Question
st.header("2. Research Question")
st.markdown("""
**Do users who see product advertisements convert at a higher rate than users who see PSA?**
""")

st.markdown("---")

# 3. What we want to test
st.header("3. What We Want to A/B Test")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="success-box">
    <strong>Treatment (Ad Group)</strong><br>
    Users exposed to product advertisements
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-box">
    <strong>Control (PSA Group)</strong><br>
    Users shown Public Service Announcements
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# 4. Success Metric
st.header("4. Success Metric")
st.markdown("""
**Primary Metric:** Conversion Rate (percentage of users who made a purchase)

**Unit of Analysis:** Individual user
""")

st.markdown("---")

# 5. Hypotheses
st.header("5. Hypotheses")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Null Hypothesis (H₀)
    The conversion rate for users who saw ads is **equal to** the conversion rate for users who saw PSA.
    
    **H₀: p_ad = p_psa**
    """)

with col2:
    st.markdown("""
    ### Alternative Hypothesis (H₁)
    The conversion rate for users who saw ads is **greater than** the conversion rate for users who saw PSA.
    
    **H₁: p_ad > p_psa**
    """)

st.markdown("---")

# 6. Expected Outcome
st.header("6. Expected Outcome")
st.markdown("""
We expect the ad group to show a **higher conversion rate** than the PSA group, indicating that 
product advertisements effectively drive purchases.

**Success Criteria:**
- Statistical significance: p-value < 0.05
- Meaningful effect size: Cohen's h > 0.2
- Practical business impact: measurable lift in conversion rate
""")

st.markdown("---")

# 7. Sample Size
st.header("7. Sample Size & Test Design")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Users", "588,101")
    
with col2:
    st.metric("Ad Group", "564,577 (96%)")
    
with col3:
    st.metric("PSA Group", "23,524 (4%)")

st.markdown("""
<div class="info-box">
<strong>Statistical Power:</strong> The large sample size ensures we can detect even small differences 
in conversion rates with high confidence.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Navigation hint
st.info("Next: View the Data Overview to explore the dataset")
