from .analyzer import get_duplicate_count, get_missing_summary, get_constant_columns


def generate_recommendations(df):
    """Generate preprocessing recommendations based on dataset characteristics."""
    recommendations = []

    missing_summary = get_missing_summary(df)
    total_missing = int(missing_summary["missing_count"].sum())
    duplicate_count = get_duplicate_count(df)
    constant_columns = get_constant_columns(df)

    if duplicate_count > 0:
        recommendations.append(f"Remove {duplicate_count} duplicate row(s).")
    elif duplicate_count == 0:
        recommendations.append("No duplicate rows detected.")

    if total_missing > 0:
        recommendations.append(
            "Fill missing values using median for numerical columns and mode for categorical ones."
        )
    else:
        recommendations.append("No missing values detected.")

    if constant_columns:
        recommendations.append(
            f"Drop constant column(s): {', '.join(constant_columns)}." if constant_columns else ""
        )
    else:
        recommendations.append("No constant columns detected.")

    recommendations.append("Encode categorical columns to prepare for machine learning.")
    recommendations.append("Standardize numerical columns to normalize scales.")

    return [rec for rec in recommendations if rec]
