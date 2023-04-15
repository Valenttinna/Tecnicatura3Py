from NumerosIgualesException import NumeroIgualesException

resultado = None

try:
    a = int(input('digite el primer numero: '))
    b = int(input('digite el segundo numero: '))
    if a == b:
        raise NumerosIgualesException('son Numeros iguales')
    resultado  = a/b
except TypeError as e: # Clase HIJA
    print(f'TypeError - Ocurrio un error: {type(e)}')
except ZeroDivisionError as e: # Clase HIJA
    print(f'ocurrio un error: {type(e)}')
except Exception as e:# Clase PADRE, SIEMPRE VA A L FINAL
    print(f'Ocurrio un error: {type(e)}')
else:
    print("No se arrojo ninguna excepcion")
finally:# Siempre se va a ejecutar
    print("Ejecucion de este bloque finally")
print(f'El resultado es: {resultado}')
print('Seguimos...')
