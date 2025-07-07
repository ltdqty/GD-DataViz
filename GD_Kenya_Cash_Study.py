#!/usr/bin/env python
# coding: utf-8

"""
Creates an interactive Plotly visualization of psychological wellbeing gains
by treatment group and gender, based on GiveDirectly’s Kenya Cash Transfer study
(Haushofer & Shapiro, 2017).
"""

# libraries
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
from scipy.stats import norm
import plotly.graph_objects as go
import copy


def main():
    
    # === 1: Load raw tab-delimited dataset ===
    df = pd.read_csv('UCT_FINAL_CLEAN.tab', sep='\t')

    # === 2: Slim to key columns ===
    dfs = df.iloc[:, np.r_[0:8, 13:17, 111, 113:115]].copy()

    # === 3: Explicitly map data types ===
    dtype_map = {
        'surveyid': 'object',
        'femaleres': 'Int64',
        'maleres': 'Int64',
        'village': 'Int64',
        'treat': 'Int64',
        'spillover': 'Int64',
        'purecontrol': 'Int64',
        'control_village': 'Int64',
        'treatXlump': 'Int64',
        'treatXmonthly': 'Int64',
        'treatXlarge': 'Int64',
        'treatXsmall': 'Int64',
        'psy_index_z0': 'float',
        'psy_index_z_miss0': 'Int64',
        'psy_index_z1': 'float'
    }

    for col, dtype in dtype_map.items():
        dfs[col] = dfs[col].astype(dtype)

    # === 4: Compute change in wellbeing (Δ z-score) ===
    dfs['delta_psy_index'] = dfs['psy_index_z1'] - dfs['psy_index_z0']

    # True average across all individuals (not an average of subgroup means)
    avg_delta = dfs['delta_psy_index'].mean().round(4)

    # === 5: Define treatment groups ===
    group_defs = {
        'Spillover Control': (dfs['treat'] == 0) & (dfs['purecontrol'] == 0),
        'Small Transfer': dfs['treatXsmall'] == 1,
        'Lump Sum': dfs['treatXlump'] == 1,
        'Monthly': dfs['treatXmonthly'] == 1,
        'Large Transfer': dfs['treatXlarge'] == 1
    }

    # === 6: Summarize deltas by group and gender ===
    records = []
    for group, condition in group_defs.items():
        for gender_label, gender_col in [('Female', 'femaleres'), ('Male', 'maleres')]:
            mask = condition & (dfs[gender_col] == 1)
            delta_mean = dfs.loc[mask, 'delta_psy_index'].mean()
            records.append({'Group': group, 'Gender': gender_label, 'Delta': delta_mean})

    summary_delta = pd.DataFrame(records)
    summary_delta['Delta'] = summary_delta['Delta'].round(4)

    # === 7: Compute percentile gain from z-score shift ===
    summary_delta['Percentile_Gain'] = summary_delta['Delta'].apply(
        lambda z: f"{round((norm.cdf(z) - 0.5) * 100, 1):+} pp"
    )
    summary_delta['Delta_Display'] = summary_delta['Delta'].apply(lambda x: f"{x:.4f}")

    # Sort group order by Female delta
    group_order = (
        summary_delta[summary_delta['Gender'] == 'Female']
        .sort_values(by='Delta')['Group']
        .tolist()
    )

    # === 8: Create Plotly bar chart ===
    fig = px.bar(
        summary_delta,
        x='Delta',
        y='Group',
        color='Gender',
        orientation='h',
        barmode='group',
        color_discrete_map={'Female': '#D4AF37', 'Male': '#2E5E4E'},
        category_orders={'Group': group_order},
        custom_data=['Gender', 'Delta_Display', 'Percentile_Gain']
    )

    # === 9: Layout and styling ===
    fig.update_layout(
        xaxis_title=dict(
            text='<b>Change in Psychological Wellbeing Index (Δ z-score)</b>',
            font=dict(family='Source Sans Pro', size=15)
        ),
        yaxis_title=dict(
            text='<b>Treatment Group</b>',
            font=dict(family='Source Sans Pro', size=15)
        ),
        xaxis=dict(showgrid=True, gridcolor='#E0E0E0', zerolinecolor='#8C8C8C'),
        yaxis=dict(autorange='reversed'),
        font=dict(color='#000000'),
        legend_title=dict(
            text='<b>Gender</b>',
            font=dict(family='Source Sans Pro', size=13, color='#000000')
        ),
        legend=dict(
            font=dict(family='Source Sans Pro', size=13, color='#000000')
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        bargap=0.3,
        margin=dict(t=100, b=140, l=80, r=100),
        width=1200,
        height=525,
        title=dict(
        text="<span style='font-size:20px; color:#2E5E4E; font-family:Georgia; font-weight:bold;'>Cash That Heals</span>"
             "<span style='font-size:16px; color:#2E5E4E; font-family:Georgia; font-style:italic;'>&nbsp;&nbsp;&nbsp;How unconditional cash shaped mental health, by gender and treatment group</span><br>"
             "<span style='font-size:15px; color:#444444; font-family:Source Sans Pro;'>Across all transfer types, women experienced meaningful psychological gains—underscoring cash's potential to support female mental health, even when not explicitly targeted.</span>",
        x=0,
        xanchor='left'
        )
    )

    fig.update_traces(
        hovertemplate=
            "<b>Group:</b> %{y}<br>" +
            "<b>Gender:</b> %{customdata[0]}<br>" +
            "<b>Δ z-score:</b> %{customdata[1]}<br>" +
            "<b>Approx. Percentile Gain:</b> %{customdata[2]}<extra></extra>"
    )

    # === 10: Annotate and export ===
    fig.add_vline(
        x=avg_delta,
        line_dash="dash",
        line_color="#8C8C8C",
        line_width=1.5,
        annotation_text=f"Avg Δ = {avg_delta}",
        annotation_position="top",
        annotation_font=dict(size=11, color="#8C8C8C")
    )

    fig.add_annotation(
        text="Note: A z-score change of 0.25 corresponds to a shift from the 50th to roughly the 60th percentile in psychological wellbeing.",
        xref="paper", yref="paper",
        x=0.5, y=-0.245,
        xanchor="center",
        showarrow=False,
        font=dict(family='Source Sans Pro', size=14, color="#000000"),
        align="center"
    )

    fig.add_annotation(
        text="<b>Source:</b> Haushofer <br>& Shapiro (2017),<br>"
             "<a href='https://doi.org/10.7910/DVN/M2GAZN' target='_blank'>Harvard Dataverse</a>",
        xref="paper", yref="paper",
        x=1.0125, y=0.5,
        xanchor="left",
        showarrow=False,
        align="left",
        font=dict(family='Source Sans Pro', size=12, color="#000000")
    )

    # === 11: Export static and interactive versions ===

    # Use a short, Kaleido-safe title for the PNG export
    static_title = "Cash That Heals: Mental wellbeing by gender and transfer type"
    fig.update_layout(title_text=static_title)

    # Export static image (for README or preview)
    fig.write_image("cover.png", width=1200, height=525, scale=2)

    # Restore the full HTML-rich title for the interactive version
    fig.update_layout(
        title=dict(
            text=(
                "<span style='font-size:20px; color:#2E5E4E; font-family:Georgia; font-weight:bold;'>Cash That Heals</span>"
                "<span style='font-size:16px; color:#2E5E4E; font-family:Georgia; font-style:italic;'>&nbsp;&nbsp;&nbsp;"
                "How unconditional cash shaped mental health, by gender and treatment group</span><br>"
                "<span style='font-size:15px; color:#444444; font-family:Source Sans Pro;'>"
                "Across all transfer types, women experienced meaningful psychological gains. Gender was not explicitly targeted in the study, however, and men's gains were larger.</span>"
            ),
            x=0,
            xanchor='left'
        )
    )

    # Export full interactive HTML
    fig.write_html("GD_DataViz_Example.html", full_html=True, include_plotlyjs="cdn")

if __name__ == "__main__":
    main()
