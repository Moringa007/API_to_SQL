from sqlalchemy import create_engine
from config import DATABASE_URI, TABLE_NAME

def load_data(df):
    """Load Netflix dataset into SQLite database."""
    engine = create_engine(DATABASE_URI)
    df.to_sql(TABLE_NAME, con=engine, if_exists='replace', index=False)
    # Removed the emoji
    print(f"Data successfully loaded into '{TABLE_NAME}' table.")

if __name__ == "__main__":
    import pandas as pd
    sample_df = pd.DataFrame([
        {'id': 's1', 'title': 'Movie A', 'category': 'Movie', 'year': 2020, 'rating': 'PG-13', 'duration': '90 min', 'description': 'A great movie'}
    ])
    load_data(sample_df)
