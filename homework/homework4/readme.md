# Data Collection & Validation Tasks

## 1. API Pull 
- **Ticker**: `BRK-A`
- **Steps**:
  1. Load API key from `.env` 
  2. Request stock data via:
     - `requests` with Alpha Vantage or equivalent API, OR  
     - `yfinance` as fallback.
  3. Convert API response to a `pandas.DataFrame`.
  4. Parse datatypes:
     - Dates → `datetime64[ns]`
     - Changed the adjusted close column as it was in the premium api for alphavantage
     - Prices/Volumes → `float` or `int`
  5. **Validation**:
     - Ensured required columns exist (e.g., `date`, `open`, `high`, `low`, `close`, `volume`).
     - Check for missing values (`NA counts`).
     - Confirm expected shape (rows × columns).
  6. Save raw output as CSV → `api_source-alpha_symbol-BRK-A_20250817-174318.csv`.

---

## 2. Scraping a Small Table 
- **Source**: [Yahoo Finance – Most Active Stocks](https://finance.yahoo.com/most-active)
- **Steps**:
  1. Parse HTML using `BeautifulSoup`.
  2. Extract table into a `pandas.DataFrame`.
  3. Ensure proper column parsing:
     - Tickers → `str`
     - Prices/Volume/Change → numeric (`float`/`int`)
  4. **Validation**:
     - Confirm all rows parsed correctly.
     - Check for missing values.
     - Validate numeric ranges (e.g., positive volumes, non-null prices).
  5. Save raw output as CSV → `data/raw/most_active.csv`.

---

## 3. Documentation 
- **Notebook Deliverables**:
  - List **data sources/URLs**:
    - API: Alpha Vantage (or yfinance fallback).
    - Scrape: Yahoo Finance – Most Active Stocks.
  - Document parameters used (ticker = `BRK-A`, endpoints, scrape URL).
  - Explain validation logic (column checks, NA counts, dtype parsing).
  - Confirmed `.env` file is used for API key handling and **not committed** to version control.
  - **“Assumptions & Risks”** :
    - Data availability and API limits may affect completeness.
    - Web scraping may change if Yahoo modifies HTML structure.
    - Ticker availability may differ across providers.
