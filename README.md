# Peak-Powerhouse

## Project Description

Peak Powerhouse is a gym database management system built with MySQL and Python. It stores information about gym locations, employees, members, memberships, products, and sales.

The Python application allows users to view records from all tables and add, update, or delete records in the sales_details table.

## Authors
Arthur Adjamoglian  
Min Deng  

CS340 - Group 3

## Project Files

- `peak_powerhouse_ddl.sql` - Creates the database tables and loads sample data.
- `peak_ph_db_queries.sql` - Contains the SQL queries.
- `python_crud.py` - Contains the Python database class.
- `run_python_crud.py` - Tests the database operations.
- `CLI_OUT.txt` - Shows the test results.


## Installation Instructions

1 - Rename `example.env` to `.env`.

2 - Open the .env file and check the host, username, and password. Update them to match your local MySQL settings.

The default settings are:
- Host: localhost
- Username: root
- Password: (empty)
- Database: peak_ph_db

3 - Set up virtual environment, run the following code below in terminal. 
*Make sure you are in the project folder*:

For Windows:

    python -m venv .venv
    .venv\Scripts\Activate.ps1

For MacOS:

    python3 -m venv .venv
    source .venv/bin/activate

4 - Run this script using pip to intall required modules:

    pip install -r requirements.txt

## Database Setup
5 - Create a MySQL database named peak_ph_db.

6 - Import peak_powerhouse_ddl.sql into the database using MySQL Workbench.

7 - The database should include sample data for testing.


## Run the Application

Run the following command in terminal:

    python run_python_crud.py


## Expected Output

The program prints data from all 8 tables.

It also shows the results of adding, updating, and deleting a record in the sales_details table.

The test output is included in CLI_OUT.txt.



## Acknowledgements

- Some code was based on the starter code from the CS340 Python CRUD Query App Assignment.

- The database design and project code were created by Arthur Adjamoglian and Min Deng.

- No AI was used in this assignment. All work is original.

