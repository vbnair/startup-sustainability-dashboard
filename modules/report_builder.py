def build_html_report(df_complete, incomplete_count, insights_html, fig_dashboard, sentiment_note, sentiment_section):
    intro_text = """
    <h2>Executive Summary</h2>
    <p>This analysis examines 20 curated <b style='color:darkblue;'>Indian internet-based startups</b> across EdTech, FinTech, E‑commerce, and SaaS sectors 
    to evaluate their business model sustainability.</p>
    <h2>Methodology & Scope</h2>
    <p>The startups were selected based on IPO‑listing or unicorn status with credible financial and ESG data from IPO filings, 
    annual reports, and reputable databases. Analysis covers multi‑year revenues (FY21–FY23), funding, valuations, profitability, and ESG disclosures.</p>
    <h2>Purpose & Topic Alignment</h2>
    <p>This aligns with <b>‘An analysis of sustainable business models among internet business start‑ups in India’</b>, 
    assessing sustainability via financial resilience, growth, and ESG adoption.</p>
    """
    data_dict = """
    <hr><h3>Data Dictionary:</h3>
    <ul>
    <li><b>Valuation (USD B):</b> Estimated market value in billions of USD.</li>
    <li><b>Funding (USD B):</b> Total funding raised.</li>
    <li><b>Revenue FY21–FY23 (INR Cr):</b> Multi-year revenue data.</li>
    <li><b>Profitability:</b> Startup profitability status.</li>
    <li><b>ESG Disclosed:</b> Indicates if ESG initiatives are disclosed.</li>
    <li><b>Media Sentiment:</b> Sentiment score from latest news.</li>
    <li><b>IPO-Listed:</b> Indicates IPO status.</li>
    </ul>
    """
    footer = f"""
    <hr><p style="text-align:center; font-size:12px; color:gray;">
    Prepared by: Vaisakh<br>
    Disclaimer: Includes <b style='color:darkblue;'>{len(df_complete)}</b> startups with complete data.
    <b style='color:darkblue;'>{incomplete_count}</b> excluded due to missing data.
    </p>
    """
    final_html = f"""
    <html>
    <head><title>Sustainable Business Models Dashboard</title></head>
    <body style="font-family:Arial; line-height:1.6; margin:40px;">
    <h1 style="text-align:center; color:darkblue;">Sustainable Business Models Dashboard</h1>
    {intro_text}
    <h2>Key Insights</h2>
    {insights_html}
    {fig_dashboard.to_html(include_plotlyjs='cdn', full_html=False)}
    {sentiment_note}
    {sentiment_section}
    {data_dict}
    {footer}
    </body>
    </html>
    """
    return final_html
