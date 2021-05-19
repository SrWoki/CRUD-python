import sqlite3 as lit

db = lit.connect('basedatos.db')

with db:
    nuevoNombre = "updatedName"
    user_id = 1



    cur = db.cursor()

    cur.execute("UPDATE usuarios SET nombre = ? WHERE id = ?", (nuevoNombre, user_id))
    db.commit()
    print("Datos actualizados")
