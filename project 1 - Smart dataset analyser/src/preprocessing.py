import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def remove_duplicates(df):
    """Remove duplicate rows from the dataset."""
    return df.drop_duplicates().reset_index(drop=True)


def fill_missing_values(df):
    """Fill missing values using median for numeric and mode for categorical."""
    cleaned = df.copy()
    numeric_columns = cleaned.select_dtypes(include=["number"]).columns.tolist()
    categorical_columns = cleaned.select_dtypes(include=["object", "category"]).columns.tolist()

    for col in numeric_columns:
        if cleaned[col].isnull().any():
            median = cleaned[col].median()
            cleaned[col] = cleaned[col].fillna(median)

    for col in categorical_columns:
        if cleaned[col].isnull().any():
            mode = cleaned[col].mode(dropna=True)
            if not mode.empty:
                cleaned[col] = cleaned[col].fillna(mode.iloc[0])
            else:
                cleaned[col] = cleaned[col].fillna("Unknown")

    return cleaned


def encode_categorical(df):
    """Encode categorical columns using one-hot encoding."""
    categorical = df.select_dtypes(include=["object", "category"]).columns.tolist()
    if not categorical:
        return df.copy()

    return pd.get_dummies(df, columns=categorical, drop_first=True)


def standardize_numerical(df):
    """Standardize numeric values using standard scaling."""
    cleaned = df.copy()
    numeric_columns = cleaned.select_dtypes(include=["number"]).columns.tolist()
    if not numeric_columns:
        return cleaned

    scaler = StandardScaler()
    cleaned[numeric_columns] = scaler.fit_transform(cleaned[numeric_columns].astype(float))
    return cleaned


def apply_preprocessing(
    df,
    remove_duplicates_flag=True,
    fill_missing_flag=True,
    encode_flag=True,
    scale_flag=False,
):
    """Apply preprocessing steps in order and return cleaned dataset."""
    cleaned = df.copy()
    if remove_duplicates_flag:
        cleaned = remove_duplicates(cleaned)
    if fill_missing_flag:
        cleaned = fill_missing_values(cleaned)
    if encode_flag:
        cleaned = encode_categorical(cleaned)
    if scale_flag:
        cleaned = standardize_numerical(cleaned)
    return cleaned
