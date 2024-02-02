import sqlite3 as sql
import pandas as pd
conn = sql.connect("Base_de_Datos_Tortas.db")
cursor = conn.cursor()

#Funciones

#Mostrar datos de la Tabla
def mostrar_datos_tabla(datos):
    cursor.execute(f"SELECT * FROM {datos}")
    results = cursor.fetchall()
    results_df = pd.DataFrame(results)
    print("---------------------------------------------------------")
    print(results_df)
    print("---------------------------------------------------------")
    conn.commit()

#Añadir tortas a la Tabla
def añadir_tortas(tabla):
      nombre = input("Ingrese el nombre de la torta: ")
      detalle = input("Ingrese detalle de la torta: ")

      okey = True
      while okey:
            try:
                  precio = int(input("Ingrese el precio de la torta: "))
                  okey = False
            except:
                  print("debe ingresar dígitos")
            
      okey = True
      while okey:
            try:
                  stock = int(input("Ingrese cuantas tortas estaran a la venta: "))
                  okey = False
            except:
                  print("debe ingresar dígitos")
      cursor.execute(f"INSERT INTO {tabla} (TortasNombre,TortasDetalle,TortasPrecio,TortasStock) VALUES ('{nombre}','{detalle}',{precio},{stock});")
      print("----------------------------")
      print("Torta agregada a la lista")
      print("----------------------------")
      conn.commit()

#Mostrar tortas disponibles
def mostrar_tortas(tabla):
      cursor.execute(f"SELECT TortasID,TortasNombre FROM {tabla};")
      contador = 0
      for i in cursor:
            contador += 1
            print("---------------")
            print(f"{i[0]}- {i[1]}.")
      return contador

#modificar tortas
def modificar_tortas(tabla_tortas):
      indice = mostrar_tortas(tabla_tortas)
      bucle = True
      print("---------------")
      while bucle:
            try:
                  ID=int(input("Cual torta desea modificar? (Elegir la torta con el numero que le corresponda, con 0 para salir):\n"))
                  while ID < 0 or ID > indice:
                        ID=int(input("Dato Incorrecto. Cual torta desea modificar? (Elegir la torta con el numero que le corresponda, con 0 para salir):\n"))
                        
                  if ID != 0:      
                        cursor.execute(f"SELECT * FROM {tabla_tortas} WHERE TortasID = {ID};")
                        resultado = cursor.fetchone()
                        print(f"1- Nombre: {resultado[1]}")
                        print(f"2- Característia: {resultado[2]}")
                        print(f"3- Precio: {resultado[3]}")
                        print(f"4- Stock: {resultado[4]}")
                        
                        onda = "1"
                        while onda != "0":
                              eleccion = input("Que desea modificar? (Usar el número correspodiente de lo que desea cambiar, con 0 para salir): ")
                              if eleccion == "1":
                                    cambio = input("Ingrese el nuevo nombre de la torta: ")
                                    cursor.execute(f"UPDATE {tabla_tortas} SET TortasNombre = '{cambio}' WHERE TortasID = {ID};")
                                    conn.commit()
                                    onda = "0"
                                    bucle = False
                              elif eleccion == "2":
                                    cambio = input("Ingrese la nueva descripcion de la torta: ")
                                    cursor.execute(f"UPDATE {tabla_tortas} SET TortasDetalle = '{cambio}' WHERE TortasID = {ID};")
                                    conn.commit()
                                    onda = "0"
                                    bucle = False 
                              elif eleccion == "3":
                                    cambio = int(input("Ingrese el nuevo precio de la torta: "))
                                    cursor.execute(f"UPDATE {tabla_tortas} SET TortasPrecio = {cambio} WHERE TortasID = {ID};")
                                    conn.commit()
                                    onda = "0"
                                    bucle = False
                              elif eleccion == "4":
                                    cambio = int(input("Ingrese cuantas tortas estan disponibles para la venta: "))
                                    cursor.execute(f"UPDATE {tabla_tortas} SET TortasStock = {cambio} WHERE TortasID = {ID};")
                                    conn.commit()
                                    onda = "0"
                                    bucle = False
                              elif eleccion == "0":
                                    onda = "0"
                                    bucle = False
                              else:
                                    eleccion = input("Opcion Incorrecta. Usar el número correspodiente de lo que desea cambiar, con 0 para salir:\n")

                  else:
                        bucle = False
            except:
                  print("---------------\n")
                  print("Debe ingresar un número...\n")
                  mostrar_tortas(tabla_tortas)
                  print("---------------")
            
#eliminar tortas
def eliminar_tortas(base):
      seleccion = True
      while seleccion:
            try:
                  torta_id = mostrar_tortas(base)
                  print("---------------")
                  borrar = int(input("Cual torta desea eliminar? (Elegir la torta con el numero que le corresponda, con 0 para salir):\n"))
                  while borrar < 0 or borrar > torta_id:
                        borrar = int(input("Dato incorrecto. Cual torta desea eliminar? (Elegir la torta con el numero que le corresponda, con 0 para salir):\n"))
                  
                  if borrar != 0:
                        cursor.execute(f"SELECT * FROM {base} WHERE TortasID = {borrar};")
                        df = cursor.fetchone()
                        decision = input(f"Esta seguro de eliminar: {df[1]}? s/n: ").lower()
                        while decision != "s" and decision != "n":
                              print("---------------")
                              decision = input(f"Opcion Incorrecta. Esta seguro de eliminar: {df[0]}? s/n: ").lower()
                        
                        if decision == "s":
                              cursor.execute(f"DELETE FROM {base} WHERE TortasID = {borrar};")
                              conn.commit()
                              print("---------------")
                              print("Torta borrada de la lista.")
                  else:
                        seleccion = False
            except:
                  print("---------------")
                  print("Debe ingresar un numero...\n")
                  



#Consulta para crear la tabla y sus campos
cursor.execute("""CREATE TABLE IF NOT EXISTS Tortas (
                    TortasID INTEGER PRIMARY KEY AUTOINCREMENT,
                    TortasNombre TEXT,
                    TortasDetalle TEXT,
                    TortasPrecio INTEGER,
                    TortasStock INTEGER
              )""")


nombre_tabla = "Tortas"
respuesta = "1"

#menu programa
while respuesta != "0" and respuesta != "n":
      respuesta = input("""----------------------Tienda de Tortas----------------------
      1- Ver lista tortas.
      2- Añadir una torta al catálogo.
      3- Modificar algun elemento de una torta en particular.
      4- Eliminar una torta del catálogo.
      0- Finalizar Programa.
      """)
      if respuesta == "1":
            mostrar_datos_tabla(nombre_tabla)
            respuesta = input("Hacer otra consulta? s/n: ").lower()
            while respuesta != "s" and respuesta != "n":
                  respuesta = input("\nDatos incorrecto. Hacer otra consulta?: ").lower()
            if respuesta == "n": 
                  print("Adios!")
      elif respuesta == "2":
            opcion = "s"
            while opcion != "n":
                  añadir_tortas(nombre_tabla)
                  opcion = input("Agregar otra torta a la lista de venta?: ").lower()
                  while opcion != "s" and opcion != "n":
                        opcion = input(" Opcion Inconrrecta. Agregar otra torta a la lista de venta?: ").lower()
      elif respuesta == "3":
           modificar_tortas(nombre_tabla)
      elif respuesta == "4":
            eliminar_tortas(nombre_tabla)
      elif respuesta == "0":
            print("Adios!")
      else:
            print("Respuesta incorrecta.....")
 

conn.commit()
cursor.close()
conn.close()