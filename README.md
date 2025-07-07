# GiveDirectly (GD) - Data Visualization

The views expressed here are my own. They are not necessarily representative of the views of GiveDirectly, the study's authors, or any affiliated organization.

This is a Python 'plotly' visualization based on data from a landmark cash transfer study: Haushofer, J., &amp; Shapiro, J. (2017). The short-term impact of unconditional cash transfers to the poor: Experimental evidence from Kenya. The Quarterly Journal of Economics.

You can view the interactive graphic here:  
**[View the graphic](https://ltdqty.github.io/GD-DataViz/GD_DataViz_Example.html)**

# Cash That Heals: Unconditional Transfers & Pyschological Wellbeing

A data storytelling project visualizing how various cash transfer models impacted psychological wellbeing—especially among women—in a landmark Universal Basic Income study conducted in Kenya by GiveDirectly and researched by Haushofer & Shapiro (2017).

This interactive report distills academic research into a straight-forward, standalone HTML visualization, illustrating mental health gains across treatment arms and genders using z-score deltas and percentile translations.

---

## The Visual

- **Title**: *Cash That Heals*  
- **Subtitle**: *How unconditional cash shaped mental health, by gender and treatment group*
- **Insight**: Across all transfer types, **women experienced meaningful psychological gains**—underscoring cash’s potential to support female mental health, even when not explicitly targeted.

You can view the interactive graphic here:  
**[View the graphic](https://ltdqty.github.io/GD-DataViz/GD_DataViz_Example.html)**

---

## Repository Contents

| File                    | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `GD_DataViz_Example.html` | Self-contained interactive Plotly graphic (no configuration needed)       |
| `GD_Kenya_Cash_Study.ipynb` | Jupyter Notebook with development process, styling, and insights        |
| `GD_Kenya_Cash_Study.py` | Python script for standalone HTML export                                   |
| `summary_delta.csv`     | Cleaned summary data: delta z-scores, gender, treatment group               |
| `UCT_FINAL_CLEAN.tab`   | Source data from the study (Haushofer & Shapiro, 2017)                      |
| `cover.png`             | Thumbnail preview of the chart                                              |
| `README.md`             | Project overview and usage                                                  |
| `data_description.md`   | Description of key variables used in the visualization                      |


## Methodology

# Original Data
Haushofer & Shapiro (2017), Replication Data for: The Short-Term Impact Of Unconditional Cash Transfers To The Poor: Experimental Evidence From Kenya.
[Harvard Dataverse DOI](https://doi.org/10.7910/DVN/M2GAZN)

# Data Processing steps:
- Extracted and filtered key variables from the source dataset
- Key variables include the psychological wellbeing index z-scores, treatment groups, and gender
- Computed **the change or delta** in the wellbeing index z-scores
- Computed **percentile gains** from z-score shifts using the standard normal distribution
- Rounded and formatted all numeric outputs for visual clarity and hover interactivity

---

## Nota bene

A z-score change of **+0.25** corresponds to an approximate shift from the **50th to the 60th percentile** in psychological wellbeing. Many transfer groups achieved even higher improvements in pyschological wellbeing.

**Note on "Spillover Control"**  
The group labeled *Spillover Control* includes individuals who did not receive cash transfers but lived in villages where other households did. Due to missing baseline data (`psy_index_z0`) for the “pure control” group (villages with no treatment exposure), we excluded them from the analysis to preserve comparability across pre-post outcomes.

---

## License

This project is shared under CC0 1.0 [https://creativecommons.org/publicdomain/zero/1.0/](./LICENSE). Attribution to original data authors retained and cited accordingly.

---

## Contact

Created by **jondlesko**  
[LinkedIn](https://www.linkedin.com/in/jonathan-lesko-ds/) • Data storytelling, public impact analytics, and intuitive visualization

