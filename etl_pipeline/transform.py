import pandas as pd

def transform_data(df):
    """Clean and structure the Netflix dataset."""
    # Drop missing values
    df.dropna(subset=['title', 'release_year', 'type'], inplace=True)

    # Rename columns for better SQL compatibility
    df.rename(columns={
        "show_id": "id",
        "type": "category",
        "release_year": "year"
    }, inplace=True)

    # Convert 'year' column to integer
    df['year'] = df['year'].astype(int)

    # Select relevant columns
    df = df[['id', 'title', 'category', 'year', 'rating', 'duration', 'description']]
    
    # Removed emoji characters
    print("Transformation complete!")
    return df

if __name__ == "__main__":
    sample_data = {
        "show_id": ["s1", "s2"],
        "title": ["Movie A", "Movie B"],
        "type": ["Movie", "TV Show"],
        "release_year": [2020, 2019],
        "rating": ["PG-13", "TV-MA"],
        "duration": ["90 min", "2 Seasons"],
        "description": ["A great movie", "An amazing TV show"]
    }
    df_sample = pd.DataFrame(sample_data)
    transformed_df = transform_data(df_sample)
    print(transformed_df)
