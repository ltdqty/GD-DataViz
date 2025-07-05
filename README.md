# GD-Data_Viz
Python 'plotly' visualization based on data from a landmark cash transfer study, Haushofer, J., &amp; Shapiro, J. (2017). The short-term impact of unconditional cash transfers to the poor: Experimental evidence from Kenya, The Quarterly Journal of Economics.

# Cash That Heals: Unconditional Transfers & Pyschological Wellbeing

A data storytelling project visualizing how various cash transfer models impacted psychological wellbeing—especially among women—in a landmark Universal Basic Income study conducted in Kenya by GiveDirectly and researched by Haushofer & Shapiro (2017).

This interactive report distills academic research into a compelling, standalone HTML visualization, illustrating mental health gains across treatment arms and genders using z-score deltas and percentile translations.

**Original Study**:  
Haushofer & Shapiro (2017), *The Short-Term Impact of Unconditional Cash Transfers to the Poor*  
[Harvard Dataverse DOI](https://doi.org/10.7910/DVN/M2GAZN)

---

## The Visual

- **Title**: *Cash That Heals*  
- **Subtitle**: *How unconditional cash shaped mental health, by gender and treatment group*
- **Insight**: Across all transfer types, **women experienced meaningful psychological gains**—underscoring cash’s potential to support female mental health, even when not explicitly targeted.

You can view the interactive graphic here:  
**[GD_DataViz_Example.html](./GD_DataViz_Example.html)**

---

## Repository Contents

| File | Description |
|------|-------------|
| `GD_DataViz_Example.html` | Self-contained interactive Plotly graphic (no configuration needed) |
| `main.ipynb` | Jupyter Notebook with development process, styling, and insight logic |
| `main.py` | Python script for standalone HTML export |
| `data_summary.csv` | Cleaned summary data: delta z-scores, gender, treatment group |
| `cover.png` | Thumbnail preview of the chart |
| `README.md` | Project overview and usage |
| `data_description.md` | Dictionary of key columns used in the visualization |

---

## 📈 Methodology

The underlying dataset is from:

**Haushofer & Shapiro (2017)**  
*The Short-Term Impact of Unconditional Cash Transfers to the Poor: Experimental Evidence from Kenya*  
Harvard Dataverse: [https://doi.org/10.7910/DVN/M2GAZN](https://doi.org/10.7910/DVN/M2GAZN)

### Processing steps:
- Extracted and filtered key variables from the source dataset
- Key variables include the wellbeing index z-scores by treatment group and gender
- Computed **the change or delta** in the wellbeing index z-scores
- Computed **percentile gains** from z-score shifts using the standard normal distribution
- Rounded and formatted all numeric outputs for visual clarity and hover interactivity

---

## Key Insight

A z-score change of **+0.25** corresponds to an approximate shift from the **50th to the 60th percentile** in psychological wellbeing. Many transfer groups achieved even higher improvements.

---

## License

This project is shared under CC0 1.0 [https://creativecommons.org/publicdomain/zero/1.0/](./LICENSE). Attribution to original data authors retained and cited accordingly.

---

## Contact

Created by **jondlesko**  
[LinkedIn](https://www.linkedin.com/in/jonathan-lesko-ds/) • Data storytelling, public impact analytics, and intuitive visualization


