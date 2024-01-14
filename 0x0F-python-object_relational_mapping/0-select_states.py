#!/usr/bin/python3
"""
Script that list all states from the databse hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> \
                            <mysql password> \
                             <database name>
"""

import sys
from sys import argv
import MySQLdb

if __name__ == "__main__":
    # connect to the nysql server running on localhost at port 3306
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    # create a cursor ibject
    cursor = db.cursor()
    # Excute SQL to retrive states from the state table
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    # fetch all rows and print
    rows = cursor.fetchall()
    for row in rows:
        print(row)
