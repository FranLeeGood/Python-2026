def multiplicacion(x): 
    return x * 10

y = multiplicacion(6)
print(f"El resultado de la funcion es {y}")

def saludo(nombre):
    print(f"Hola, mi nombre es + {nombre}")

saludo("Tomas")

def suma(a,b):
    return a + b
resultado = suma(2,3)
print(resultado)

def resta(a, b = 5):        # VALOR ASIGNADO EN CASO DE QUE NO SE INGRESE UN VALOR A B
    return a - b
resultado1 = resta(6)
print("Resultado 1 (b por defecto): ", resultado)

resultado2 = resta(4, 4)
print("Resultado 2 (b personalizado):", resultado2)

def calcular_potencia(base, exponente):
    return base * exponente
resultado = calcular_potencia(exponente=3, base=2)
print(resultado)

# NO RECURSIVO
def factorial_normal(n):
    r = 1
    i = 2
    while 1 <= n: 
        r *= i
        i += 1
        return r
print(factorial_normal(5))

# RECUSIVO
def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)
    
print(factorial_recursivo(5))