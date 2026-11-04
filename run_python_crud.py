import os
from dotenv import load_dotenv
import mysql.connector
from python_crud import PeakPowerhouseQueries

# Load username and password from .env file
load_dotenv()

# Credentials for database
# Make sure to generate .env file with DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME
conn = mysql.connector.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USERNAME'),
    password = os.getenv('DB_PASSWORD'),
    database = os.getenv('DB_NAME')
)

cursor = conn.cursor()

q = PeakPowerhouseQueries(cursor, conn)

# Print statements for all table selects
print(q.get_all_locations())


cursor.close()
conn.close()
