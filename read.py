from os import curdir
import sqlite3 as lit

db = lit.connect('basedatos.db')

with db:
    cur = db.cursor()
    selectquery = "SELECT * FROM usuarios"
    cur.execute(selectquery)

    row = cur.fetchall()

    for data in row:
        print(data)