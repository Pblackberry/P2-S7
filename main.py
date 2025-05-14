import pyodbc
import json
import GestorEstudiantes

conexion=pyodbc.connect(GestorEstudiantes.ObtenerConexion())

print("consulta:\n")
GestorEstudiantes.BuscarCatequizando(conexion)
GestorEstudiantes.insertar_registro(conexion)
GestorEstudiantes.eliminar_registro(conexion)