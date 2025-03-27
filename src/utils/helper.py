import os
import pandas as pd
import logging
from datetime import datetime

# File handling
def load_file(file_path):
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    absolute_path = os.path.join(project_root, file_path)
    
    if not os.path.exists(absolute_path):
        raise FileNotFoundError(f"{absolute_path} does not exist.")
    return pd.read_csv(absolute_path)

# Logging
def log_message(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_levels = {
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR
    }
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.log(log_levels.get(level.upper(), logging.INFO), message)
    
# Data Validation    
def check_missing_values(df):
    empty_values = df.isnull().sum()
    return empty_values[empty_values > 0]
    
# Dataframe Description    
def describe_dataframe(df):
    print("DataFrame Shape:", df.shape)
    print("\nColumn Names:", df.columns.tolist())
    print("\nData Types:\n", df.dtypes)
    print("\nMissing Values:\n", check_missing_values(df))
    print("\nSummary Statistics:\n", df.describe())