# API to SQL ETL Pipeline for Netflix Data

## Project Overview

This project demonstrates the process of **extracting** Netflix movie and TV show data from a **CSV file**, **transforming** it to suit the needs of an SQL database, and **loading** the transformed data into an SQLite database. The project also includes **data visualization** to explore various insights, such as rating trends over the years.

The ETL (Extract, Transform, Load) pipeline is automated and scalable, allowing for easy updates and further analysis on the Netflix dataset.

## Features
- **Extract**: Retrieves Netflix movie and TV show data from a CSV file.
- **Transform**: Cleans and processes the data to make it suitable for database storage.
- **Load**: Inserts the transformed data into an SQLite database.
- **Visualization**: Provides charts showing trends in ratings by year, offering insights into the data.

## Project Structure
API_to_SQL/
│
├── etl_pipeline/                   # Folder containing the ETL pipeline scripts
│   ├── extract.py                  # Data extraction script
│   ├── transform.py                # Data transformation script
│   ├── load.py                     # Data loading script
│   └── main.py                     # Main script to run the entire ETL pipeline
│
├── data/                           # Folder for storing raw and processed data
│   └── netflix_data.csv            # CSV file containing Netflix movie and TV show data
│
├── visualizations/                 # Folder for storing visualizations
│   └── rating_trends.png           # Example chart visualizing ratings trends
│
├── tests/                          # Folder for test scripts
│   └── test_transform.py           # Unit tests for the transform process
