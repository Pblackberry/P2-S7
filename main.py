import pyodbc
import json
import GestorEstudiantes

def main():
    # Conexión a la BD
    conexion = pyodbc.connect(GestorEstudiantes.ObtenerConexion())

    while True:
        print("\n\t** SISTEMA CRUD  Quito_Catequesis_DB_2025** \n")   
        print("\t***************************")  
        print("\tOpciones CRUD:\n")
        print("\t1. Consultar registros")
        print("\t2. Crear registro")
        print("\t3. Actualizar registro")
        print("\t4. Eliminar registro")
        print("\t5. Salir\n")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            GestorEstudiantes.BuscarCatequizando(conexion)
        elif opcion == '2':
            GestorEstudiantes.insertar_registro(conexion)
        elif opcion == '3':
            GestorEstudiantes.actualizar_registro(conexion)
        elif opcion == '4':
            GestorEstudiantes.eliminar_registro(conexion)
        elif opcion == '5':
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

    conexion.close()

if __name__ == "__main__":
    main()
