import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('netflix_shows.db')

# Define the SQL query to count ratings per year
query = """
SELECT year, rating, COUNT(*) AS count
FROM netflix_shows
WHERE category = 'Movie'
GROUP BY year, rating
ORDER BY year, rating;
"""

# Execute the query and load it into a DataFrame
df = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Check the data
print(df.head())
