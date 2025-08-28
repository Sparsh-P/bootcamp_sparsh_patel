# Portfolio Optimization and Stock Selection

##  Overview
This project demonstrates a **quantitative approach to portfolio construction and stock selection** using real-world market data.  
The objective was to mimic the behavior of a **common retail trader portfolio** (holding ~8–15 stocks, with 2–3 stocks dominating >50% of total weight) and evaluate performance through multiple risk-return metrics.  

Through simulation, analysis, and visualization, the project identifies **top-performing portfolios** and extracts the most consistently appearing stocks across them, ultimately producing a **ranked list of top 10 candidate stocks**.

---

## 📂 Project Structure

The project is organized into three main files:

1. **Data Preparation**
   - API call via **Kaggle** to fetch the dataset.
   - Initial **cleaning, filtering, and formatting** of stock price data for downstream analysis.

2. **Metrics & Transformation**
   - Defined functions to calculate core performance metrics:
     - **CAGR (Compound Annual Growth Rate)**
     - **Volatility**
     - **Sharpe Ratio**
     - **Max Drawdown**
     - **Returns**
     - **Correlation matrix**
   - Transformed stock-level data into portfolio-level metrics.

3. **Portfolio Simulation & Selection**
   - Generated **1,000 random portfolios**:
     - Each portfolio contained **8–15 stocks**.
     - Within each portfolio, **3 stocks constituted over half the weight** (to reflect typical retail investor concentration).
   - Evaluated all portfolios based on risk-return tradeoffs.
   - Selected the **top 5 portfolios**.
   - Extracted constituent stocks from these portfolios.
   - Ranked stocks by their **frequency of appearance** and **relative weights** across top-performing portfolios.

---

##  Methodology

### Step 1: Data Cleaning
- Pulled stock data using Kaggle API.
- Removed missing values and standardized time series.
- Filtered for liquid and actively traded securities.

### Step 2: Performance Metrics
We defined and computed the following:

1. **CAGR**  
   \[
   CAGR = \left(\frac{V_{final}}{V_{initial}}\right)^{\frac{1}{n}} - 1
   \]

2. **Volatility** (annualized standard deviation of returns)

3. **Sharpe Ratio**  
   \[
   \text{Sharpe} = \frac{R_p - R_f}{\sigma_p}
   \]

4. **Max Drawdown** (peak-to-trough decline)

5. **Returns** (cumulative & annualized)

6. **Correlation Matrix** (for diversification analysis)

### Step 3: Portfolio Simulation
- Constructed **1,000 random portfolios** subject to:
  - Portfolio size: **8–15 stocks**.
  - Concentration: **3 stocks hold >50%** weight.
- For each portfolio:
  - Calculated **expected return**.
  - Calculated **portfolio volatility**.
  - Derived **Sharpe ratio** and other metrics.

### Step 4: Stock Ranking
- Identified the **top 5 portfolios** by performance.
- Extracted all constituent stocks.
- Counted stock **frequency of appearance**.
- Weighted stocks by their **portfolio allocation share**.
- Computed a **final score** = Frequency × Weight.
- Ranked stocks by descending score.

---

##  Final Results

The **Top 10 Stocks** identified are:

| Rank | Stock        |
|------|--------------|
| 1    | CHOICEIN     |
| 2    | LGHL         |
| 3    | DOMS         |
| 4    | PIDILITIND   |
| 5    | HNDFDS       |
| 6    | GODREJAGRO   |
| 7    | EICHERMOT    |
| 8    | OIL          |
| 9    | SUPREMEIND   |
| 10   | CONCORDBIO   |

These stocks were selected because they consistently appeared in top portfolios and carried meaningful weights in allocation.

---

##  Visualizations

The project produced several key plots:

1. **Risk–Return Scatter**  
   - Plotted all 1,000 portfolios in volatility–return space.
   - Highlighted **top 5 portfolios** for clarity.

2. **Efficient Frontier Approximation**  
   - Displayed curve-like concentration of efficient portfolios.

3. **Correlation Heatmap**  
   - Showed inter-stock correlations.
   - Helped validate diversification benefits.

4. **Top 10 Stock Scores (Bar Chart)**  
   - Ranked final 10 stocks by descending score.
   - Clear visual identification of best candidates.

---




# Risks & Assumptions
- Data Quality & Timeliness: The analysis assumes that the dataset obtained from Kaggle is accurate, complete, and up to date. Any missing, incorrect, or stale data could bias portfolio results.
- Market Conditions: Historical returns and volatilities are used to compute portfolio metrics. These are not guaranteed predictors of future performance, as market dynamics may shift.
- Simplified Portfolio Construction: Portfolios were randomly generated with constraints (8–15 stocks, 3 with high weights). This mimics retail investor behavior but may not fully capture institutional or optimized strategies.
- No Transaction Costs or Taxes: The study assumes zero brokerage, slippage, or tax impact, which in reality can materially affect net returns.
- Risk-Free Rate: A constant risk-free rate was assumed in calculating Sharpe ratios. Changes in interest rates could alter risk-adjusted performance.
- Correlation Stability: Asset correlations were assumed static based on historical data. In reality, correlations often change, especially during market stress, which could impact diversification benefits.
- Survivorship Bias: Stocks included are based on availability in the dataset. Companies that were delisted, merged, or bankrupt may be excluded, leading to potential survivorship bias.
- Randomness in Portfolio Generation: Since portfolios are randomly generated, results may differ on reruns unless a fixed random seed is used.