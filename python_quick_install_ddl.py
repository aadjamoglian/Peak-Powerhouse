from dotenv import load_dotenv
import os
import mysql.connector

# Load username and password from .env file
load_dotenv()

# Connect to MySQL server
conn = mysql.connector.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USERNAME'),
    password = os.getenv('DB_PASSWORD'),
    database = 'peak_ph_db'
)

cursor = conn.cursor()

# Create database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS peak_ph_db")
cursor.execute("USE peak_ph_db")

# Run DDL script
with open("peak_powerhouse_ddl.sql", "r", encoding="utf-8") as file:
    script = file.read()

queries = script.split(";")

for query in queries:
    query_stripped = query.strip();

    cursor.execute(query_stripped)

conn.commit()

cursor.close()
conn.close()

print("Successfully loaded ddl file!")
