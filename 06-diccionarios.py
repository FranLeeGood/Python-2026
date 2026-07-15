# DICCIONARIOS

paciente = {
    "nombre": "Benjamin Bahamonde",
    "edad": 18,
    "ciudad": "Ancud",
    "fechas_atencion": [5, 8, 12],
    "diagnostico": "resfrio comun",  
    "informacion_extra": {           
        "tipo_de_sangre": "A+",
        "hemograma": False
    }                                
}

# Segunda forma de declarar un diccionario 
medico = dict(
    nombre = 'Ignacio Saez',
    edad = 19,
    especialidad = 'cardiologo'     
)

print(type(paciente))
print(f"====== ficha paciente ===== \n{paciente}") 

# CONSULTA DE INFORMACION A  DICCIONARIIS

# ¿como consulto solo el nombre del pacienyte sin traer el diccionario completo"
print(f'nombre del paciente a consultar: {paciente['nombre']}')

#A diferencia de [], este metodo no genera error si no existe la clave
#metodo get() obtiene el valor de una clave, si no existe retorna None
print(paciente.get('nombre'))
print(paciente.get('rut,' 'N/D(no data)'))

#Retornar las claves, los valores o ambos como pares
print(paciente.keys()) #dict_keys(["nombre", "edad",....... ]) solo claves
print(paciente.values()) #dict_values(["Benjamin", "18", ......])
print(paciente.items()) #dict_items([("nombre", "Benjamin"),.....])

print(len(medico))
print(len(paciente))

#Modificacion del diccionario
#agregar una clave nueva al diccionario paciente

paciente['telefono'] = '+56936361020'
print(f"====== ficha con telefono ===== /n")
print(paciente) 

#Sobrescribir y/o actualizar valor de una clave existente
paciente['edad'] = 20

print("/n==== FICHA PACIENTE CON EDAD ACTUALIZADA ===== /n")
print(paciente)

# fusiona otro diccionario (a pares clave-valor) en el actual
# util para actualizar varios campos a la vez
paciente.update({'edad':21, 'ciudad':'Castro'})
print(paciente['edad'])
print(paciente['ciudad'])
print(paciente)

#eliminar una clave sin retorno
del(paciente['informacion_extra'])
print(paciente)
# Eliminar una clave y retornar su valor (a difenrecia de del, que no lo retorna) -> pop()
edad_eliminada= paciente.pop("edad")
print(f'Edad eliminada:{edad_eliminada}')
print(paciente)

#OTRAS  UTILIDADES DEL DICCIONARIO

#Con in se vverifica si una clave existe en el diccionario (sin usar condicionales todavia)
print('nombre' in paciente)
print('rut' in paciente)

#con copy() se crea una copia independiente del diccionario
paciente2 = paciente.copy()
paciente2['nombre'] = 'Miguel'
print(paciente["nombre"])
print(paciente2['nombre'])
print(paciente2)

# Con clear() elimina todos los elementos del diccionario, dejandola vacio (a diferencia del)
medico2 = medico.copy()
print("/n===== DICCIONARIO COPIA (MEDICO2)=====")
print(medico2)
medico2.clear()
print(medico2) #-> {}

#metodo map reemplaza un ford 
n =[1,2,3,4,5]
n_str = list(map(str,n))
print(f"Lista de numero con strings: {",".join(n_str)}")

#metodo filter()

ramos= []


# metodo zip
a = [1,2,3,4]
b = ["a","b","c","d"]

comprimir = list(zip)

