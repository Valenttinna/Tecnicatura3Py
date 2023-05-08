import psycopg2 #Para conectarno s Postgresql

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            #cursor = conexion.cursor()##ahora no lo necesito con el with
            #sentencia = 'SELECT * FROM persona'

            ##espesificamos que es lo que queresmos sin *
            #sentencia = 'SELECT id_persona, nombre FROM persona'

            ##o podemos ver solo los datos de una persona
     #       sentencia = 'SELECT * FROM persona WHERE id_persona = 1'
            ##cando ponemos = %s : placeholder
     #       cursor.execute(sentencia) #Ejecutar sentencia
     #       registros = cursor.fetchall()#Recupera todos los registros
     #       print(registros)

            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = input('Digite un numero para el id_persona: ')
            cursor.execute(sentencia,(id_persona,))
            registros = cursor.fetchone()
            print(registros)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

#cursor.close()## directamente se cierra con el with
conexion.close()
