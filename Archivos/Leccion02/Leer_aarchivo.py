
archivo = open('prueba.txt','r', encoding='utf8')
#print(archivo.read())

#print(archivo.read(16))
#print(archivo.read(10))
#print(archivo.readline())
#print(archivo.readline())
# vamos a iterar el archovo, cada una de las lineas
#for linea in archivo:
    #print(linea)
#print(archivo.readlines()[9])

#Anexamos informacion, copiamos a otro
archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())
archivo.close()
archivo2.close()

print('Se ha terminado el proceso de leer y copiar archivos')