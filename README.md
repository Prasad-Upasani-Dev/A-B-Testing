# A/B Testing Analysis: Marketing Campaign Effectiveness

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Status](https://img.shields.io/badge/Status-Complete-success)

End-to-end A/B test analysis to measure whether showing **product ads** increases conversion compared to showing a **PSA** (control).

## Problem

Marketing teams run A/B tests to answer:

- Would the campaign be successful?
- If successful, how much of the success is attributable to ads (vs. PSA)?

## Headline result

| Metric | Ad | PSA |
|---|---:|---:|
| Users | 564,577 | 23,524 |
| Conversion rate | 2.55% | 1.79% |
| Absolute lift | +0.77 percentage points |  |
| Relative lift | +43.10% |  |
| 95% CI (absolute lift) | [0.59%, 0.95%] |  |
| p-value (two-proportion z-test) | < 0.0001 |  |
| Effect size (Cohen's h) | 0.1847 |  |

Interpretation: ads increase conversions with a statistically significant and practically meaningful lift, and the notebook further checks whether this advantage is consistent across days/hours and ad frequency.

## Contents

- `data_exploration.ipynb`: main notebook (EDA, visualizations, statistical testing, and conclusions)
- `Data/marketing_AB.csv`: dataset
- `Data/readme.md`: dataset description
- `requirements.txt`: Python dependencies

## Reproduce locally

```bash
git clone https://github.com/Prasad-Upasani-Dev/A-B-Testing.git
cd A-B-Testing

python -m venv abtest-env
abtest-env\Scripts\activate     # Windows
# source abtest-env/bin/activate # macOS/Linux

pip install -r requirements.txt
jupyter notebook data_exploration.ipynb
```

## What the notebook covers

- Group allocation check (Ad vs PSA)
- Conversion comparison (counts + rates, interactive Plotly)
- Dose-response analysis (ad frequency vs conversion)
- Temporal consistency (Ad vs PSA by day-of-week and hour-of-day)
- Hypothesis testing:
  - Two-proportion z-test (one-sided: H1: p_ad > p_psa)
  - Chi-square test
  - Confidence intervals (group rates + absolute lift)
  - Effect size (Cohen's h)

## Repo structure

```
A-B-Testing/
├── data_exploration.ipynb
├── requirements.txt
├── README.md
├── .gitignore
└── Data/
    ├── marketing_AB.csv
    └── readme.md
```

## Notes

- **Interactive charts**: the notebook uses Plotly; run it locally in Jupyter for full interactivity.
- **Large file**: `Data/marketing_AB.csv` is included in the repo, so the first clone may take a bit longer.

## Author

Prasad Upasani  
GitHub: [Prasad-Upasani-Dev](https://github.com/Prasad-Upasani-Dev)  
LinkedIn: https://www.linkedin.com/in/prasad-upasani/
