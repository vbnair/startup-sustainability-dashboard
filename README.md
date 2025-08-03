

# **Sustainable Business Models Dashboard for Indian Internet Startups**(version1.0)

An **interactive analytics dashboard** analyzing the **sustainability of business models** among **20 curated Indian internet‑based startups** across **EdTech, FinTech, E‑commerce, and SaaS sectors**.

The solution integrates **financial metrics, ESG disclosures, and real‑time media sentiment analysis** to provide **data‑driven insights** into startup growth and sustainability.

---

## **Key Features**

* **Multi‑Dimensional Startup Analysis**

  * Valuation, funding, and multi‑year revenues (FY21–FY23).
  * Profitability, size categorization, and IPO‑listing status.
  * ESG (Environmental, Social, Governance) disclosure indicators.
* **Automated Media Sentiment Analysis**

  * Fetches recent news headlines using [NewsAPI](https://newsapi.org).
  * Runs NLP sentiment scoring using Hugging Face transformers.
  * Provides sentiment distribution across sectors and interpretation.
* **Interactive Visualizations**

  * Funding vs Revenue scatter with valuations.
  * Sector‑wise profitability, ESG adoption, and revenue growth trends.
  * Sentiment distribution pie charts and sector‑wise sentiment bar charts.
* **Data Transparency & Sources**

  * Collapsible source notes for each startup.
  * Data dictionary explaining each field for easy interpretation.

---

## **How It Works**

1. **Data Input**

   * Input file: `startup_dataset_curated.csv`
   * Fields:

     * `Startup`: Name of the company (Indian HQ).
     * `Sector`: EdTech / FinTech / E‑commerce / SaaS.
     * `Year Founded`, `Valuation (USD B)`, `Funding (USD B)`.
     * `Revenue FY21–FY23 (INR Cr)`: Multi‑year revenue data.
     * `Profitability`: Profitable / Loss‑making / Near Breakeven.
     * `ESG Disclosed`: Yes / No.
     * `IPO‑Listed`: Yes / No.
     * `Source Notes`: Data source references (IPO filings, credible reports).

2. **Processing**

   * Filters for complete data records.
   * Calls **NewsAPI** to fetch the latest news headline for each startup.
   * Runs **Hugging Face Sentiment Analysis** on the headline (Positive / Negative / Neutral).
   * Generates sector‑level summaries, key insights, and interpretations.

3. **Output**

   * **Interactive HTML Dashboard**: `interactive_dashboard_curated.html`.
   * **Processed Dataset with Sentiment**: `cleaned_dataset_with_sentiment.csv`.
   * **Sector Summary File**: `sector_summary.csv`.

---


## **Interpreting the Dashboard**

* **Executive Summary**: Snapshot of key findings across sectors.
* **Funding vs Revenue Scatter**: Reveals correlations between funding raised and revenue generated (bubble size = valuation).
* **Business Model & Profitability**: Highlights which sectors are most sustainable.
* **ESG & Sentiment Insights**: Provides a layer of **non‑financial sustainability indicators**, including **media sentiment**.
* **Collapsible Sources**: Ensures every figure can be traced back to its origin.
* **Data Dictionary**: Embedded for clear understanding of all metrics.

---

## **Tech Stack**

* **Python** (Pandas, Plotly, Requests).
* **Hugging Face Transformers**: Sentiment analysis (`distilbert-base-uncased-finetuned-sst-2-english`).
* **NewsAPI**: Fetches real‑time headlines for startups.
* **Google Colab**: Collaborative and cloud‑based execution.

---

## **Best Practices Applied**

* **Error Handling**: Graceful fallback when NewsAPI fails (e.g., invalid key or rate limits).
* **Data Transparency**: Source notes for each startup and an embedded **data dictionary**.
* **Interpretability**: Narrative insights, highlighting key metrics in **bold** for emphasis.
* **Modularity**: Clearly separated steps for data ingestion, processing, sentiment analysis, and visualization.
* **Academic Rigor**: Multi‑year analysis with cross‑validated data points (financial + non‑financial).

---

## **Potential Use Cases**

* **Startup Analysis**: Benchmarking business model sustainability in Indian markets.
* **Investor Insights**: Identifying sectors with strong sentiment and financial growth.
* **Academic Research**: Integrating ESG and sentiment into startup growth models.
* **Business Consulting**: Quick diagnostic tool for evaluating startup health.

---

## **Author**

Developed by **Vaisakh**.
For feedback or collaboration opportunities, please reach out [vaisakhbk.online](https://www.vaisakhbk.online/).

-------------------------------------------------------------------------------

## Folder Structure 
```
startup-sustainability-dashboard/
│
├── datasets/
│ ├── startup_dataset_curated.csv # Input: curated startup dataset
│ ├── cleaned_dataset_with_sentiment.csv # Output: enriched dataset with sentiment
│ └── sector_summary.csv # Output: sector-level aggregated data
│
├── outputs/
│ └── interactive_dashboard_curated.html # Interactive HTML dashboard
│
├── modules/ # Modular Python components
│ ├── data_processing.py # Data loading & preparation
│ ├── sentiment_analysis.py # NewsAPI integration & sentiment scoring
│ ├── visualization.py # Plotly-based charts & dashboard
│ └── report_builder.py # HTML assembly with narrative sections
│
├── notebooks/
│ └── sustainableStartUps_Analysis.ipynb # Optional Colab/Jupyter exploratory version
│
├── analysis.py # Main pipeline script
├── .env # Environment variables (NewsAPI key)
├── requirements.txt # Python dependencies
└── README.md
```
## 📸 Dashboard Preview

![Dashboard Preview](assets/interactive_dashboard_curated%20-html.png)
