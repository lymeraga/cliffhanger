import sqlite3

# Path to the target database file where all tables will be merged
target_db_path = 'merged.db'

# Paths to the source database files
source_db_paths = ['/Users/francescaelia/Documents/cs1951a/final-project-cliffhanger/db_data/TMBD Movies Dataset 1.db', 'db_data/TMBD Movies Dataset 2.db', 'db_data/TMBD Movies Dataset 3.db']

# Connecting to the target database (it will be created if it doesn't exist)
conn = sqlite3.connect(target_db_path)
cursor = conn.cursor()

for source_db in source_db_paths:
    # Attach source database
    cursor.execute(f"ATTACH DATABASE '{source_db}' AS source_db")

    # Assuming you know the table names or can retrieve them programmatically
    cursor.execute("SELECT name FROM source_db.sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    for table_name in tables:
        # Copy each table from the source DB to the target DB
        table_name = table_name[0]
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} AS SELECT * FROM source_db.{table_name}")

    # Detach the source database
    cursor.execute("DETACH DATABASE 'source_db'")

# Commit changes and close the connection
conn.commit()
conn.close()