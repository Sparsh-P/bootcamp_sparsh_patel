# Portfolio Optimization Project - Orchestration Plan

## Jobs/Tasks Overview

### Task 1: Data Acquisition & Validation
**Purpose**: Fetch historical stock data from Kaggle API and validate data quality  
**Estimated Runtime**: 15-20 minutes  
**Frequency**: Daily (for updates) / One-time (for historical backfill)

### Task 2: Data Cleaning & Preprocessing  
**Purpose**: Clean raw data, handle missing values, adjust for corporate actions  
**Estimated Runtime**: 10-15 minutes  
**Frequency**: After each data acquisition

### Task 3: Metrics Calculation
**Purpose**: Calculate CAGR, volatility, Sharpe ratio, max drawdown, correlation matrices  
**Estimated Runtime**: 5-10 minutes  
**Frequency**: After data preprocessing

### Task 4: Portfolio Simulation
**Purpose**: Generate 1,000 random portfolios with retail investor constraints  
**Estimated Runtime**: 2-3 minutes  
**Frequency**: Weekly or on-demand

### Task 5: Portfolio Evaluation & Ranking
**Purpose**: Evaluate portfolios, select top 5, rank stocks by frequency × weight  
**Estimated Runtime**: 1-2 minutes  
**Frequency**: After portfolio simulation

### Task 6: Results Export & Visualization
**Purpose**: Generate reports, charts, and export top 10 stock recommendations  
**Estimated Runtime**: 2-3 minutes  
**Frequency**: After portfolio ranking

## Task Dependencies (DAG Structure)

```
[Data Acquisition] 
       ↓
[Data Cleaning & Preprocessing]
       ↓
[Metrics Calculation]
       ↓
[Portfolio Simulation] 
       ↓
[Portfolio Evaluation & Ranking]
       ↓
[Results Export & Visualization]
```

**Critical Path**: All tasks are sequential with no parallel execution opportunities
**Total Pipeline Runtime**: ~35-53 minutes end-to-end

## Inputs/Outputs for Each Task

### Task 1: Data Acquisition & Validation
- **Inputs**: 
  - Kaggle API credentials (`kaggle.json`) (hidden in env file)
  - Stock universe list (`stock_symbols.csv`)
  - Date range parameters (2010-2024)
- **Outputs**: 
  - Raw stock data (`nse_all_stock_data.csv`)
  - Data quality report (`logs/data_quality_YYYYMMDD.json`)

### Task 2: Data Cleaning & Preprocessing
- **Inputs**: 
  - Raw stock data (`data/raw/stock_prices_YYYYMMDD.csv`)
  - Corporate actions data (`data/reference/corporate_actions.csv`)
- **Outputs**: 
  - Clean stock data (`data/processed/clean_stock_data.csv`)
  - Cleaning summary report (`logs/cleaning_report_YYYYMMDD.json`)

### Task 3: Metrics Calculation  
- **Inputs**:
  - Clean stock data (`data/processed/clean_stock_data.csv`)
  - Risk-free rate data (`data/reference/risk_free_rate.csv`)
- **Outputs**:
  - Stock metrics (`data/processed/stock_metrics.csv`)
  - Correlation matrix (`data/processed/correlation_matrix.csv`)

### Task 4: Portfolio Simulation
- **Inputs**:
  - Stock metrics (`data/processed/stock_metrics.csv`)
  - Simulation parameters (`config/simulation_config.yaml`)
- **Outputs**:
  - Portfolio compositions (`data/results/portfolio_weights.csv`)
  - Portfolio metrics (`data/results/portfolio_performance.csv`)

### Task 5: Portfolio Evaluation & Ranking
- **Inputs**:
  - Portfolio performance (`data/results/portfolio_performance.csv`)
  - Portfolio weights (`data/results/portfolio_weights.csv`)
- **Outputs**:
  - Top 5 portfolios (Shown as a graph)
  - Stock rankings (Shown as a graph)

### Task 6: Results Export & Visualization
- **Inputs**:
  - Stock rankings (`data/results/stock_rankings.csv`)
  - Portfolio performance (`data/results/portfolio_performance.csv`)
- **Outputs**:
  - Top 10 stocks report (`reports/top_10_stocks_YYYYMMDD.pdf`)
  - Visualization charts (`reports/charts/`)
  - Summary dashboard (`reports/portfolio_dashboard.html`)

## Logging & Checkpoint Strategy

### Logging Framework
- **Tool**: Python logging module with structured JSON output
- **Log Levels**: DEBUG, INFO, WARNING, ERROR, CRITICAL
- **Log Location**: `logs/pipeline_YYYYMMDD_HHMMSS.log`

### Checkpoint Strategy
**Checkpoint 1 - After Data Acquisition**:
- Save raw data with timestamp
- Log data volume, date range, missing symbols
- **Recovery**: Re-run from Kaggle API if checkpoint missing

**Checkpoint 2 - After Data Cleaning**:
- Save processed dataset with validation metrics
- Log cleaning operations performed, rows removed
- **Recovery**: Re-process from raw data checkpoint

**Checkpoint 3 - After Metrics Calculation**:
- Cache calculated metrics for all stocks
- Log computation time, any calculation warnings
- **Recovery**: Recalculate from clean data if needed

**Checkpoint 4 - After Portfolio Simulation**:
- Save all 1,000 portfolio compositions and performance
- Log simulation parameters, convergence status
- **Recovery**: Re-run simulation from metrics checkpoint

### Error Handling & Recovery
- **Data Quality Issues**: Retry with relaxed validation, log warnings
- **API Failures**: Implement exponential backoff, max 3 retries
- **Memory Issues**: Process data in chunks, implement garbage collection
- **Timeout Handling**: Set 30-minute timeout per task with graceful degradation

## Automation Strategy

### Automate Now
**Daily Data Updates**:
- **Rationale**: Market data changes daily, automation ensures freshness
- **Implementation**: Cron job at 6:00 AM IST (after market close)
- **Tasks**: Data Acquisition → Data Cleaning → Metrics Calculation

**Weekly Portfolio Refresh**:
- **Rationale**: Portfolio recommendations don't need daily changes, reduces computational cost
- **Implementation**: Scheduled every Sunday at 8:00 AM IST
- **Tasks**: Portfolio Simulation → Evaluation → Results Export

### Keep Manual (For Now)
**Historical Data Backfill**:
- **Rationale**: One-time setup, requires human validation of data quality across 14 years
- **Frequency**: As-needed when adding new stocks or extending history
- **Manual Steps**: Data validation, outlier investigation, corporate action adjustments

**Model Parameter Tuning**:
- **Rationale**: Requires domain expertise to adjust simulation constraints
- **Manual Steps**: Changing portfolio size (8-15), concentration rules (>50%), performance thresholds
- **Review Frequency**: Monthly analysis of results quality

**Report Distribution**:
- **Rationale**: Initial phase requires human review before stakeholder distribution
- **Manual Steps**: Quality check of top 10 stocks, performance validation, report formatting
- **Future Automation**: After 3 months of stable operation

**Emergency Handling**:
- **Rationale**: Market crashes, data anomalies require human judgment
- **Manual Steps**: Parameter adjustment during extreme market conditions
- **Triggers**: Correlation >0.8, volatility >50%, max drawdown >40%

### Future Automation Candidates (6-12 months)
- **Model retraining**: Automated parameter optimization based on performance feedback
- **Anomaly detection**: Automated flagging of unusual market conditions
- **Report generation**: Fully automated PDF generation and email distribution
- **Performance monitoring**: Automated comparison against benchmark indices