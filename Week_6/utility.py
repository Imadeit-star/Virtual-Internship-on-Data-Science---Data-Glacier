import logging
import os
import subprocess
import yaml
import pandas as pd
import datetime
import gc
import re
################
# File Reading
################

def read_config_file(filepath):
    with open(filepath, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(exc)

def validate_column_headers(df, target_headers):
    """
    Validates the column headers of a pandas DataFrame against a list of target headers.

    Args:
        df (pandas.DataFrame): The DataFrame to validate.
        target_headers (list): A list of target column headers.

    Returns:
        bool: True if the column headers match, False otherwise.
    """
    current_headers = df.columns.tolist()

    if current_headers == target_headers:
        print("Column headers match the target headers.")
        return True
    else:
        print("Column headers do NOT match the target headers.")
        print("Current Headers:", current_headers)
        print("Target Headers:", target_headers)

        missing_headers = set(target_headers) - set(current_headers)
        if missing_headers:
            print("\nMissing Headers:", missing_headers)

        extra_headers = set(current_headers) - set(target_headers)
        if extra_headers:
            print("Extra Headers:", extra_headers)

        return False

def summarize_Dataframe(df, file_path):
    """
    Summarizes a pandas DataFrame by providing the number of rows, columns, file size,
    data types, missing values, and basic descriptive statistics.

    Args:
        df (pandas.DataFrame): The DataFrame to summarize.
        file_path (str): The path to the original file from which the DataFrame was loaded.
    """
    print("--- DataFrame Summary ---")
    print(f"Total number of rows: {df.shape[0]}")
    print(f"Total number of columns: {df.shape[1]}")

    try:
        file_size = os.path.getsize(file_path)
        print(f"File size: {file_size} bytes")
    except FileNotFoundError:
        print(f"Could not determine file size: File not found at {file_path}")

    print("\n--- Data Types ---")
    print(df.dtypes)

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    print("\n--- Descriptive Statistics (Numerical Columns) ---")
    try:
        display(df.describe())
    except Exception as e:
        print(f"Could not generate descriptive statistics: {e}")

    print("\n--- First 5 Rows ---")
    try:
        display(df.head())
    except Exception as e:
        print(f"Could not display head: {e}")
