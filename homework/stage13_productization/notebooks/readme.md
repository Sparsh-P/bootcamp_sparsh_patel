# 📊 Options Pricing Model – Production Deployment

## Project Summary
This project delivers a production-ready **options pricing model** capable of estimating market prices for options based on key input features:

- **Implied Volatility**  
- **Moneyness**  
- **Volatility-Time Interaction**

The solution includes a **REST API** for programmatic access and a **Streamlit dashboard** for interactive visualization and exploration.

---

## Highlights & Insights

- **Optimal Model Performance**: Mean Absolute Error (MAE) of ~$58.8 using a “drop missing” strategy  
- **Explained Variance**: R² of 15.6%, indicating limited explanatory capability  
- **Data Sensitivity**: Performance improves by 19.3% when missing data points are dropped  
- **Caution**: Model outputs should be used as directional guidance, not precise pricing for trading

---

├── app.py # Flask API endpoints
├── app_streamlit.py # Streamlit dashboard
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── data/ # Input datasets
├── model/ # Pickled models
│ └── h13model.pkl
├── src/ # Utility scripts
│ └── utils.py
├── notebooks/ # Jupyter notebooks for development
└── reports/ # Output reports & charts
---

## Getting Started

### 1. Environment Setup

```bash
# Create a dedicated environment
python -m venv stage13_env

# Activate environment (macOS/Linux)
source stage13_env/bin/activate

# Activate environment (Windows)
stage13_env\Scripts\activate

# Install required dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Verify installation
python -c "import flask, streamlit; print('Dependencies installed successfully')"

import requests

# GET prediction
response = requests.get('http://127.0.0.1:5000/predict/0.25/1.05/0.05')
print(response.json())

# POST prediction
data = {'implied_volatility': 0.25, 'moneyness': 1.05, 'vol_time': 0.05}
response = requests.post('http://127.0.0.1:5000/predict', json=data)
print(response.json())


---
# Model Assumptions & Limitations


## Assumptions

- **Linear Relationship**: Market prices are assumed to vary linearly with implied volatility.  
- **Missing at Random (MAR)**: Any missing volatility data is assumed to be unrelated to the option prices.  
- **Temporal Stability**: The relationships between features and prices are considered stable over time and across market conditions.  

---

## Limitations

- **Low R² (15.6%)**: The model captures only a small portion of the price variability.  
- **Sensitivity to Missing Data**: Using imputation reduces performance by roughly 19.3%.  
- **Segment Bias**: The model performs poorly for options with low strikes.  
- **Wide Confidence Intervals**: High uncertainty in predictions limits precision.  

---

## Input Validation Ranges

| Feature | Minimum | Maximum |
|---------|---------|---------|
| Implied Volatility | 0.1 | 2.0 |
| Moneyness | 0.5 | 2.0 |
| Vol-Time Interaction | 0.0 | 0.5 |

---

## Risk Assessment

**Overall Risk Level**: Medium–High  

**Key Risk Areas**:  
- Limited explanatory power (R² only 15.6%)  
- Missing data may introduce systematic bias  
- Large prediction errors for extreme moneyness values  

**Recommended Mitigations**:  
1. Use the model for **directional guidance**, not precise pricing.  
2. Monitor **data quality in real time**.  
3. Build **segment-specific models** for different strike ranges.  
4. Conduct **regular model retraining and validation**.  

---

## Development Lifecycle

**Data Pipeline Stages**:  
1. **Stage 5-6**: Data storage and preprocessing  
2. **Stage 7-8**: Outlier detection and exploratory analysis (EDA)  
3. **Stage 9**: Feature engineering (moneyness, vol-time interaction)  
4. **Stage 10**: Model training using linear regression  
5. **Stage 11**: Risk evaluation and bootstrap validation  
6. **Stage 12**: Stakeholder reporting  
7. **Stage 13**: Production deployment (current stage)  

---

## Model Versions

- **v1.0**: Baseline linear regression using implied volatility only  
- **v1.1**: Added moneyness and vol-time interaction features  
- **v1.2**: Current version optimized using the drop-missing strategy  

---

## Testing Evidence

**Local Testing**:  
- Launch Flask API: `python app.py`  
- Test API endpoints using Jupyter notebooks or `curl`  
- Validate error handling for invalid inputs  
- Confirm confidence interval calculations  



---


## Next Steps

1. **Enhanced Features**: Include Greeks (Delta, Gamma, Theta, Vega)  
2. **Alternative Models**: Implement Black–Scholes benchmark  
3. **Real-Time Data**: Integrate live options market feeds  
4. **Security**: Add API key-based authentication  
5. **Monitoring**: Track prediction accuracy over time  
6. **Scaling**: Containerize for deployment on cloud infrastructure  

> For technical details or troubleshooting, refer to development notebooks from previous stages or check the API `/health` endpoint for the current model status.
