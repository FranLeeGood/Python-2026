print("1, hamburguesa")
print("2,pizza")
print("3, completo italiano")

opcion = input("ingrese una de las 3 opciones")
match opcion: #esta funcion match funciona de la 3.9
    case"1":
        print("ha seleccionado una hamburguesa. Precio: $5000")
    case"2":
        print("has elegido una pizza. precio $7500")
    case"3":
        print("has elegido un completo italiano. precio $2500")
    case _: 
        print("opcion no valida, ingrese una de las 3 opciones")

hora = 18
match hora: 
    case h if 0 <= h < 6:
        print("Buenas madrugadas")
    case h if 6 <= h < 12:
        print("Buenos dias")
    case h if 12 <= h < 18:
        print("Buenas tardes")
    case h if 18 <= h < 24:
        print("Buenas noches")
    case _:
        print("Hora invalida")

x = [1, 2, 3]
match x: 
    case [a, b, c]:     # DESAGRUPANDO VALORES DE LA LISTA X
        print(f"Elementos de la lista x: {a}, {b}, {c}")

datos = dict(
    nombre = 'Victor',
    edad = 31 
)

match datos: 
    case {'nombre': n, 'edad': e}: 
        print(f"Nombre: {n}, Edad: {e}")


valor = input("Ingrese un numero entero para saber si es par o impar")
match valor: 
    case x if x % 2 == 0:       # MATCH TOMA EL VALOR DE CUALQUIER VALOR
        print(f"{valor} es un numeor Par")
    case x if x % 2 != 0:
        print(f"{valor} es un numeor Impar")

        
       
