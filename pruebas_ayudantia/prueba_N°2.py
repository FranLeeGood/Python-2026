print("=== Ejercicio 1 ===")

nombre_apellido = input("Ingrese su nombre y apellido: ")
edad = int(input("Ingrese su edad: "))
carrera = input("Ingrese el nombre de su carrera: ")
estatura = float(input("Ingrese su estatura: "))

print(f"Nombre: {nombre_apellido}\nEdad: {edad}\nCarrera: {carrera}\nEstatura: {estatura} cm")

print("\n=== Ejercicio 2 ===")

utiles_escolares = []

utiles_escolares.append("lapiz")
utiles_escolares.append("Cuaderno")
utiles_escolares.append("regla")

print(f"Primer útil escolar: {utiles_escolares[0]}\nSegundo útiil escolar: {utiles_escolares[1]}\nTercer útil escolar: {utiles_escolares[2]}")

print("\n === Ejercicio 3 ===")

mis_notas = []

mis_notas.append("5.5")
mis_notas.append("5.5")
mis_notas.append("5.5")
mis_notas.append("5.5")
mis_notas.append("5.6")

print(f" Cantidad de notas: \n nota 1: {mis_notas[0]} \n nota 2: {mis_notas[1]} \n nota 3: {mis_notas[2]} \n nota 4: {mis_notas[3]} \n nota 5: {mis_notas[4]} \n Nota Maxima: {max(mis_notas)} \n Nota Minima: {min(mis_notas)} \n Promedio notas: 5.5")