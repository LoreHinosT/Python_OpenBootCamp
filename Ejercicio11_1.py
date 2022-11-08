import sqlite3 as sql


def createDB():
    conn=sql.connect("alumnos.db")
    conn.commit()
    conn.close()

def createTable():
    conn=sql.connect("alumnos.db")
    cursor=conn.cursor()
    cursor.execute(
        """CREATE TABLE alumnos(
            id integer,
            name text,
            surname text
        )
        """
    )

    conn.commit()
    conn.close()

def insertRow(id,nombre,apellido):
    conn=sql.connect("alumnos.db")
    cursor=conn.cursor()
    instruccion= f"INSERT INTO alumnos VALUES({id},'{nombre}','{apellido}')"
    cursor.execute(instruccion)

    conn.commit()
    conn.close()

def readRows():
    conn=sql.connect("alumnos.db")
    cursor=conn.cursor()
    instruccion= f"SELECT * FROM alumnos"
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)


if __name__=="__main__": 
    createDB()
    createTable()
    insertRow(1,"Lorena","Hinostroza")
    insertRow(2,"Facundo","Caballero")
    insertRow(1,"Mariela","Hijosa")
    insertRow(2,"Lola","Cab")
    insertRow(1,"Laura","Dias")
    insertRow(2,"Maria","Cabalo")
    readRows()

def search():
    conn=sql.connect("alumnos.db")
    cursor=conn.cursor()
    instruccion= f"SELECT * FROM alumnos WHERE name like'Laura'"
    #instruccion=f"SELECT * FROM streamers WHERE subs <1000 ORDER BY subs DESC'"
    cursor.execute(instruccion)
    datos=cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)
