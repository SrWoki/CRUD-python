from os import curdir
import sqlite3 as lit


db = lit.connect('basedatos.db')

with db:
    user_id = 1

    cur = db.cursor()
    cur.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
    db.commit()
    print("Usuario eliminado")