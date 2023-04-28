import psycopg2 #Para conectarno s Postgresql

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_bd'
)

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia) #Ejecutar sentencia
registros = cursor.fetchall()#Recupera todos los registros
print(registros)

cursor.close()
conexion.close()
