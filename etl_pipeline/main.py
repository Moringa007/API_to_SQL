from extract import extract_data
from transform import transform_data
from load import load_data

def run_etl():
    print("🚀 Starting Netflix ETL process...")

    # Extract
    df_raw = extract_data()
    if df_raw is None:
        print("❌ Extraction failed. Exiting.")
        return
    
    # Transform
    df_transformed = transform_data(df_raw)

    # Load
    load_data(df_transformed)

    print("✅ Netflix ETL process completed!")

if __name__ == "__main__":
    run_etl()
