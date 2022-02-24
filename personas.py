import sqlite3

class Personas:
    
    def abrir(self):
        conexion = sqlite3.connect("agregar ubicacion de la base de datos")
        return conexion
    
    def alta(self,datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql = "inser into personas(nombre,apellido,legajo) values (?,?,?)"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()
    
    def consulta(self,datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select description, legajo form persona where codigo =?"
            cursor.execute(sql,datos)
            return cursor.fetchall()
        finally:
            cone.close()
    
    def recuperar_todos(self):
        try:
            cone= self.abrir()
            cursor=cone.cursor()
            sql="select nombre, apellido, legajo from articulos "
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            