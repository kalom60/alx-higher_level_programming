#!/usr/bin/python3

"""
    a script that takes in an argument and displays all
    values in the states table of hbtn_0e_0_usa where
    name matches the argument
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306,
        charset="utf8"
    )

    cur = db.cursor()
    sql_input = "SELECT * FROM states WHERE name\
                LIKE '{}' ORDER BY id ASC".format(sys.argv[4])
    cur.execute(sql_input)
    data = cur.fetchall()

    for r in data:
        print(r)

    cur.close()
    db.close()
