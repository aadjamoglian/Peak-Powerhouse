""" CS340 Design Python Class Application
-- Name: Arthur Adjamoglian & Min Deng
-- Citation for the following code: Starter code provided from Pyton CRUD Query App Assignment.
-- No AI was used in completion of this assignment. All work is original.

"""

import mysql.connector

class PeakPowerhouseQueries(object):
    """Python app that queries various relationships in peak_ph_db"""

    def __init__(self, cursor, connection=None):
        self.cursor = cursor
        self.connection = connection

    def _commit(self):
        """Commit if a connection object was provided."""
        if self.connection is not None:
            self.connection.commit()

    def get_all_locations(self):
        """Get all locations from peak powerhouse gym"""
        
        sql = """
        select * from locations;
        """

        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.cursor.close()
        return results

    def get_all_members(self):
        """Get all members across gyms member id, first name and last name"""

        sql = """
        select member_id, member_fname, member_lname from members;
        """

        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.cursor.close()
        return results

    def get_all_memberships(self):
        """Get all memberships"""

        sql = """
        select * from memberships;
        """

        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.cursor.close()
        return results

    def get_all_employees(self):
        """Get all employees employee id, first name, last name, phone, email"""

        sql = """
        select employee_id, employee_fname, employee_lname, employee_phone, employee_email
        from employees;
        """

        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.cursor.close()
        return results

    def get_all_roles(self):
        """Get all roles"""

        sql = """
        select * from roles;
        """

        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.cursor.close()
        return results

    def get_all_sales(self):
        """Get all sales records"""

        sql = """
        select * from sales;
        """

        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.cursor.close()
        return results

    def get_all_sales_details(self):
        """Get all sales details records"""

        sql = """
        select * from sales_details
        """

        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def get_all_products(self):
        """Get all products"""

        sql = """
        select * from products;
        """

        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.cursor.close()
        return results

    

    