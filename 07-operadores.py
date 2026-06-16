# OPERADORES EN PYTHON 
a = 10
b =  5
c = 4
d= 10

print ("=== OPERADORES ARITMETICOS ===")
print (f"La suma entre la variable a y b es: {a + b}") # operador de suma
print (f"La resta entre la variable a y b es: {a - b}") # operador de resta
print (f"La multiplicacion entre la variable a y b es: {a * b}") # operador de producto
print (f"La division entre la variable a y b es: {a / b}") # operador de division
print (f"El modulo entre la variable a y b es: {a % b}") # operador de modulo
print (f"El coeficiente entre la variable a y b es: {a //+ b}") # operador de division entera
print (f"El resultado de b elevado a c (5^4): {b ** c}") # operador de potencia -> pow() hace

# se puede hacer esta operacion?
print ("Hola" * (int((10*2) / 5 )), "\n")

print("=== OPERADORES DE COMPARACION ===") # La salida es un booleano (True o False)
print (a == b ) # op igualdad
print (a != b ) # op desigualdad, distinto o diferente 
print (a > b ) # op mayor que
print (a < b ) # op menor que
print (a >= d ) # op mayor o igual que 
print (a <= d ) # op menor o igual que

print("=== OPERADORES LOGICOS ===")
"""" Trabajaremos con el siguiente ejemplo
    Tenemos un vehiculo que tiene bencina (variable_bencina) y una opcion
    que dice si esta encendido o no el vehiculo(variable encendido).
    Dependiendo del estado de cada variable, se ira cambiando por False o True """

# Variables Booelanos
bencina = True
encendido = True
edad = 19

# if = si
# else = sino

#  Utilizando el Operador AND
if bencina and encendido:
    print("El vehiculo puede arrancar")
else:
    print("E vehiculo no puede arrancar ")    


    # Utilizando el Operador OR
if bencina or encendido:
    print("El vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")

    #Utilizando el operador NOT junto and AND
if not bencina and encendido:
    print("El vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")

    #Utilizando el operador NOT junto al OR
if not bencina or encendido:
    print("El vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")

    #Utilizando el operador not junto al operador AND y OR
if(not bencina or encendido) or (encendido and edad>=18):
    print("El vehiculo puede arrancar")
else:
    print("El vehiculo no puede arrancar")










