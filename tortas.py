import sqlite3 as sql

conn = sql.connect("Base_de_Datos_Tortas.db")

#Creamos la variable "cursor" para el recorrido en la base de datos a la hora de usar consultas
cursor = conn.cursor()

#Consulta para crear la tabla y sus campos
cursor.execute("""CREATE TABLE IF NOT EXISTS Tortas (
                    TortasID INTEGER PRIMARY KEY AUTOINCREMENT,
                    TortasNombre TEXT,
                    TortasDetalle TEXT,
                    TortasPrecio INTEGER,
                    TortasStock INTEGER
              )""")

#Consulta para agregar datos
# cursor.execute("INSERT INTO Tortas VALUES (1,'Torta de Chocolate','Tiene ojaldre y crema de durazno',7500,10)")

cursor.execute("INSERT INTO Tortas VALUES (2,'Torta Rellena','Ingrediente a eleccion',1500,2)")

# cursor.execute("INSERT INTO Tortas(TortasNombre,TortasPrecio,TortasStock) VALUES ('Torta de Frutilla',8000,4)")
# cursor.execute("INSERT INTO Tortas(TortasNombre,TortasPrecio,TortasStock) VALUES ('Torta de Helado',9750,15)")
# cursor.execute("INSERT INTO Tortas(TortasNombre,TortasPrecio,TortasStock) VALUES ('Torta de Balcarce',20000,6)")


conn.commit()

conn.close()