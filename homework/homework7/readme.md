

### `winsorize_series(series, lower=0.05, upper=0.95)` (Stretch)
- Replaces extreme values with boundary values based on quantiles.
- Helps reduce the effect of outliers without removing data points.

---

##  Application to Numeric Column
- Applied the above functions on a numeric column (`X`).
- Created a **boolean outlier flag** indicating whether a point is an outlier.

---

##  Sensitivity Analysis

### Summary Stats (With vs. Without Outliers)
- Compared **mean, median, and standard deviation** across:
- All data
- Filtered (IQR-based outlier removal)
- Winsorized data

### Regression Analysis
- Fitted a **simple linear regression** (`y ~ x`) for:
- All data
- Filtered (IQR)
- Winsorized

#### Results:

| Method       | Slope    | Intercept | R²       | MAE      |
|--------------|----------|-----------|----------|----------|
| all          | 0.031638 | 0.000775  | 0.033588 | 0.006798 |
| filtered_iqr | 0.027082 | 0.000778  | 0.028844 | 0.006484 |
| winsorized   | 0.225155 | 0.000144  | 0.247920 | 0.005453 |

---

##  Reflection

- **Chosen Methods & Thresholds**:  
- IQR (1.5× rule of thumb) and Z-score (threshold = 3.0).  
- Winsorization at 5% (lower) and 95% (upper).  
- These are common thresholds in statistics for balancing robustness and retaining data.

- **Assumptions**:  
- Data roughly follows a distribution where IQR/Z-score methods are meaningful.  
- Outliers are due to noise or anomalies, not true signal.  
- Winsorization boundaries represent “reasonable” data ranges.

- **Observed Impacts**:  
- IQR-filtered data slightly reduced slope and R², with marginally better MAE.  
- Winsorization significantly increased slope and R², suggesting **outliers heavily distorted regression** in raw data.  
- MAE improved with both methods, especially winsorization.

- **Risks if Assumptions Are Wrong**:  
- Outliers might represent real phenomena (e.g., rare but important events). Removing/winsorizing them may bias conclusions.  
- If data is not approximately symmetric, Z-score thresholds may misclassify points.  
- Over-aggressive winsorization may understate variability.

---

## Original Data Generation Code (Not Used)
- The initial synthetic data gave a **near-perfect correlation** between `X` and `Y`.  
- This is **not desirable** for regression analysis since it masks the effect of outliers.

---

## Updated Random Generation Logic
- Introduced **outliers in only one column** to break the correlation.  
- Produces more realistic regression results where outlier handling makes a noticeable difference.

---
