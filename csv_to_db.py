import csv
import sqlite3

# Create or open a SQLite database
conn = sqlite3.connect('dataset.db')
cur = conn.cursor()

# Information about your CSV files and their respective table structures
csv_info = [
    {
        "file_path": "/Users/francescaelia/Documents/cs1951a/final-project-cliffhanger/data/TMDB Movies Dataset 1.csv",
        "table_name": "Table1",
        "columns": "order_id INTEGER, id INTEGER PRIMARY KEY, imdb_id TEXT, popularity_score REAL, budget REAL, revenue REAL, original_title TEXT, cast TEXT, homepage TEXT, director TEXT, tagline TEXT, keywords TEXT, overview TEXT, runtime INTEGER, genres TEXT, production_company TEXT, release_date TEXT, vote_count INTEGER, vote_average REAL, release_year INTEGER, budget_adjusted REAL, revenue_adjusted REAL, profit REAL, popularity_level TEXT"
    },
    {
        "file_path": "/Users/francescaelia/Documents/cs1951a/final-project-cliffhanger/data/TMBD Movies Dataset 2.csv",
        "table_name": "Table2",
        "columns": "order_id INTEGER, id INTEGER PRIMARY KEY, original_language TEXT, original_title TEXT, overview TEXT, popularity_score REAL, release_date TEXT, title TEXT, vote_average REAL, vote_count INTEGER"
    },
    {
        "file_path": "/Users/francescaelia/Documents/cs1951a/final-project-cliffhanger/data/TMBD Movies Dataset 3.csv",
        "table_name": "Table3",
        "columns": "order_id INTEGER, id INTEGER PRIMARY KEY, title TEXT, original_language TEXT, release_date TEXT, vote_count INTEGER, popularity INTEGER, adult TEXT"
    }
]

# Create tables and import data
for info in csv_info:
    # Create table
    cur.execute(f"CREATE TABLE IF NOT EXISTS {info['table_name']} ({info['columns']})")
    
    # Import CSV data into table
    with open(info["file_path"], 'r') as file:
        dr = csv.DictReader(file)
        to_db = [(i[col] for col in dr.fieldnames) for i in dr]
        
        cols = ', '.join(dr.fieldnames)
        placeholders = ', '.join(['?']*len(dr.fieldnames))
        cur.executemany(f"INSERT INTO {info['table_name']} ({cols}) VALUES ({placeholders});", to_db)

# Commit and close
conn.commit()
conn.close()