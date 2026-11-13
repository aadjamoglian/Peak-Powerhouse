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

# ---------- SELECT tests ----------
print("\n=== Locations ===")
print(q.get_all_locations())

print("\n=== Members ===")
print(q.get_all_members())

print("\n=== Memberships ===")
print(q.get_all_memberships())

print("\n=== Employees ===")
print(q.get_all_employees())

print("\n=== Roles ===")
print(q.get_all_roles())

print("\n=== Sales ===")
print(q.get_all_sales())

print("\n=== Sales Details ===")
print(q.get_all_sales_details())

print("\n=== Products ===")
print(q.get_all_products())

print("\n=== More Complex Queries ===")
print("--- Sales By Location ---")
print(q.get_sales_by_location())

# There is a unique constraint for a sale and a product in the sales details table
# A product id may appear only once for an order, multiples of the product are handled
# with quantity parameter.

# ---------- CRUD tests on sales_details ----------
# Test INSERT
print("\n=== Testing INSERT ===")
new_id = q.add_sales_detail(2, 3, 2)
print("New sales_details_id:", new_id)
print("Sales details after INSERT:")
print(q.get_all_sales_details())

# Test UPDATE
print("\n=== Testing UPDATE ===")
rows = q.update_sales_detail_quantity(new_id, 5)
print("Rows updated:", rows)
print("Sales details after UPDATE:")
print(q.get_all_sales_details())

# Test DELETE
print("\n=== Testing DELETE ===")
rows = q.delete_sales_detail(new_id)
print("Rows deleted:", rows)
print("Sales details after DELETE:")
print(q.get_all_sales_details())

cursor.close()
conn.close()
