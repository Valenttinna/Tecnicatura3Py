import psycopg2 as bd #Para conectarno s Postgresql

conexion = bd.connect( user='postgres', password='admin', host='127.0.0.1',
    port='5432',
    database='test_bd')
try:
    #conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s,%s,%s)'
    valores = ('Macarena','Carrazco','mcarraz@mail.com')
    conexion.commit() #hacemos commit maualmente
    cursor.execute(sentencia,valores)
    print('termina la transaccion')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()

conexion.close()