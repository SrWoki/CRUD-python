import sqlite3 as lit


myuser = (

    (1, 'Fernando', 'fernando@gmail.com'),
    (2, 'Miguel', 'miguel@gmail.com'),
    (3, 'Carlos', 'carlos@gmail.com'),
    (4, 'Maria', 'maria@gmail.com'),


)

db = lit.connect('basedatos.db')

with db:
    cur = db.cursor()
    cur.executemany('INSERT INTO usuarios VALUES (?,?,?)', myuser)
    print("Datos insertada")