#!/usr/bin/python3
"""
Script that lsit all states from th e satabase
Args:
    username (str): MySQL username.
    password (str): MySQL password.
    db_name (str): Database name.
"""

import MySQLdb
import sys
from sys import argv

if __name__ == "__main__":
    # connect to Mysql server running
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    # create cursir object
    cursor = db.cursor()
    # Execute the sl query to retrive state with name stating with N
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    # fetall states in row
    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]
