# Definir el diccionario con las notas
notas = {
    "Ana": 6.2,
    "Luis": 4.8,
    "Pedro": 3.9,
    "Sofía": 5.5
}

# Variable para llevar la cuenta de los aprobados
aprobados = 0

# se recorre el diccionario para mostrar los datos y evaluar
for nombre, nota in notas.items():
    if nota >= 4.0:
        estado = "Aprobado"
        aprobados = aprobados + 1  # sumamos 1 si aprobó
    else:
        estado = "Reprobado"
        
    # Imprimir en formato que se pide 
    print(f"{nombre} : {nota} -> {estado}")

# Espacio y total final
print()
print(f"Total de aprobados: {aprobados}")