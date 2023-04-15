#Declaraos una variable
try:

    archivo = open('prueba.txt','w', encoding= 'utf8')# w= write
    archivo.write('Programamos con diferenctes tipos de archivos, ahora en txt. \n')
    archivo.write('Los acentos son importantes para las palaras\n')
    archivo.write('Como por ejemplo: acción, ejecución\n')
    archivo.write('r= leer\na= anexar\nx = crea un archivo exepcion')
    archivo.write('\nt= texto \nb = archivos vinarios \nw+=leer y escribir')
    archivo.write('\nSaludos a todos los alumnos de la tecnicatura')
    archivo.write('\nCon esto terminamos')
except Exception as e:
    print(e)
finally: # Siemrpe se ejecuta
    archivo.close()# lo cierra
#archivo.write('Todo quedo perfecto')
# error el archivo ya quedo cerrado no se puede seguir anipulando fuera



