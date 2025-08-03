import os
from dotenv import load_dotenv
from modules.data_processing import load_and_prepare_data, generate_sector_summary
from modules.sentiment_analysis import run_sentiment_analysis
from modules.visualization import generate_dashboard
from modules.report_builder import build_html_report

# === Setup ===
load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
if not NEWS_API_KEY:
    raise ValueError("NewsAPI key missing in .env")

DATASET_PATH = "datasets/startup_dataset_curated.csv"
OUTPUT_CLEANED = "datasets/cleaned_dataset_with_sentiment.csv"
OUTPUT_SECTOR = "datasets/sector_summary.csv"
OUTPUT_HTML = "outputs/interactive_dashboard_curated.html"

# === Load & Process Data ===
df_complete, incomplete_count = load_and_prepare_data(DATASET_PATH)

# === Sentiment Analysis ===
df_complete = run_sentiment_analysis(df_complete, NEWS_API_KEY)
df_complete.to_csv(OUTPUT_CLEANED, index=False)

# === Sector Summary ===
generate_sector_summary(df_complete, OUTPUT_SECTOR)

# === Dashboard & Report ===
fig_dashboard = generate_dashboard(df_complete)
insights_html = "<ul>" + "".join([f"<li>{i}</li>" for i in [
    f"<b style='color:darkblue;'>{df_complete.groupby('Sector')['Valuation (USD B)'].mean().idxmax()}</b> startups have the highest valuations.",
    f"<b style='color:darkblue;'>{(df_complete.groupby('Sector')['Revenue_FY23'].mean() - df_complete.groupby('Sector')['Revenue_FY21'].mean()).idxmax()}</b> shows the highest revenue growth.",
    f"ESG adoption strongest in <b style='color:darkblue;'>{df_complete[df_complete['ESG Disclosed'] == 'Yes']['Sector'].mode()[0]}</b>."
]]) + "</ul>"

sentiment_note = "<p>Sentiment analysis included for available startups.</p>"
sentiment_section = "<h2>Media Sentiment Insights</h2><p>Charts and interpretation here...</p>"

final_html = build_html_report(df_complete, incomplete_count, insights_html, fig_dashboard, sentiment_note, sentiment_section)
with open(OUTPUT_HTML, "w") as f:
    f.write(final_html)

print(f"Outputs generated:\n- {OUTPUT_CLEANED}\n- {OUTPUT_SECTOR}\n- {OUTPUT_HTML}")
