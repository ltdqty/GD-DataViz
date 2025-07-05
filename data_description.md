# Data Description

This document outlines the core variables used in the analysis of psychological wellbeing changes from the GiveDirectly unconditional cash transfer study in Kenya. It includes definitions for both source variables from the original dataset (`UCT_FINAL_CLEAN.tab`) and derived variables used in the final visualization.

---

## Source Variables (`UCT_FINAL_CLEAN.tab`)

| Variable            | Type     | Description |
|---------------------|----------|-------------|
| `surveyid`          | object   | Unique identifier for each survey respondent |
| `femaleres`         | Int64    | Indicator: 1 if respondent is female, 0 otherwise |
| `maleres`           | Int64    | Indicator: 1 if respondent is male, 0 otherwise |
| `village`           | Int64    | Numeric identifier for the respondent’s village |
| `treat`             | Int64    | 1 if individual received a cash transfer; 0 if not |
| `spillover`         | Int64    | 1 if non-recipient in a treatment village (potential indirect exposure) |
| `purecontrol`       | Int64    | 1 if individual resides in a village with no treated households |
| `control_village`   | Int64    | 1 if village did not receive any treatment assignment |
| `treatXlump`        | Int64    | 1 if respondent received a lump-sum transfer |
| `treatXmonthly`     | Int64    | 1 if respondent received monthly transfers |
| `treatXlarge`       | Int64    | 1 if respondent received a large transfer |
| `treatXsmall`       | Int64    | 1 if respondent received a small transfer |
| `psy_index_z0`      | float    | Standardized psychological wellbeing index at baseline |
| `psy_index_z_miss0` | Int64    | Missing-ness: 1 if missing, 0 if measured |
| `psy_index_z1`      | float    | Psychological wellbeing index at endline |

---

## Derived Variables (`summary_delta`)

| Variable          | Type    | Description |
|-------------------|---------|-------------|
| `Group`           | object  | Treatment group label (e.g., Lump Sum, Monthly, Spillover Control) |
| `Gender`          | object  | Gender category (`Female`, `Male`) |
| `Delta`           | float   | Mean change in wellbeing index (z1 − z0) for the subgroup |
| `Delta_Display`   | object  | Rounded delta value, formatted for display |
| `Percentile_Gain` | object  | Approximate percentile shift based on z-score delta, using standard normal distribution assumptions |

---

## Notes

- The group labeled *Spillover Control* includes individuals who did **not** receive a cash transfer themselves but lived in villages where others did. This group serves as the control group in the visualization because they have complete pre/post data and allow for estimation of neighborhood effects.
- Individuals in the *Pure Control* group (villages with no treated households) were excluded from subgroup comparisons due to widespread missingness in baseline psychological wellbeing scores (`psy_index_z0`), making it impossible to compute reliable change scores.

---

**Source**: Haushofer, Johannes; Shapiro, Jeremy, 2017. “Replication Data for: The Short-Term Impact Of Unconditional Cash Transfers To The Poor,” Harvard Dataverse. DOI: [10.7910/DVN/M2GAZN](https://doi.org/10.7910/DVN/M2GAZN)

