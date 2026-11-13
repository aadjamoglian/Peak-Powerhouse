import subprocess
import sys
import platform

# Get OS name
os_name = platform.system()
print("Operating System: " + os_name)

# Install virtual environment
try:
    subprocess.run(
        [sys.executable, "-m", "venv", ".venv"],
        check=True
    )

    print("Virtual environment created successfully.")
except subprocess.CalledProcessError as e:
    print(f"Failed to create virtual environment: {e}")

if platform.system() == "Windows":
    venv_python = r".venv\Scripts\python.exe"
else:
    venv_python = ".venv/bin/python"

# Install modules listed in requirements.txt
subprocess.run(
    [venv_python, "-m", "pip", "install", "-r", "requirements.txt"],
    check=True
)

print("Modules installed successfully!")

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

cursor.close()
conn.close()

print("Successfully loaded ddl file!")
