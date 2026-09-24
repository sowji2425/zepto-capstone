# zepto-capstone
# Zepto Data & AI Engineering Platform — Capstone Project

This repository contains the unified, three-part platform engineered for the Zepto analytics guild.

## Module Setup and Dependencies
All modules utilize standard Python environment utilities. Install dependencies via:
```bash
pip install -r requirements.txt
```

## How to Execute the Platform

### 1. Run Data Pipeline (/data_pipeline)
Performs web-scraping, applies structural schema normalization formatting constraints, and saves data to a local SQLite database:
```bash
python data_pipeline/scraper.py
python data_pipeline/database.py
python data_pipeline/queries.py
```

### 2. Run Analytics Pipeline (/analytics)
Runs data profiling, transformations, and predictive classification modeling for customer analytics:
```bash
python analytics/model_pipeline.py
```

### 3. Run Grounded Policy Support Engine (/support_assistant)
Executes the RAG engine against internal corporate policy records:
```bash
python support_assistant/rag_engine.py
```

## Summary of Core Design Choices
1. **Data Pipeline:** Selected deliberate value dropping for missing values instead of statistical estimation to maintain strict e-commerce listing record compliance.
2. **Analytics:** Random Forest model structure selected to accurately map mixed classification data matrices without forcing rigid linearity assumptions.
3. **Support RAG:** Engineered an deterministic term mapping engine to reliably test localized contextual grounding without requiring fragile, paid external network connections.
