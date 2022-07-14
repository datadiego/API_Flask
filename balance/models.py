import sqlite3
from unittest import result

class DBManager:
    def __init__(self, ruta):
        self.ruta = ruta
    
    def consultaSQL(self, consulta):
        #1 conectar con la base de datos
        conexion = sqlite3.connect(self.ruta)

        #2 abrir un cursor
        cursor = conexion.cursor()

        #3 ejecutar consulta SQL (select, delete...)
        cursor.execute(consulta)

        #4 tratar los datos

        self.movimientos = []
        nombres_columnas = []

        for desc_columna in cursor.description:
            #devuelve como esta definida nuestra tabla
            nombres_columnas.append(desc_columna[0])
        #nombres_columnas ahora es ["id", "fecha", "concepto", "tipo", "cantidad"]
        datos = cursor.fetchall()

        for dato in datos:
            movimiento = {}
            indice = 0
            for nombre in nombres_columnas:
                movimiento[nombre] = dato[indice]
                indice += 1
            self.movimientos.append(movimiento)

        conexion.close()
        return self.movimientos


    def obtener_movimiento_por_id(self, id):
        consulta= "SELECT * FROM movimientos WHERE id=?"
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        cursor.execute(consulta, (id,))

        nombres_columnas = []
        
        datos = cursor.fetchone()
        resultado = None
        if datos:
            nombres_columnas = []
            for desc_columna in cursor.description:
                nombres_columnas.append(desc_columna[0])

            movimiento = {}
            indice = 0
            for nombre in nombres_columnas:
                movimiento[nombre] = datos[indice]
                indice += 1
            resultado = movimiento        

        conexion.close()
        return resultado

    def consulta_con_parametros(self, consulta, params):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        resultado = False
        try:
            cursor.execute(consulta, params)
            conexion.commit()
            resultado = True
        except Exception as error:
            print("ERROR DB:", error)
            conexion.rollback()
        conexion.close()
        return resultado
