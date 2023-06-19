#!/usr/bin/python3
"""
Prints all rows in the states table of a database
with a name that matches a given arguemnt.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) >= 5:
        db_connection - MySQldb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3])
        cursor = db_connection.cursor()
        state_name = sys.argv[4]
        cursor.execute(
                'SELECT * FROM states WHERE CAST(name AS BINARY) LIKE ' +
                'CAST("{}" AS BINARY) ORDER BY id ASC;'.format(state_name)
                )
       results = cursor.fetchall()
       for result in rsults:
           print(result)
           db_connection.close()
