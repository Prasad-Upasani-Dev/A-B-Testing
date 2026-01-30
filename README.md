# A/B Testing Analysis: Marketing Campaign Effectiveness

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Status](https://img.shields.io/badge/Status-Complete-success)

End-to-end A/B test analysis to measure whether showing **product ads** increases conversion compared to showing a **PSA** (control).

## A/B Testing Hypothesis Form

### 1) The concept

Marketing teams run randomized experiments to quantify whether ads drive incremental conversions. In this project, most users see **ads** (treatment) while a smaller group sees a **PSA** (control) in the same placement.

### 2) Research question

Do users who see ads convert at a higher rate than users who see PSA?

### 3) What we want to A/B test

- **Treatment**: product advertisement exposure
- **Control**: PSA exposure

### 4) Success metric

- **Primary metric**: conversion rate (percentage of users who purchased)
- **Unit of analysis**: user

### 5) Hypotheses

- **H0 (null)**: \(p_{ad} = p_{psa}\)
- **H1 (one-sided)**: \(p_{ad} > p_{psa}\)

### 6) Expected outcome

We expect the ad group to have a higher conversion rate than the PSA group (positive lift).

### 7) Sample size and duration

This dataset contains ~588k users. The analysis is performed on the provided snapshot (no explicit campaign duration is included in the dataset).

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

Interpretation: ads increase conversions with a statistically significant lift. The notebook also checks whether this advantage is consistent across days/hours and ad frequency.

## Repository contents

- `data_exploration.ipynb`: main notebook (EDA, visualizations, statistical testing, and conclusions)
- `Data/marketing_AB.csv`: dataset
- `Data/readme.md`: dataset description
- `requirements.txt`: Python dependencies

## Quickstart

```bash
git clone https://github.com/Prasad-Upasani-Dev/A-B-Testing.git
cd A-B-Testing

python -m venv abtest-env
abtest-env\Scripts\activate     # Windows
# source abtest-env/bin/activate # macOS/Linux

pip install -r requirements.txt
jupyter notebook data_exploration.ipynb
```

## What you’ll find in the notebook

- Group allocation check (Ad vs PSA)
- Conversion comparison (counts + rates, interactive Plotly)
- Dose-response analysis (ad frequency vs conversion)
- Temporal consistency (Ad vs PSA by day-of-week and hour-of-day)
- Statistical testing:
  - Two-proportion z-test (one-sided)
  - Chi-square test
  - Confidence intervals (group rates + absolute lift)
  - Effect size (Cohen's h)

## Dataset

From `Data/readme.md`:

- `user id`: unique user identifier
- `test group`: `ad` or `psa`
- `converted`: purchase indicator
- `total ads`: number of ads shown to a user
- `most ads day`: day of week with highest exposure
- `most ads hour`: hour of day with highest exposure

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

- Interactive charts: the notebook uses Plotly; run locally in Jupyter for full interactivity.
- Large file: `Data/marketing_AB.csv` is included in the repo, so the first clone may take longer.

## Contributing

If you’d like to extend the analysis or improve the visuals, feel free to open an issue or submit a pull request.

## Author

Prasad Upasani  
GitHub: [Prasad-Upasani-Dev](https://github.com/Prasad-Upasani-Dev)  
LinkedIn: https://www.linkedin.com/in/prasad-upasani/
