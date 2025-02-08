import pandas as pd
from config import CSV_FILE_PATH

def extract_data():
    """Read Netflix dataset from CSV file."""
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        print(f"Successfully loaded {len(df)} records from Netflix dataset.")  # ✅ Removed emoji
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")  # ❌ Removed emoji
        return None

if __name__ == "__main__":
    df = extract_data()
    print(df.head())  # Display first 5 rows for verification
