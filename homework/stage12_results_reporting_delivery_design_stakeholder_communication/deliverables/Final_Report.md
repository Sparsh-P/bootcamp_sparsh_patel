# Insights Report  

---

## 1. Risk–Return Tradeoff (Chart 1)  
**Key Insight:**  
Data preprocessing choices directly affect portfolio positioning on the risk–return plane.  

**Evidence:**  
- Outlier treatment (green): Higher return, slight increase in volatility.  
- Mean imputation (orange): Lower return, higher volatility → least desirable.  
- Baseline (blue): Middle ground but not the best.  

**Implication:**  
➡️ Cleaning methods are not neutral — they reshape the risk–return profile in meaningful ways.  

---

## 2. Return by Scenario (Chart 2)  
**Key Insight:**  
Returns diverge notably depending on preprocessing assumptions.  

**Evidence:**  
- Outlier adjustment delivers the **highest return (13.5%)**.  
- Mean imputation produces the **lowest return (11%)**.  

**Implication:**  
➡️ Portfolio returns are **highly sensitive to technical assumptions**, with tangible financial consequences.  

---

## 3. MetricA Across Categories (Chart 3)  
**Key Insight:**  
Performance strength is unevenly distributed across categories.  

**Evidence:**  
- Z: ~58.8  
- Y: ~67.5  
- X: ~72.5 (strongest)  

**Implication:**  
➡️ Category X emerges as a consistently stronger performer, signaling more robustness or upside potential.  

---

# Assumptions & Sensitivity Checks  

**Underlying Assumptions:**  
- Volatility used as a proxy for risk.  
- Sharpe ratio assumed sufficient for performance, though tail risks may be understated.  
- Preprocessing method (imputation/outlier rules) drives shifts in results.  
- Small sample size constrains broad generalization.  


| Scenario       | Assumption                  | Method        |
|----------------|----------------------------|---------------|
| Baseline       | Missing data imputation      | Median        |
| Alt-Outlier    | Outlier adjustment           | >3σ removed   |
| Alt-Impute     | Missing data imputation      | Mean          |

**Sensitivity Example:**  

| Assumption               | Baseline Return | Alt Scenario Return |
|---------------------------|-----------------|---------------------|
| Fill Nulls: Median        | 0.12            | 0.10                |
| Remove Outliers: 3σ       | 0.12            | 0.14                |  

---

# Decision Implications  

### Opportunities  
- Applying robust outlier treatment enhances risk-adjusted returns.  
- Category X deserves deeper exploration as a potential high-performing segment.  

### Risks  
- Naive mean imputation erodes performance and introduces bias.  
- Exclusive reliance on Sharpe ratio may conceal tail risks.  
- Limited dataset raises concerns over representativeness.  

---


---

# Appendix: Main Data Snapshot  

| Scenario      | Return | Volatility | Sharpe | Assumption   | Value  | Category | MetricA  | MetricB  | Date       |
|---------------|--------|------------|--------|--------------|--------|----------|----------|----------|------------|
| baseline      | 0.120  | 0.180      | 0.56   | imputation   | median | Z        | 68.23    | 158.66   | 2025-02-01 |
| alt_impute    | 0.110  | 0.185      | 0.49   | imputation   | mean   | Y        | 65.18    | 145.04   | 2025-02-02 |
| alt_outlier   | 0.135  | 0.190      | 0.61   | outlier_rule | 3σ     | X        | 93.85    | 120.38   | 2025-02-03 |

---
