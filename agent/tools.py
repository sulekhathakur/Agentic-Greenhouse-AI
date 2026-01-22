import pandas as pd

def load_data():
    df = pd.read_csv("greenhouse.csv")
    return df

def basic_analysis(df: pd.DataFrame):
    summary = df.describe(include="all").to_string()
    return summary

def column_overview(df: pd.DataFrame):
    return f"Columns: {list(df.columns)} | Rows: {len(df)}"
