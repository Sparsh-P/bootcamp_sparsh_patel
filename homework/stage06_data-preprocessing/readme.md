
---

## Cleaning Functions

Defined in `src/cleaning.py`:

- **`fill_missing_median(df)`**  
  Replaces missing numerical values with the median of the respective column.  

- **`drop_missing(df, threshold=0.5)`**  
  Drops rows or columns with missing values exceeding a specified threshold (default: 50%).  

- **`normalize_data(df)`**  
  Scales numerical features to a standard range  (0–1) for comparability.  

---

## Workflow

1. **Load Data**  
   Used the raw dataset from `/data/raw/`.  

2. **Apply Cleaning Functions**  
   Call the functions from `src/cleaning.py` inside our notebook.  

3. **Save Cleaned Data**  
   Stored the processed dataset in `/data/processed/`.  

4. **Compare Original vs Cleaned Data**  
   - Validate shape, missing values, and summary statistics.  
   - Highlighted key changes introduced by cleaning.  
 

---

## Cleaning Strategy

- **Handling Missing Data**  
  - Impute with median for numerical stability.  
    

- **Normalization**  
  - Ensure values across features are on comparable scales.  
  

- **Validation**  
  - Checked before/after dataset shape.  
  - Count missing values pre- and post-cleaning.  

---

---
