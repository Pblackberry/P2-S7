import pyodbc
import json


def BuscarCatequizando(conexion):
    try:
        SQL_QUERY="{CALL Consultas.sp_ConsultarCatequizando}"
        cursor= conexion.cursor()
        cursor.execute(SQL_QUERY)
        contenido=cursor.fetchall()
        for i in contenido:
            print(f"{i.Id_catequizando}\t{i.Nombre}\t{i.Apellido}\t{i.Fecha_nacimiento}\t{i.Cedula}")
    except Exception as e:
         print("\n \t Ocurrió un error al conectar a SQL Server: \n\n", e)

def insertar_registro(conexion):
    aux_nivel=0
    l_NIVEL="0"
    try:
        with conexion.cursor() as cursor:
            SQL_QUERY="{CALL Consultas.sp_InsertarCatequizando(?,?,?,?,?,?,?)}"
            l_NOMBRE=input("Ingrese el nombre del nuevo catequizando: \t")
            l_APELLIDO=input("Ingrese el apellido del nuevo catequizando: \t")
            l_CEDULA=input("Ingrese la cedula del nuevo estudiante: \t")
            l_CERTIFICADO=input("Ingrese al codigo de certificado de bautizo \t")
            l_FECHA=input("Ingrese la fecha de nacimiento en formato año-mes-dia: \t")
            while aux_nivel==0:
                l_NIVEL=input("Seleccione el nivel al que se inscribirá al catequizanod\n1.Primera Comunion\n2.Confirmacion\n3.Pre Confirmacion\n")
                if l_NIVEL!="1" and l_NIVEL!="2" and l_NIVEL!="3":
                    print("Opcion incorrecta, seleccione un nivel del menu\n")
                else:
                    aux_nivel=1
                
            l_PERSONA=input("Ingrese el id de la persona representante del catequizando (ids actuales: 1,2 o 3): \n")
            cursor.execute(SQL_QUERY,(l_NOMBRE,l_APELLIDO,l_CEDULA,l_CERTIFICADO,l_FECHA,l_NIVEL,l_PERSONA))
            conexion.commit()
            print("Registro insertado con éxito")
        
    except Exception as e:
         print("\n \t Ocurrió un error al conectar a SQL Server: \n\n", e)
         
def actualizar_registro(conexion):
    try:
        with conexion.cursor() as cursor:
            SQL_QUERY = "{CALL Consultas.sp_ActualizarCatequizando(?,?,?)}"

            l_ID = input("Ingrese el ID del catequizando a actualizar: \t")
            l_NOMBRE = input("Ingrese el nuevo nombre: \t")
            l_APELLIDO = input("Ingrese el nuevo apellido: \t")

            cursor.execute(SQL_QUERY, (l_ID, l_NOMBRE, l_APELLIDO))
            conexion.commit()

            print("✅ Registro actualizado con éxito")

    except Exception as e:
        print("\n \t Ocurrió un error al conectar a SQL Server: \n\n", e)

         
def eliminar_registro(conexion):
    try:
        with conexion.cursor() as cursor:
            SQL_QUERY1="{CALL Consultas.sp_EliminarCatequizando(?)}"
            SQL_QUERY2="""DELETE FROM Catequizando.Certificados_otorgados WHERE Catequizando_Id_catequizando= ?"""
            SQL_QUERY3="""DELETE FROM Parroquia.Inscripción_catequizando_parroquia WHERE Catequizando_Id_catequizando= ?"""
            l_IDCatequizando=input("Ingrese el id del registro de catequizando que desea eliminar: \t")
            cursor.execute(SQL_QUERY2,(l_IDCatequizando))
            conexion.commit()
            cursor.execute(SQL_QUERY3,(l_IDCatequizando))
            conexion.commit()
            cursor.execute(SQL_QUERY1,(l_IDCatequizando))
            conexion.commit()
            print("registro eliminado con exito")
    except Exception as e:
         print("\n \t Ocurrió un error al conectar a SQL Server: \n\n", e)
         
