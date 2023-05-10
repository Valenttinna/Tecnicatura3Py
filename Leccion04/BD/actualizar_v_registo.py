import psycopg2 #Para conectarno s Postgresql

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores= (
                ('Rafael','Ridolfi', 'rafael@mail.com', 5),
                ('Catalina','Martinez', 'catma@mail.com', 6),
            )#Tupla de tuplas
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Los registros actualizados son: {registros_actualizados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()