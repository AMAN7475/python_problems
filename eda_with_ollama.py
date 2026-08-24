import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ollama


# Function to Perform EDA
def eda_analysis(file):

    # Get file path
    file_path = file

    # Read CSV file
    df = pd.read_csv(file_path)

    # Fill missing values with median for numeric columns
    for col in df.select_dtypes(include=['number']).columns:
        df[col] = df[col].fillna(df[col].median())

    # Fill missing values with mode for categorical columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Data Summary
    summary = df.describe(include='all').to_string()

    # Missing Values
    missing_values = df.isnull().sum().to_string()

    return (
        f"\nData Loaded Successfully!\n\n"
        f"Summary:\n{summary}\n\n"
        f"Missing Values:\n{missing_values}"
    )