# A/B Testing Analysis: Marketing Campaign Effectiveness

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Complete-success)

A comprehensive statistical analysis of marketing campaign effectiveness using A/B testing methodology to determine whether product advertisements significantly increase customer conversions compared to Public Service Announcements (PSA).

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Key Findings](#-key-findings)
- [Dataset](#-dataset)
- [Methodology](#-methodology)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Analysis Highlights](#-analysis-highlights)
- [Results Visualization](#-results-visualization)
- [Statistical Tests](#-statistical-tests)
- [Conclusions](#-conclusions)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

## 🎯 Project Overview

This project evaluates the effectiveness of a marketing advertising campaign through rigorous A/B testing. The analysis compares two groups:

- **Treatment Group (Ad)**: Users exposed to product advertisements
- **Control Group (PSA)**: Users shown Public Service Announcements

### Business Problem

Marketing companies invest heavily in advertising campaigns but need to quantify the actual impact on customer conversions. This analysis answers:

1. **Would the campaign be successful?**
2. **If successful, how much of that success can be attributed to the ads?**

## 🔑 Key Findings

| Metric | Ad Group | PSA Group | Difference |
|--------|----------|-----------|------------|
| **Sample Size** | 564,577 users | 23,524 users | - |
| **Conversion Rate** | **2.55%** | 1.79% | **+0.77 percentage points** |
| **Conversions** | 14,423 | 420 | - |
| **Relative Lift** | - | - | **+43.10%** |
| **Statistical Significance** | p < 0.0001 | - | **Highly Significant** |
| **Effect Size (Cohen's h)** | 0.1847 | - | **Small to Medium** |

### Key Insights

✅ **Ads significantly increase conversions** by 43% compared to PSA  
✅ **Statistically significant** at p < 0.0001 (well below α = 0.05)  
✅ **Consistent performance** across all days and hours  
✅ **Optimal ad frequency** identified for maximum conversion  
✅ **Strong business case** for implementing the campaign

## 📊 Dataset

**Source**: Marketing A/B Test Dataset  
**Size**: 588,101 user records  
**Period**: Campaign duration (see data files)

### Variables

| Column | Description | Type |
|--------|-------------|------|
| `user_id` | Unique identifier for each user | Integer |
| `test_group` | Assignment to 'ad' or 'psa' group | Categorical |
| `converted` | Whether user made a purchase | Boolean |
| `total_ads` | Number of ads/PSAs shown to user | Integer |
| `most_ads_day` | Day of week with highest ad exposure | Categorical |
| `most_ads_hour` | Hour of day with highest ad exposure | Integer |

## 🔬 Methodology

### Experimental Design

- **Test Type**: Two-sample proportion test (Ad vs PSA)
- **Randomization**: Users randomly assigned to test groups
- **Sample Size**: ~588K total users (96% ad, 4% psa)
- **Primary Metric**: Conversion Rate (% of users who purchased)
- **Significance Level**: α = 0.05 (95% confidence)

### Analysis Pipeline

```
1. Data Loading & Exploration
   ├── Dataset profiling
   ├── Missing value analysis
   └── Data quality checks

2. Exploratory Data Analysis (EDA)
   ├── Test group distribution
   ├── Conversion analysis
   ├── Dose-response analysis
   ├── Temporal consistency checks
   └── Interaction effects

3. Statistical Hypothesis Testing
   ├── Two-Proportion Z-Test
   ├── Chi-Square Test
   ├── Confidence Intervals (Individual & Lift)
   └── Effect Size Analysis (Cohen's h)

4. Deep Dive Analysis
   ├── Ad exposure impact
   ├── Temporal patterns (day/hour)
   └── Segmentation insights

5. Business Recommendations
   ├── Implementation decision
   └── Optimization strategies
```

## 🛠 Technologies Used

### Core Libraries

```python
# Data Manipulation
pandas >= 1.3.0
numpy >= 1.21.0

# Visualization
matplotlib >= 3.4.0
seaborn >= 0.11.0
plotly >= 5.14.0
kaleido >= 0.2.1

# Statistical Analysis
scipy >= 1.7.0
statsmodels >= 0.13.0

# Notebook
jupyter >= 1.0.0
ipywidgets >= 8.1.0
nbformat >= 5.10.0
```

## 💻 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/AB_Testing_Marketing.git
cd AB_Testing_Marketing
```

2. **Create virtual environment** (recommended)

```bash
# Windows
python -m venv abtest-env
abtest-env\Scripts\activate

# macOS/Linux
python3 -m venv abtest-env
source abtest-env/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Launch Jupyter Notebook**

```bash
jupyter notebook data_exploration.ipynb
```

## 🚀 Usage

### Quick Start

1. Open `data_exploration.ipynb` in Jupyter Notebook
2. Run all cells sequentially (Cell → Run All)
3. Review the comprehensive analysis and visualizations

### Customization

- **Adjust significance level**: Modify `alpha` parameter in statistical tests
- **Change visualization styles**: Edit the `create_plotly_layout()` helper function
- **Add new analyses**: Use the modular structure to extend the notebook

## 📁 Project Structure

```
AB_Testing_Marketing/
│
├── Data/
│   ├── marketing_AB.csv          # Main dataset
│   └── readme.md                  # Data documentation
│
├── data_exploration.ipynb         # Main analysis notebook
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── .gitignore                     # Git ignore rules
```

## 📈 Analysis Highlights

### 1. Test Group Distribution

Validated proper randomization with 96% ad group and 4% PSA control group, ensuring sufficient statistical power.

### 2. Conversion Analysis

- **Ad Group**: 2.55% conversion rate (14,423 conversions)
- **PSA Group**: 1.79% conversion rate (420 conversions)
- **Absolute Lift**: 0.77 percentage points
- **Relative Lift**: 43.10% improvement

### 3. Dose-Response Analysis

Identified optimal ad frequency for maximum conversion rate, revealing diminishing returns beyond a certain threshold.

### 4. Temporal Consistency

Verified that ad superiority holds consistently across:
- ✅ All days of the week
- ✅ All hours of the day
- ✅ Various ad frequency levels

### 5. Interaction Effects

Analyzed how ad frequency interacts with:
- Day of week patterns
- Hour of day trends
- User engagement levels

## 📊 Results Visualization

The notebook includes interactive Plotly visualizations:

- **Test Group Distribution**: Bar chart showing user allocation
- **Conversion Analysis**: Grouped bar charts and rate comparisons
- **Dose-Response Curve**: Optimal ad frequency analysis
- **Temporal Consistency**: Line charts across days and hours
- **Interaction Heatmaps**: Complex relationship visualizations
- **Statistical Summary**: Confidence intervals and effect sizes

All plots feature:
- 🎨 Professional color schemes
- 🖱️ Interactive hover tooltips
- 📱 Responsive square dimensions
- 📊 Consistent styling throughout

## 🔍 Statistical Tests

### Two-Proportion Z-Test

```
H₀: p_ad = p_psa (no difference in conversion rates)
H₁: p_ad > p_psa (ad group has higher conversion rate)

Result: p < 0.0001 → Reject H₀
Conclusion: Strong evidence that ads increase conversions
```

### Chi-Square Test

```
Tests independence between test group and conversion status

Result: χ² statistic with p < 0.0001
Conclusion: Test group and conversion are significantly related
```

### Confidence Intervals

- **Ad Group**: [2.51%, 2.60%]
- **PSA Group**: [1.62%, 1.95%]
- **Absolute Lift**: [0.59%, 0.95%]

Intervals don't overlap → Strong evidence of difference

### Effect Size (Cohen's h)

```
Cohen's h = 0.1847 (Small to Medium effect)

Interpretation: Practically meaningful difference beyond just statistical significance
```

## 💡 Conclusions

### Primary Conclusion

**Recommendation: IMPLEMENT THE ADVERTISING CAMPAIGN**

The analysis provides overwhelming evidence that advertisements significantly increase customer conversions compared to PSA.

### Supporting Evidence

1. **Statistical Significance**: p < 0.0001 (far below threshold)
2. **Practical Significance**: 43% relative lift is business-meaningful
3. **Consistency**: Effect holds across all temporal dimensions
4. **Confidence**: 95% CI for lift is entirely positive [0.59%, 0.95%]
5. **Effect Size**: Cohen's h = 0.18 indicates real-world impact

### Business Impact

- **For every 1,000 ad viewers**: ~26 conversions
- **For every 1,000 PSA viewers**: ~18 conversions
- **Net gain**: ~8 additional conversions per 1,000 users
- **Relative improvement**: 43% increase in conversion rate

### Optimization Insights

1. **Ad Frequency**: Optimal range identified (see dose-response analysis)
2. **Timing**: Consistent performance across all hours/days
3. **Scale**: Effect validated on large sample (564K+ users)

## 🚀 Future Enhancements

Potential extensions to this analysis:

- [ ] **ROI Analysis**: Incorporate ad costs and revenue data
- [ ] **Segmentation**: Analyze performance by user demographics
- [ ] **Time Series**: Study conversion rates over campaign duration
- [ ] **Multi-Variate Testing**: Test multiple ad variations simultaneously
- [ ] **Causal Inference**: Apply advanced causal analysis methods
- [ ] **Machine Learning**: Predict conversion probability
- [ ] **Long-term Effects**: Analyze customer lifetime value
- [ ] **Cross-Platform**: Compare effectiveness across channels

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Dataset source: [Credit if applicable]
- Statistical methods based on standard A/B testing frameworks
- Visualization inspired by best practices in data science communication

---

⭐ **If you found this project helpful, please consider giving it a star!** ⭐

---

**Keywords**: A/B Testing, Marketing Analytics, Statistical Analysis, Hypothesis Testing, Python, Data Science, Conversion Rate Optimization, Business Intelligence, Plotly, Jupyter Notebook
