import sqlite3 as lit

def main():
    try:
        db = lit.connect('basedatos.db')
        cur = db.cursor()

        tablequery = "CREATE TABLE usuarios (id INT, nombre TEXT, email TEXT)"

        cur.execute(tablequery)
        print("TABLA CREADA")

    except lit.Error as e:
        print("No se pudo crear la tabla")


if __name__ == "__main__":
    main()