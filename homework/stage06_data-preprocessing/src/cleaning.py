

import pandas as pd
import numpy as np
from typing import List


def fill_missing_median(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
   
    df_copy = df.copy()
    
    for col in columns:
        if col in df_copy.columns:
            median_val = df_copy[col].median()
            df_copy[col] = df_copy[col].fillna(median_val)
            print(f"Filled {df[col].isna().sum()} missing values in '{col}' with median: {median_val:.2f}")
    
    return df_copy


def drop_missing(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    
    df_copy = df.copy()
    original_rows = len(df_copy)
    
    # Drop rows that don't meet threshold
    df_copy = df_copy.dropna(thresh=int(threshold * df_copy.shape[1]))
    
    dropped_rows = original_rows - len(df_copy)
    print(f"Dropped {dropped_rows} rows with <{threshold:.1%} non-null values")
    
    return df_copy


def normalize_data(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
   
    df_copy = df.copy()
    
    for col in columns:
        if col in df_copy.columns:
            min_val = df_copy[col].min()
            max_val = df_copy[col].max()
            
            if max_val != min_val:
                df_copy[col] = (df_copy[col] - min_val) / (max_val - min_val)
                print(f"Normalized '{col}' to range [0, 1]")
            else:
                print(f"Warning: '{col}' has constant values, skipping normalization")
    
    return df_copy

# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler, StandardScaler

# # MinMax scaling for numeric_col
# # scaler = MinMaxScaler()
# # df['numeric_scaled'] = scaler.fit_transform(df[['numeric_col']])

# # # StandardScaler
# # standardizer = StandardScaler()
# # df['numeric_standard'] = standardizer.fit_transform(df[['numeric_col']])


# def fill_missing_median(df, columns=None):
#     df_copy = df.copy()
#     if columns is None:
#         columns = df.select_dtypes(include=np.number).columns
#     for col in columns:
#         df_copy[col] = df_copy[col].fillna(df_copy[col].median())
#     return df_copy

# def drop_missing(df, columns=None, threshold=None):
#     df_copy = df.copy()
#     if columns is not None:
#         return df_copy.dropna(subset=columns)
#     if threshold is not None:
#         return df_copy.dropna(thresh=int(threshold*df_copy.shape[1]))
#     return df_copy.dropna()

# def normalize_data(df, columns=None, method='minmax'):
#     df_copy = df.copy()
#     if columns is None:
#         columns = df_copy.select_dtypes(include=np.number).columns
#     if method=='minmax':
#         scaler = MinMaxScaler()
#     else:
#         scaler = StandardScaler()
#     df_copy[columns] = scaler.fit_transform(df_copy[columns])
#     return df_copy