#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database
Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): State name to filter cities.
"""

import MySQLdb
import sys
from sys import argv

if __name__ == "__main__":
    """
    Entry point of the script.
    Takes command line arguments for MySQL.
    Calls filter_cities function to perform the required task.
    """
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    # Create a cursor object using cursor() method
    cursor = db.cursor()
    # Execute a single SQL query to retrieve cities of the specified state
    i = argv[4]
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (i,))
    # Fetch all the rows and print the results
    rows = cursor.fetchall()
    cities_list = [row[0] for row in rows]
    if cities_list:
        print(", ".join(cities_list))
    # Close the cursor and database connection
    cursor.close()
    db.close()
