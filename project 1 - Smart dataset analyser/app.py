import streamlit as st
from src import analyzer, preprocessing, recommendations, utils, visualizer


def render_dataset_overview(df):
    overview = analyzer.get_overview(df)
    shape = overview["shape"]
    dtypes = overview["dtypes"]

    st.subheader("Dataset Overview")
    st.write(f"**Rows:** {shape[0]}  |  **Columns:** {shape[1]}")

    with st.expander("Preview dataset"):
        st.dataframe(df.head(5), use_container_width=True)

    st.write("**Column Names**")
    st.write(overview["columns"])

    st.write("**Data Types**")
    st.table(dtypes)


def render_analysis(df):
    st.subheader("Data Analysis")
    missing_summary = analyzer.get_missing_summary(df)
    duplicate_count = analyzer.get_duplicate_count(df)
    numeric, categorical = analyzer.get_column_breakdown(df)
    numeric_stats, categorical_stats = analyzer.get_summary_statistics(df)

    st.metric("Duplicate rows", duplicate_count)
    st.write("**Missing Values**")
    st.table(missing_summary)

    st.write("**Column Breakdown**")
    st.write(f"Numeric columns: {numeric}")
    st.write(f"Categorical columns: {categorical}")

    if not numeric_stats.empty:
        st.write("**Numeric Summary Statistics**")
        st.dataframe(numeric_stats)
    if not categorical_stats.empty:
        st.write("**Categorical Summary Statistics**")
        st.dataframe(categorical_stats)


def render_visualizations(df):
    st.subheader("Visualizations")

    missing_fig = visualizer.plot_missing_values(df)
    corr_fig = visualizer.plot_correlation_heatmap(df)
    hist_fig = visualizer.plot_histogram(df)
    box_fig = visualizer.plot_boxplot(df)

    if missing_fig is not None:
        st.pyplot(missing_fig)
    else:
        st.info("No missing values to display.")

    if corr_fig is not None:
        st.pyplot(corr_fig)
    else:
        st.info("Not enough numeric columns for correlation heatmap.")

    if hist_fig is not None:
        st.pyplot(hist_fig)
    else:
        st.info("No numeric columns to display histogram.")

    if box_fig is not None:
        st.pyplot(box_fig)
    else:
        st.info("No numeric columns to display boxplot.")


def render_recommendations(df):
    st.subheader("Preprocessing Suggestions")
    recs = recommendations.generate_recommendations(df)
    for rec in recs:
        st.write(f"- {rec}")


def main():
    st.set_page_config(page_title="Smart Dataset Analyzer", layout="wide")
    st.title("Smart Dataset Analyzer")
    st.write("Upload a CSV file and inspect your dataset with clean analytics, visualizations, and preprocessing tools.")

    if "df" not in st.session_state:
        st.session_state.df = None

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    sample_data_path = "dataset/sample_dataset.csv"

    if uploaded_file is not None:
        st.session_state.df = utils.load_csv(uploaded_file)
    else:
        st.info("Try the sample dataset or upload your own CSV file.")
        if st.button("Load sample dataset"):
            st.session_state.df = utils.load_csv(sample_data_path)
        with open(sample_data_path, "r", encoding="utf-8") as sample_file:
            st.download_button(
                label="Download sample dataset",
                data=sample_file.read(),
                file_name="sample_dataset.csv",
                mime="text/csv",
            )

    df = st.session_state.df

    if df is None or df.empty:
        return

    try:
        col1, col2 = st.columns([2, 1])

        with col1:
            render_dataset_overview(df)
            render_analysis(df)

        with col2:
            st.subheader("Dataset Quality")
            score = utils.calculate_quality_score(df)
            st.metric("Quality Score", f"{score}/100")
            st.progress(int(score))

            st.subheader("One-Click Preprocessing")
            remove_dup = st.checkbox("Remove duplicate rows", value=True)
            fill_missing = st.checkbox("Fill missing values", value=True)
            encode_cat = st.checkbox("Encode categorical variables", value=True)
            scale_num = st.checkbox("Standardize numerical columns", value=False)

            if st.button("Apply preprocessing"):
                df = preprocessing.apply_preprocessing(
                    df,
                    remove_duplicates_flag=remove_dup,
                    fill_missing_flag=fill_missing,
                    encode_flag=encode_cat,
                    scale_flag=scale_num,
                )
                st.success("Preprocessing applied successfully.")

            render_recommendations(df)
            csv_bytes = utils.create_download_link(df)
            st.download_button(
                "Download cleaned dataset",
                data=csv_bytes,
                file_name="cleaned_dataset.csv",
                mime="text/csv",
            )

        st.markdown("---")
        render_visualizations(df)
    except Exception as exc:
        st.error(f"An error occurred while processing the dataset: {exc}")


if __name__ == "__main__":
    main()
