## 5 ) Documentation (TODO)

### Data Storage
We will use a structured approach to store datasets in a way that is both efficient and easy to access. 
The data will be organized into specific folders and formats, with clear naming conventions.

Initially we setup the OS directory to the relevant bootcamp folder. 
The `.env` file will contain environment variables to override default paths for raw and processed data.
Here we will use `data/raw/` for original files such as CSV and `data/processed/` for cleaned datasets such as parquet.

- **Folders**:  
  - `data/raw/` → original input files (CSV).  
  - `data/processed/` → original input files for analysis (Parquet).  
  

- **Formats**:  
  - CSV for interoperability and quick inspection. It is human readable and widely supported.
  - Parquet for efficient storage and faster reads. It cannot be easily read by humans but is optimized for performance in data processing tasks.

- **Environment Variables**:  
  - `DATA_DIR_RAW` → overrides location of `data/raw/`.  
  - `DATA_DIR_PROCESSED` → overrides location of `data/processed/`.  
  - Defaults to `data/` subfolders if not set which in our case will be the downloads folder.

---

### Validation Checks
- Schema validation: expected column names ( `date`, `ticker`,`price`,).  
- Data types enforced `date` parsed as datetime.  
- Missing values handled through except statements.  


---

### Assumptions
- All datasets have a column named `date` when time-series analysis is expected.  
- Raw data is immutable (never edited in place; transformations go to `processed/`).  
- Datetime format is consistent across datasets and dataframe is cleaned before saving.
- Parquet engine (`pyarrow` or `fastparquet`) must be installed for Parquet support.  
