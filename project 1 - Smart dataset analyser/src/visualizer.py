import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


def plot_missing_values(df):
    """Plot a bar chart of missing values by column."""
    missing = df.isnull().sum()
    if missing.sum() == 0:
        return None

    fig, ax = plt.subplots(figsize=(8, 4))
    missing = missing[missing > 0].sort_values(ascending=True)
    ax.barh(missing.index, missing.values, color="steelblue")
    ax.set_title("Missing Values by Column")
    ax.set_xlabel("Missing Count")
    ax.set_ylabel("Column")
    plt.tight_layout()
    return fig


def plot_correlation_heatmap(df):
    """Plot a correlation heatmap of numeric features."""
    numeric = df.select_dtypes(include=["number"])
    if numeric.shape[1] < 2:
        return None

    corr = numeric.corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax, cbar=True)
    ax.set_title("Correlation Heatmap")
    plt.tight_layout()
    return fig


def plot_histogram(df):
    """Plot histograms for numeric columns."""
    numeric = df.select_dtypes(include=["number"])
    if numeric.empty:
        return None

    numeric.hist(bins=10, edgecolor="black", alpha=0.7, figsize=(10, 5))
    fig = plt.gcf()
    fig.suptitle("Histogram of Numeric Columns")
    plt.tight_layout()
    return fig


def plot_boxplot(df):
    """Plot boxplots for numeric columns."""
    numeric = df.select_dtypes(include=["number"])
    if numeric.empty:
        return None

    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(data=numeric, orient="h", palette="pastel", ax=ax)
    ax.set_title("Boxplot for Numeric Columns")
    plt.tight_layout()
    return fig
