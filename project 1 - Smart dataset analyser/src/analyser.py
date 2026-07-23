import pandas as pd


def get_overview(df):
    """Return basic dataset overview information."""
    return {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
    }


def get_missing_summary(df):
    """Return summary of missing values by column."""
    missing = df.isnull().sum()
    percent = df.isnull().mean() * 100
    return pd.DataFrame({"missing_count": missing, "missing_percent": percent}).sort_values(
        by="missing_count", ascending=False
    )


def get_duplicate_count(df):
    """Return the number of duplicate rows."""
    return int(df.duplicated().sum())


def get_constant_columns(df):
    """Return columns with constant values."""
    return [col for col in df.columns if df[col].nunique(dropna=False) <= 1]


def get_summary_statistics(df):
    """Return summary statistics for numerical and categorical columns."""
    numeric_stats = df.select_dtypes(include=["number"]).describe().transpose()
    categorical_stats = df.select_dtypes(include=["object", "category"]).describe().transpose()
    return numeric_stats, categorical_stats


def get_column_breakdown(df):
    """Return numeric and categorical column names."""
    numeric = df.select_dtypes(include=["number"]).columns.tolist()
    categorical = df.select_dtypes(include=["object", "category"]).columns.tolist()
    return numeric, categorical
