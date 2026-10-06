# Emotional Intelligence Analysis of ChatGPT

Measuring how emotionally intelligent an LLM's responses are by scoring 1,000+ ChatGPT responses across 8 emotional categories with sentiment analysis, then visualizing bias trends by prompt category.

## Overview

Large language models are often described as "empathetic," but that claim is rarely measured. This project builds a repeatable scoring pipeline that:

1. Collects ChatGPT responses to a set of emotionally framed prompts
2. Scores each response with sentiment analysis across 8 emotional categories
3. Aggregates scores by prompt category to surface emotional bias trends
4. Visualizes the results in Matplotlib and Seaborn dashboards

## Key Results

- Scored **1,000+ LLM responses** across **8 emotional categories**
- Built dashboards showing sentiment distribution and emotional bias trends by prompt category
- Surfaced recurring response patterns across prompt categories

<!-- TODO: add 2-3 concrete findings, e.g. "Responses to grief prompts skewed X% more positive than responses to anger prompts" -->

## Emotional Categories

<!-- TODO: list your 8 categories, e.g. joy, sadness, anger, fear, surprise, disgust, trust, anticipation -->

| Category | Description |
|----------|-------------|
| ... | ... |

## Tech Stack

- **Language:** Python
- **Data processing:** Pandas, NumPy
- **Sentiment scoring:** <!-- TODO: e.g. VADER, TextBlob, NRCLex, Hugging Face transformers -->
- **Visualization:** Matplotlib, Seaborn

## Pipeline

```
prompts  ──►  response collection  ──►  cleaning & normalization
                                              │
                                              ▼
dashboards  ◄──  aggregation by category  ◄──  sentiment scoring (8 categories)
```

## Project Structure

<!-- TODO: adjust to match your repo -->

```
.
├── data/
│   ├── prompts.csv            # prompts grouped by category
│   └── responses.csv          # collected LLM responses
├── notebooks/
│   └── analysis.ipynb         # exploration and dashboards
├── src/
│   ├── collect.py             # response collection
│   ├── score.py               # sentiment scoring
│   └── visualize.py           # charts and dashboards
├── outputs/
│   └── figures/               # saved charts
├── requirements.txt
└── README.md
```

## Getting Started

```bash
git clone https://github.com/<your-username>/chatgpt-emotional-intelligence.git
cd chatgpt-emotional-intelligence
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Run the pipeline:

```bash
python src/score.py
python src/visualize.py
```

Or open `notebooks/analysis.ipynb` to step through the analysis.

## Sample Output

<!-- TODO: add 1-2 chart screenshots — recruiters skim images first -->
<!-- ![Sentiment distribution by category](outputs/figures/sentiment_distribution.png) -->

## Limitations & Future Work

- Lexicon/model-based sentiment scoring can miss sarcasm and context
- Extend the comparison to other LLMs on the same prompt set
- Move scoring into a scheduled batch pipeline so new model versions can be benchmarked automatically

## Author

**Sai Manideep Reddy Lakkireddy**
[LinkedIn](https://linkedin.com/in/sai-manideepreddy--/) · saimanideeplakkireddy@gmail.com
