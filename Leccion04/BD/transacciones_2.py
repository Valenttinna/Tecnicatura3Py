import psycopg2 #Para conectarno s Postgresql

conexion = psycopg2.connect( user='postgres', password='admin', host='127.0.0.1',
    port='5432',
    database='test_bd')
try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s,%s,%s)'
    valores = ('Carlos','Carrazco','ccarraz@mail.com')
    cursor.execute(sentencia,valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s,email=%s WHERE id_persona=%s'
    valores = ( 'Fabri','Juarez','fjuarez@mail.com', 1)
    cursor.execute(sentencia, valores)


    conexion.commit()  # hacemos commit maualmente
    print('termina la transaccion')

except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo un rollback: {e}')
finally:
    conexion.close()

