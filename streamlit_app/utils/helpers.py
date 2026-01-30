"""
Helper functions for Streamlit app
"""
import pandas as pd
import numpy as np
import os
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, proportion_confint

# Cache data loading for performance
def load_data():
    """Load and cache the marketing data"""
    # Get the path relative to this file (works locally and on cloud)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    streamlit_app_dir = os.path.dirname(current_dir)
    project_root = os.path.dirname(streamlit_app_dir)
    data_path = os.path.join(project_root, 'Data', 'marketing_AB.csv')
    return pd.read_csv(data_path, index_col=0)

def calculate_metrics(data):
    """Calculate all key metrics for the analysis"""
    # Group-level metrics
    ad_data = data[data['test group'] == 'ad']
    psa_data = data[data['test group'] == 'psa']
    
    ad_conversions = ad_data['converted'].sum()
    ad_total = len(ad_data)
    ad_rate = ad_data['converted'].mean()
    
    psa_conversions = psa_data['converted'].sum()
    psa_total = len(psa_data)
    psa_rate = psa_data['converted'].mean()
    
    # Lift calculations
    abs_diff = ad_rate - psa_rate
    lift = (abs_diff / psa_rate) * 100
    
    # Statistical tests
    count = np.array([ad_conversions, psa_conversions])
    nobs = np.array([ad_total, psa_total])
    z_stat, p_value = proportions_ztest(count, nobs, alternative='larger')
    
    # Confidence intervals
    ad_ci = proportion_confint(ad_conversions, ad_total, alpha=0.05, method='normal')
    psa_ci = proportion_confint(psa_conversions, psa_total, alpha=0.05, method='normal')
    
    # CI for lift
    se_diff = np.sqrt((ad_rate * (1 - ad_rate) / ad_total) + 
                      (psa_rate * (1 - psa_rate) / psa_total))
    lift_ci_lower = abs_diff - (1.96 * se_diff)
    lift_ci_upper = abs_diff + (1.96 * se_diff)
    
    # Effect size (Cohen's h)
    cohens_h = 2 * (np.arcsin(np.sqrt(ad_rate)) - np.arcsin(np.sqrt(psa_rate)))
    
    # Chi-square test
    contingency = pd.crosstab(data['test group'], data['converted'])
    chi2, chi2_p, dof, expected = stats.chi2_contingency(contingency)
    
    return {
        'ad_conversions': ad_conversions,
        'ad_total': ad_total,
        'ad_rate': ad_rate,
        'psa_conversions': psa_conversions,
        'psa_total': psa_total,
        'psa_rate': psa_rate,
        'abs_diff': abs_diff,
        'lift': lift,
        'z_stat': z_stat,
        'p_value': p_value,
        'ad_ci': ad_ci,
        'psa_ci': psa_ci,
        'lift_ci_lower': lift_ci_lower,
        'lift_ci_upper': lift_ci_upper,
        'cohens_h': cohens_h,
        'chi2': chi2,
        'chi2_p': chi2_p
    }

def apply_custom_css():
    """Apply custom CSS for attractive styling"""
    return """
    <style>
    /* Main container */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Headers */
    h1 {
        color: #2c3e50;
        font-weight: 600;
    }
    
    h2 {
        color: #34495e;
        font-weight: 500;
        border-bottom: 2px solid #667eea;
        padding-bottom: 10px;
    }
    
    h3 {
        color: #4a5568;
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    
    .metric-value {
        font-size: 2.5em;
        font-weight: 700;
        margin: 10px 0;
    }
    
    .metric-label {
        font-size: 0.9em;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Quote box */
    .quote-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 30px;
        border-radius: 15px;
        font-size: 1.2em;
        font-style: italic;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }
    
    /* Info boxes */
    .info-box {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
    }
    
    .success-box {
        background-color: #e8f5e9;
        border-left: 4px solid #4caf50;
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
    }
    
    .warning-box {
        background-color: #fff3e0;
        border-left: 4px solid #ff9800;
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #2c3e50;
    }
    
    /* Tables */
    table {
        width: 100%;
    }
    
    th {
        background-color: #667eea;
        color: white;
        padding: 12px;
        text-align: left;
    }
    
    td {
        padding: 10px;
        border-bottom: 1px solid #ddd;
    }
    
    tr:hover {
        background-color: #f5f5f5;
    }
    </style>
    """
