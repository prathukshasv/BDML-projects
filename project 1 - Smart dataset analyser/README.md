# Smart Dataset Analyzer

Smart Dataset Analyzer is a beginner-friendly Streamlit application built to help users explore, clean, and visualize CSV datasets with a single click. The app provides quick dataset overview reports, preprocessing suggestions, and downloadable cleaned data.

## Features

- Upload any CSV dataset.
- Display first five rows, shape, column names, and data types.
- Analyze missing values, duplicate rows, numerical columns, categorical columns, and summary statistics.
- Visualizations for missing values, correlations, histograms, and boxplots.
- Preprocessing suggestions for duplicates, missing values, encoding, and scaling.
- Dataset quality score shown as a progress bar.
- One-click preprocessing for cleaning and transforming the dataset.
- Download the cleaned dataset as a CSV file.

## Installation

1. Clone the repository or download the project folder.
2. Open the project in VS Code.
3. Create a Python virtual environment (recommended):

```bash
python -m venv .venv
```

4. Activate the environment:

- Windows PowerShell:
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- Windows CMD:
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open the displayed URL in your browser, upload a CSV file, and explore the dataset.

## Project Structure

```
Smart_Dataset_Analyzer/
├── dataset/
│   └── sample_dataset.csv
├── src/
│   ├── analyzer.py
│   ├── preprocessing.py
│   ├── visualizer.py
│   ├── recommendations.py
│   └── utils.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Screenshots

- Dataset overview and summary.
- Missing values bar chart.
- Correlation heatmap.
- Histogram and boxplot visualizations.
- Cleaned dataset download.

> Add actual screenshots to this section after running the app locally.
