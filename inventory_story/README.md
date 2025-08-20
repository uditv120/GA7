# Retail Inventory Turnover: 2024 Data Story

Author contact: 22f3002257@ds.study.iitm.ac.in

This repository contains a small, self-contained analysis that demonstrates how Large Language Models (LLMs) can accelerate data storytelling from data-to-insight. It includes code, visuals, and a concise narrative aimed at executive stakeholders.

Key facts:
- Inventory Turnover Ratio (2024 quarterly): Q1 3.67, Q2 5.65, Q3 2.80, Q4 10.60
- Average for 2024: 5.68 (vs. industry target 8)
- Challenge: Excess inventory and storage costs driven by sub-target turnover in Q1–Q3, with a rebound in Q4

Core recommendation: optimize supply chain and demand forecasting.

Files:
- `data/inventory_turnover_2024.csv` — Source data
- `analyze_inventory.py` — Python analysis that computes metrics and generates charts
- `outputs/turnover_trend.png`, `outputs/turnover_bars.png` — Visualizations

How to run:
1) Create and activate a Python 3.10+ environment
2) Install deps: `pip install -r requirements.txt`
3) Run: `python analyze_inventory.py`

What the analysis shows:
- Trend: Turnover is weak in Q1 (3.67) and Q3 (2.80), modest in Q2 (5.65), then spikes in Q4 (10.60). The average (5.68) sits well below the industry target (8), leaving a gap of ~2.32.
- Variability: A high spread indicates inconsistency in supply-demand alignment. Q4’s spike suggests the target is attainable with the right levers.
- Business implications: Prolonged sub-target turnover drives carrying costs (storage, capital tied up, obsolescence risk) and reduces agility in responding to demand shifts.

Recommended actions (prioritized):
1) Forecasting excellence — optimize supply chain and demand forecasting
   - Deploy hierarchical demand forecasting (SKU x region x channel) and ML-driven seasonality/price effects.
   - Improve new product forecasting with early signal capture (preorders, search, marketing).
   - Institute monthly Forecast Accuracy reviews (MAPE, bias) with accountability.
2) Inventory policy tuning
   - Recalculate safety stock with service-level targets and lead-time variability.
   - ABC/XYZ segmentation to tailor reorder points and review cadences.
   - Rationalize long-tail SKUs; apply make-to-order or vendor-managed inventory for slow movers.
3) Supply-side agility
   - Shorten and diversify lead times through nearshoring/dual-sourcing.
   - Introduce smaller, more frequent replenishment cycles where feasible.
   - Vendor scorecards tied to fill rate, OTIF, and responsiveness.
4) Commercial levers
   - Targeted markdowns, bundles, and promotions on excess stock informed by elasticity.
   - Dynamic assortment and lifecycle pricing to preempt overstock.

Evidence of LLM assistance:
- This project plan, code scaffolding, and narrative were drafted with an LLM and iterated via prompts (GitHub Copilot-style assistance).

Next steps to create a Pull Request:
1) Initialize a new Git repo in this folder, commit files, and push to GitHub.
2) Open a PR titled "Retail Inventory Turnover Analysis (LLM-assisted)" including this README, code, and charts.
3) Ensure the PR description references LLM assistance and includes the contact email above for verification.


added new outputs for pr
