import base64
from io import BytesIO, StringIO

import pandas as pd
import streamlit as st


def load_csv(uploaded_file):
    """Load a CSV file into a DataFrame."""
    try:
        if uploaded_file is None:
            return pd.DataFrame()

        return pd.read_csv(uploaded_file)
    except Exception as exc:
        st.error(f"Unable to read CSV file: {exc}")
        return pd.DataFrame()


def get_column_types(df):
    """Return numeric and categorical column lists."""
    numeric = df.select_dtypes(include=["number"]).columns.tolist()
    categorical = df.select_dtypes(include=["object", "category"]).columns.tolist()
    return numeric, categorical


def dataframe_to_csv_bytes(df):
    """Convert a DataFrame to CSV bytes for download."""
    buffer = StringIO()
    df.to_csv(buffer, index=False)
    return buffer.getvalue().encode("utf-8")


def calculate_quality_score(df):
    """Compute a score out of 100 based on data quality metrics."""
    if df.empty:
        return 0

    missing_ratio = df.isnull().mean().mean()
    duplicate_ratio = df.duplicated().mean()
    constant_ratio = (df.nunique(dropna=False) <= 1).mean()

    score = 100 - (missing_ratio * 50 + duplicate_ratio * 30 + constant_ratio * 20)
    score = max(0, min(100, score))
    return round(score, 1)


def create_download_link(df, filename="cleaned_dataset.csv"):
    csv_bytes = dataframe_to_csv_bytes(df)
    return csv_bytes
