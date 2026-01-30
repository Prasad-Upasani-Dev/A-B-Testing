"""
A/B Testing Marketing Analysis - Home Page
"""
import streamlit as st
import sys
sys.path.append('utils')
from helpers import apply_custom_css

# Page configuration
st.set_page_config(
    page_title="A/B Testing Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(apply_custom_css(), unsafe_allow_html=True)

# Header
st.title("A/B Testing Analysis")
st.subheader("Marketing Campaign Effectiveness Study")

# Hero section with quote
st.markdown("""
<div class="quote-box">
"The first principle is that you must not fool yourself, and you are the easiest person to fool."
<br>— Richard Feynman
</div>
""", unsafe_allow_html=True)

# Introduction
st.markdown("---")
st.header("Project Overview")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### The Challenge
    
    Marketing teams invest heavily in advertising campaigns but need to quantify the actual impact on conversions.
    
    **Key Questions:**
    - Would the campaign be successful?
    - How much success is attributable to ads?
    """)

with col2:
    st.markdown("""
    ### The Approach
    
    Randomized controlled experiment comparing two groups:
    - **Ad Group**: Users exposed to product advertisements
    - **Control Group**: Users shown Public Service Announcements
    
    Both groups see content in identical placement and size.
    """)

# Quick metrics preview
st.markdown("---")
st.header("Quick Results Preview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Total Users</div>
        <div class="metric-value">588K</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Ad Conversion</div>
        <div class="metric-value">2.55%</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">PSA Conversion</div>
        <div class="metric-value">1.79%</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Relative Lift</div>
        <div class="metric-value">+43%</div>
    </div>
    """, unsafe_allow_html=True)

# Navigation guide
st.markdown("---")
st.header("Navigation Guide")

st.markdown("""
<div class="info-box">
Use the sidebar to navigate through the analysis:

1. **Hypothesis** - Test design and hypotheses
2. **Data Overview** - Dataset exploration
3. **Analysis** - Interactive visualizations
4. **Statistical Tests** - Hypothesis testing results
5. **Decision** - Final recommendation

Start with the Hypothesis page to understand the test design.
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("A/B Testing Analysis | Prasad Upasani | 2026")
