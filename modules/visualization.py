import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def generate_dashboard(df_complete):
    fig_dashboard = make_subplots(
        rows=3, cols=2,
        subplot_titles=("Funding vs Revenue", "Business Model Distribution",
                        "Profitability by Sector", "ESG Disclosure by Sector",
                        "Profitability vs ESG Heatmap", "Revenue Growth by Size"),
        specs=[[{}, {"type": "domain"}], [{}, {}], [{}, {}]],
        vertical_spacing=0.15, horizontal_spacing=0.12
    )

    for trace in px.scatter(df_complete, x="Funding (USD B)", y="Revenue_FY23", color="Sector",
                            size="Valuation (USD B)", hover_data=["Startup"]).data:
        fig_dashboard.add_trace(trace, row=1, col=1)

    for trace in px.pie(df_complete, names="Business Model").data:
        fig_dashboard.add_trace(trace, row=1, col=2)

    for trace in px.histogram(df_complete, x="Sector", color="Profitability", barmode="group").data:
        fig_dashboard.add_trace(trace, row=2, col=1)

    for trace in px.histogram(df_complete, x="Sector", color="ESG Disclosed", barmode="group").data:
        fig_dashboard.add_trace(trace, row=2, col=2)

    heat_data = pd.crosstab(df_complete['Profitability'], df_complete['ESG Disclosed'])
    fig_dashboard.add_trace(go.Heatmap(z=heat_data.values, x=heat_data.columns, y=heat_data.index, colorscale="YlGnBu"), row=3, col=1)

    growth_data = df_complete.groupby("Size Category")[["Revenue_FY21","Revenue_FY23"]].mean().reset_index()
    for trace in px.bar(growth_data, x="Size Category", y="Revenue_FY23", color="Size Category").data:
        fig_dashboard.add_trace(trace, row=3, col=2)

    fig_dashboard.update_layout(height=1900, width=1250, title_text="Sustainable Business Models Dashboard: Curated Insights")
    return fig_dashboard
