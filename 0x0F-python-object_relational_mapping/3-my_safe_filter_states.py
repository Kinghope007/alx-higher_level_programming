#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa where
name matches the provided argument (safe from MySQL injection).
Args:
        argv[1] (str): MySQL username.
        argv[2] (str): MySQL password.
        argv[3] (str): Database name.
        argv[4] (str): State name to search for.
"""

import MySQLdb
import sys
from sys import argv

if __name__ == "__main__":
    """
    Entry point of the script.
    Takes command line arguments.
    Calls safe_filter_states function to perform the required task.
    """
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
            )
    # Create a cursor object using cursor() method
    cursor = db.cursor()
    # Use parameterized query to prevent SQL injection
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (argv[4],))
    # Fetch all the rows and print them as specified
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # Close the cursor and database connection
    cursor.close()
    db.close()
