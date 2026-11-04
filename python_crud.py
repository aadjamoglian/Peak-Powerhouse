""" CS340 Python CRUD Assignment Template File
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
        select * from locations
        """

        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        self.cursor.close()
        return results

    