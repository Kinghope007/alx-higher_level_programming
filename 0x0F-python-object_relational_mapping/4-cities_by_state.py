#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
Args:
        argv[1] (str): MySQL username.
        argv[2] (str): MySQL password.
        argv[3] (str): Database name.
"""

import MySQLdb
import sys
from sys import argv

if __name__ == "__main__":
    """
    Entry point of the script.
    Takes command line arguments for MySQL.
    Calls cities_by_state function to perform the required task.
    """
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # Create a cursor object using cursor() method
    cursor = db.cursor()
    # Execute a single SQL query to retrieve cities with state information
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)
    # Fetch all the rows and print them as specified
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # Close the cursor and database connection
    cursor.close()
    db.close()
