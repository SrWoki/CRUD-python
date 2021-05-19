import sqlite3 as lit

def main():
    try:
        db = lit.connect('basedatos.db')
        print("Base de datos creada ", db)

    except:
            print("Error al crear base de datos")

if __name__ == "__main__":
    main()
