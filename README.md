API to SQL ETL Pipeline for Netflix Data
Project Overview
This project demonstrates the process of extracting Netflix movie and TV show data from a CSV file, transforming it to suit the needs of an SQL database, and loading the transformed data into an SQLite database. The project also includes data visualization to explore various insights, such as rating trends over the years.

The ETL (Extract, Transform, Load) pipeline is automated and scalable, allowing for easy updates and further analysis on the Netflix dataset.

Features
Extract: Retrieves Netflix movie and TV show data from a CSV file.
Transform: Cleans and processes the data to make it suitable for database storage.
Load: Inserts the transformed data into an SQLite database.
Visualization: Provides charts showing trends in ratings by year, offering insights into the data.
Project Structure
graphql
Copy
Edit
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
│
└── README.md                       # This file
Steps to Run the ETL Pipeline
1. Clone the Repository
To get started, clone the repository to your local machine using the following command:

bash
Copy
Edit
git clone https://github.com/your-username/API_to_SQL.git
2. Install Dependencies
The project requires some Python libraries to run. Install them using pip:

bash
Copy
Edit
pip install -r requirements.txt
Make sure you have pandas, requests, sqlalchemy, and other dependencies listed in the requirements.txt.

3. Set Up Your Database
The project uses an SQLite database, so make sure that SQLite is installed and accessible on your machine. The ETL pipeline will create the database automatically when you run it.

4. Run the ETL Pipeline
To start the ETL pipeline, simply run the main script main.py:

bash
Copy
Edit
python etl_pipeline/main.py
This will trigger the ETL process:

Extract data from the CSV.
Transform the data to clean and structure it.
Load the data into an SQLite database.
5. Explore the Data
After running the pipeline, you can use the DB Browser for SQLite or any SQLite client to explore the netflix_show table and see the data.

6. Visualize the Data
For easy analysis, this project includes basic visualizations. To view the visualizations, check the visualizations/ folder. Here, you will find visualizations like rating trends over the years.

7. Testing the Pipeline
Tests have been written for the data transformation process to ensure the integrity of the ETL pipeline. You can run the tests by executing the following command:

bash
Copy
Edit
pytest tests/test_transform.py
Technologies Used
Python 3.x: The programming language used for the ETL pipeline.
pandas: For data manipulation and transformation.
SQLite: Lightweight relational database for storing the data.
Matplotlib: For data visualization.
pytest: For testing the transformation logic.
