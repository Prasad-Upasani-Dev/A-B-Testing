# A/B Testing Analysis: Marketing Campaign Effectiveness

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Status](https://img.shields.io/badge/Status-Complete-success)

This repository contains an end-to-end A/B test analysis of a marketing campaign. The goal is to measure whether showing **product ads** increases conversion compared to showing a **PSA** (control).

## Key result (headline)

Ads outperform PSA on conversion rate, with a statistically significant difference.

| Metric | Ad | PSA |
|---|---:|---:|
| Users | 564,577 | 23,524 |
| Conversion rate | 2.55% | 1.79% |
| Absolute lift | +0.77 percentage points |  |
| Relative lift | +43.10% |  |
| 95% CI (absolute lift) | [0.59%, 0.95%] |  |
| p-value (two-proportion z-test) | < 0.0001 |  |
| Effect size (Cohen's h) | 0.1847 |  |

## What’s inside

- `data_exploration.ipynb`: main notebook (EDA, visualizations, statistical testing, and conclusions)
- `Data/marketing_AB.csv`: dataset
- `Data/readme.md`: dataset description
- `requirements.txt`: Python dependencies

## How to run

```bash
git clone https://github.com/Prasad-Upasani-Dev/A-B-Testing.git
cd A-B-Testing

python -m venv abtest-env
abtest-env\Scripts\activate

pip install -r requirements.txt
jupyter notebook data_exploration.ipynb
```

## Notebook coverage (high level)

- Group allocation check (Ad vs PSA)
- Conversion counts and conversion rate comparison (interactive Plotly)
- Dose-response analysis (ad frequency vs conversion)
- Temporal consistency (Ad vs PSA by day-of-week and hour-of-day)
- Hypothesis testing:
  - Two-proportion z-test (one-sided: \(p_{ad} > p_{psa}\))
  - Chi-square test
  - Confidence intervals (group rates + absolute lift)
  - Effect size (Cohen's h)

## Author

Prasad Upasani  
GitHub: [Prasad-Upasani-Dev](https://github.com/Prasad-Upasani-Dev)  
LinkedIn: https://www.linkedin.com/in/prasad-upasani/
