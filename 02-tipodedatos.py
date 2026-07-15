# Numeros enteros
edad = 19
amnio_nacimiento = 2006


# Numeros flotantes (reales)
estatura = 1.85 # el decimal se utiliza punto no coma
peso = 50


#numeros complejos 
num_complejo = 4 + 2j        #   primera forma de crear un numero complejo 
otro_complejo = complex(4,2)   #  segunda forma de crear un numero complejo


print(num_complejo)
print(otro_complejo)


#operaciones aritmetica basica (Area de un triangulo)
base = 8
altura = 12.5

area = (base * altura)/ 2

PI = 3.14159
print(area)
print(f"el area del triangulo es de (area) cm")


#formato de salida de numeros 
print(f"el numeri PI tiene un valor de {PI:.4f}")


#El metodo de redondeo 
print(round(PI,2))
print (round(area))
print(f"el area del triangulo es de {round(area)} cm")


#transformaciones de numeros 

print(float(edad))


#cadenas de texto

carrera = "Ingenieria civil en informatica" 
institucion = "universidad de los lagos"
print(carrera[0])


#imprimir la posicion del caracter 
print(carrera)[0] #se imprime la primer letra 
print(carrera)[0] #se imprime ultima letra

print("hola" * 4) # multiplicacion de un string por un entero)

print(carrera[0:10]) #obteniendo una sub cadena (cortando strings)


# ARREGLOS (LISTAS)
print("--------- arreglos (listas)--------")
colores = ["azul", "rojo", "verde", "amarillo"] #arreglo de strings   # arreglo numerico
numeros = [1,2,3,4,5,6] 

print(colores[1]) # se imprime el primer elemento de la lista de cadena 
print(numeros[-1]) #se imprime el ultimo elmento de la lista numeros 
lista_mixta = [25, "hola" , True]
print(lista_mixta) 
 

#aplicando metodo split
print(carrera.split())  #separa la cadena en sub cadenas 
print(institucion.split())


#Booleanos logicos 
luz_electrica = True 
interruptor = False

print("-----booleanos-------")
print(luz_electrica)
print(interruptor)

print(f"El tipo de dato es {type(carrera)}")

print("-----EVALUANDO DATOS BOOLEANOS-------")
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("True"))
print(bool(4000))






