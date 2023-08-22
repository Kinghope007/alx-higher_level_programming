#!/usr/bin/python3
"""
Prints all rows in the states table of a database
with a name that matches a given arguemnt.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db_connection = MySQldb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3])
        cursor = db_connection.cursor()
        cursor.execute(
                'SELECT * FROM states WHERE name LIKE '{:S}' ORDER BY id ASC;'.format(sys.argv[4])
                )
       results = cursor.fetchall()
       for result in rsults:
           print(result)
           db_connection.close()
