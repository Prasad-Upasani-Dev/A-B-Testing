# A/B Testing Analysis: Marketing Campaign Effectiveness

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Status](https://img.shields.io/badge/Status-Complete-success)

A comprehensive statistical analysis of marketing campaign effectiveness using A/B testing to determine whether product advertisements significantly increase customer conversions compared to Public Service Announcements (PSA).

## Table of Contents

- [Overview](#overview)
- [Key Results](#key-results)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Analysis Structure](#analysis-structure)
- [Statistical Tests](#statistical-tests)
- [Conclusions](#conclusions)

## Overview

This project evaluates the effectiveness of a marketing advertising campaign through A/B testing. The analysis compares two groups:

- **Treatment Group (Ad)**: Users exposed to product advertisements
- **Control Group (PSA)**: Users shown Public Service Announcements

### Business Objective

Quantify the actual impact of advertising on customer conversions to answer:
1. Would the campaign be successful?
2. How much of that success can be attributed to the ads?

## Key Results

| Metric | Ad Group | PSA Group | Difference |
|--------|----------|-----------|------------|
| Sample Size | 564,577 users | 23,524 users | - |
| Conversion Rate | 2.55% | 1.79% | +0.77 pp |
| Conversions | 14,423 | 420 | - |
| Relative Lift | - | - | +43.10% |
| P-Value | < 0.0001 | - | Highly Significant |
| Effect Size (Cohen's h) | 0.1847 | - | Small-Medium |

### Primary Findings

- Advertisements significantly increase conversions by 43% compared to PSA
- Statistically significant at p < 0.0001 (well below alpha = 0.05)
- Effect is consistent across all days and hours
- 95% Confidence Interval for lift: [0.59%, 0.95%]
- Strong business case for campaign implementation

## Dataset

**Size**: 588,101 user records  
**Format**: CSV

### Variables

| Column | Description | Type |
|--------|-------------|------|
| user_id | Unique user identifier | Integer |
| test_group | Assignment to 'ad' or 'psa' | Categorical |
| converted | Purchase indicator | Boolean |
| total_ads | Number of ads shown | Integer |
| most_ads_day | Peak exposure day | Categorical |
| most_ads_hour | Peak exposure hour | Integer |

## Methodology

### Experimental Design

- **Test Type**: Two-sample proportion test
- **Randomization**: Random assignment to test groups
- **Sample Size**: ~588K total users
- **Primary Metric**: Conversion rate
- **Significance Level**: alpha = 0.05

### Analysis Pipeline

1. **Data Exploration**
   - Data profiling and quality checks
   - Test group distribution analysis
   - Conversion rate analysis

2. **Statistical Testing**
   - Two-Proportion Z-Test
   - Chi-Square Test
   - Confidence Intervals (individual and lift)
   - Effect Size Analysis (Cohen's h)

3. **Advanced Analysis**
   - Dose-response analysis
   - Temporal consistency checks
   - Interaction effects
   - Segmentation insights

4. **Business Recommendations**
   - Implementation decision
   - Optimization strategies

## Installation

### Prerequisites

- Python 3.8+
- pip package manager

### Setup

```bash
# Clone repository
git clone https://github.com/Prasad-Upasani-Dev/A-B-Testing.git
cd A-B-Testing

# Create virtual environment (recommended)
python -m venv abtest-env
abtest-env\Scripts\activate  # Windows
# source abtest-env/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook data_exploration.ipynb
```

## Usage

1. Open `data_exploration.ipynb` in Jupyter Notebook
2. Run all cells sequentially (Cell → Run All)
3. Review analysis and visualizations

## Technologies

**Core Libraries:**
- pandas, numpy - Data manipulation
- matplotlib, seaborn - Static visualization
- plotly - Interactive visualization
- scipy, statsmodels - Statistical analysis
- jupyter - Notebook environment

**Full requirements**: See `requirements.txt`

## Analysis Structure

```
data_exploration.ipynb
├── Part 1: Data Loading & Exploration
├── Part 2: Exploratory Data Analysis
│   ├── Test group distribution
│   ├── Conversion analysis
│   ├── Dose-response analysis
│   └── Temporal consistency
├── Part 3: Statistical Hypothesis Testing
│   ├── Two-Proportion Z-Test
│   ├── Chi-Square Test
│   ├── Confidence Intervals
│   └── Effect Size Analysis
├── Part 4: Results Visualization
├── Part 5: Deep Dive Analysis
└── Part 6: Conclusions & Recommendations
```

## Statistical Tests

### Hypothesis

**Null Hypothesis (H₀)**: p_ad = p_psa  
**Alternative Hypothesis (H₁)**: p_ad > p_psa

### Results

**Two-Proportion Z-Test**
- Result: p < 0.0001
- Conclusion: Reject H₀, ads significantly increase conversions

**Chi-Square Test**
- Result: p < 0.0001
- Conclusion: Test group and conversion are significantly related

**Confidence Intervals (95%)**
- Ad Group: [2.51%, 2.60%]
- PSA Group: [1.62%, 1.95%]
- Absolute Lift: [0.59%, 0.95%]
- Intervals do not overlap, confirming significant difference

**Effect Size**
- Cohen's h = 0.1847 (Small to Medium)
- Indicates practically meaningful difference

## Conclusions

### Recommendation

**Implement the advertising campaign.**

The analysis provides strong evidence that advertisements significantly increase customer conversions compared to PSA.

### Supporting Evidence

1. **Statistical Significance**: p < 0.0001
2. **Practical Significance**: 43% relative lift
3. **Consistency**: Effect holds across all temporal dimensions
4. **Confidence**: 95% CI for lift is entirely positive
5. **Effect Size**: Cohen's h indicates real-world impact

### Business Impact

- Per 1,000 ad viewers: ~26 conversions
- Per 1,000 PSA viewers: ~18 conversions
- Net gain: ~8 additional conversions per 1,000 users
- Relative improvement: 43% increase in conversion rate

## Project Structure

```
AB_Testing_Marketing/
├── Data/
│   ├── marketing_AB.csv
│   └── readme.md
├── data_exploration.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

## Author

**Prasad Upasani**

- GitHub: [@Prasad-Upasani-Dev](https://github.com/Prasad-Upasani-Dev)
- LinkedIn: [Connect on LinkedIn](https://linkedin.com/in/yourprofile)

---

**Keywords**: A/B Testing, Marketing Analytics, Statistical Analysis, Hypothesis Testing, Python, Data Science, Conversion Rate Optimization, Business Intelligence
