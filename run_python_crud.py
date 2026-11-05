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
    database = 'peak_ph_db'
)

cursor = conn.cursor()

q = PeakPowerhouseQueries(cursor, conn)

Print table selects
print(q.get_all_locations())

print(q.get_all_members())

print(q.get_all_memberships())

print(q.get_all_employees())

print(q.get_all_roles())

print(q.get_all_sales())

print(q.get_all_sales_details())

print(q.get_all_products())

# There is a unique constraint for a sale and a product in the sales details table
# A product id may appear only once for an order, multiples of the product are handled
# with quantity parameter.
# print(q.add_sales_detail(2,2,1))

# Update quantity in sales details table
# print(q.update_sales_detail_quantity(2, 1))

# Delete row from sales_details table
# print(q.delete_sales_detail(6))

cursor.close()
conn.close()
