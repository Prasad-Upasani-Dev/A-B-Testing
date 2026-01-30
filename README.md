# A/B Testing Analysis: Marketing Campaign Effectiveness

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red)
![Status](https://img.shields.io/badge/Status-Complete-success)

End-to-end A/B test analysis to measure whether showing **product ads** increases conversion compared to showing a **PSA** (control).

**Live Demo:** https://a-b-testing-marketing.streamlit.app/

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

## Interactive Streamlit App

**Live Demo:** https://a-b-testing-marketing.streamlit.app/

Explore the analysis through an interactive web application with professional visualizations and clean navigation.

**Run the app locally:**

```bash
cd streamlit_app
streamlit run Home.py
```

**App features:**
- **Home**: Project overview with quick metrics
- **Hypothesis**: Complete A/B test hypothesis form
- **Data Overview**: Dataset exploration with interactive charts
- **Analysis**: Conversion, temporal consistency, and dose-response visualizations
- **Statistical Tests**: Z-test, confidence intervals, chi-square, and effect size
- **Decision**: Final recommendation with business impact analysis

All visualizations use Plotly for interactivity with attractive color schemes and minimal text.

## Repository contents

- `data_exploration.ipynb`: main notebook (EDA, visualizations, statistical testing, and conclusions)
- `streamlit_app/`: interactive web application
  - `Home.py`: landing page
  - `pages/`: multi-page app structure
  - `utils/helpers.py`: data loading and calculations
- `Data/marketing_AB.csv`: dataset
- `Data/readme.md`: dataset description
- `requirements.txt`: Python dependencies

## Quickstart

### Option 1: Jupyter Notebook

```bash
git clone https://github.com/Prasad-Upasani-Dev/A-B-Testing.git
cd A-B-Testing

python -m venv abtest-env
abtest-env\Scripts\activate     # Windows
# source abtest-env/bin/activate # macOS/Linux

pip install -r requirements.txt

# Run Jupyter notebook
jupyter notebook data_exploration.ipynb

# OR run Streamlit app
cd streamlit_app
streamlit run Home.py
```

### Option 2: Streamlit Web App (Quick Start)

```bash
git clone https://github.com/Prasad-Upasani-Dev/A-B-Testing.git
cd A-B-Testing

python -m venv abtest-env
abtest-env\Scripts\activate     # Windows
# source abtest-env/bin/activate # macOS/Linux

pip install -r requirements.txt
cd streamlit_app
streamlit run Home.py
```

The app will open automatically in your browser at `http://localhost:8501`

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
├── data_exploration.ipynb       # Main analysis notebook
├── streamlit_app/               # Interactive web app
│   ├── Home.py                  # Landing page
│   ├── pages/
│   │   ├── 1_Hypothesis.py      # Test design & hypotheses
│   │   ├── 2_Data_Overview.py   # Dataset exploration
│   │   ├── 3_Analysis.py        # Interactive visualizations
│   │   ├── 4_Statistical_Tests.py  # Hypothesis testing
│   │   └── 5_Decision.py        # Final recommendations
│   └── utils/
│       └── helpers.py           # Data loading & calculations
├── Data/
│   ├── marketing_AB.csv         # Dataset (588k records)
│   └── readme.md                # Data dictionary
├── requirements.txt             # Python dependencies
├── README.md
└── .gitignore
```

## Notes

- **Jupyter Notebook**: Contains comprehensive analysis with Plotly visualizations. Run locally for full interactivity.
- **Streamlit App**: Professional web interface for exploring the analysis. Best viewed in a browser with the app running locally.
- **Large file**: `Data/marketing_AB.csv` (588k records) is included in the repo, so the first clone may take longer.
- **Python version**: Requires Python 3.8 or higher.

## Contributing

If you’d like to extend the analysis or improve the visuals, feel free to open an issue or submit a pull request.

## Author

Prasad Upasani  
GitHub: [Prasad-Upasani-Dev](https://github.com/Prasad-Upasani-Dev)  
LinkedIn: https://www.linkedin.com/in/prasad-upasani/
