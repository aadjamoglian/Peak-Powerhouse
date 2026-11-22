import os
from dotenv import load_dotenv
import mysql.connector
from python_crud import PeakPowerhouseQueries

# Load username and password from .env file
load_dotenv()

def print_menu():
    print("\nPeak Powerhouse Gym Database")
    print("1. View Tables")
    print("2. Insert Sales Details")
    print("3. Update Sales Details")
    print("4. Delete Sales Details")
    print("5. Other Saved Queries")
    print("0. Exit")

def print_view_table_menu():
    tables = ['Locations', 'Members', 'Memberships', 'Employees', 'Roles', 'Sales', 'Sales Details', 'Products']
    for index, table in enumerate(tables, start=1):
        print(f"{index}. View {table} table")

def print_saved_queries():
    queries = ['Sales By Location']
    for index, query in enumerate(queries, start=1):
        print(f"{index}. View {query} table")

def main():
    conn = mysql.connector.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USERNAME'),
        password = os.getenv('DB_PASSWORD'),
        database = 'peak_ph_db'
    )

    cursor = conn.cursor()

    q = PeakPowerhouseQueries(cursor, conn)

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("\n Table Options:")
            print_view_table_menu()
            print("0. Exit")
            view_choice = input("Choose an option: ")
            
            if view_choice == "1":
                locations = q.get_all_locations()
                print()
                for location in locations:
                    print(location)

            elif view_choice == "2":
                members = q.get_all_members()
                print()
                for member in members:
                    print(member)

            elif view_choice == "3":
                memberships = q.get_all_memberships()
                print()
                for membership in memberships:
                    print(membership)
                
            elif view_choice == "4":
                employees = q.get_all_employees()
                print()
                for employee in employees:
                    print(employee)

            elif view_choice == "5":
                roles = q.get_all_roles()
                print()
                for role in roles:
                    print(role)

            elif view_choice == "6":
                sales = q.get_all_sales()
                print()
                for sale in sales:
                    print(sale)

            elif view_choice == "7":
                sales_details = q.get_all_sales_details()
                print()
                for sales_detail in sales_details:
                    print(sales_detail)

            elif view_choice == "8":
                products = q.get_all_products()
                print()
                for product in products:
                    print(product)
            
            elif view_choice == "0":
                pass
            
            else:
                print("Invalid option...")
                print("Returing to main menu.")

        elif choice == "2":
            sales = q.get_all_sales()
            print("\nTransactions Ids:")
            for sale in sales:
                print(sale[0])
            transaction_id = input("\nEnter transaction id to add sales details for: ")

            products = q.get_all_products()
            print("\nProducts: ")
            for product in products:
                print(f"{product[0]} - {product[1]} ({product[2]}), Price: {product[3]}, Cost: {product[4]}")
            product_id = input("\nEnter product id to add product to sales details: ")

            quantity = input("\nEnter quantity for product to be added: ")
            q.add_sales_detail(transaction_id, product_id, quantity)

        elif choice == "3":
            sales_details = q.get_all_sales_details()
            print()
            for sales_detail in sales_details:
                print(sales_detail)
            update_id = input("\nEnter Sales Details Id to update quantity for: ")
            quantity = input("\nEnter new quantity: ")
            q.update_sales_detail_quantity(update_id, quantity)

        elif choice == "4":
            sales_details = q.get_all_sales_details()
            print()
            for sales_detail in sales_details:
                print(sales_detail)
            delete_id = input("\nEnter Sales Detiails Id to delete: ")
            q.delete_sales_detail(delete_id)

        elif choice == "5":
            print("\nSaved Query Options")
            print_saved_queries()
            print("0. Exit")
            query_choice = input("Choose an option: ")

            if query_choice == "1":
                rows = q.get_sales_by_location()
                print()
                for row in rows:
                    print(row)

            elif query_choice == "0":
                print("Returning to main menu.")

            else:
                print("Invalid option...")

        
        elif choice == "0":
            print("Exiting program.")
            break

        else:
            print("Invalid option...")


if __name__ == "__main__":
    main()
