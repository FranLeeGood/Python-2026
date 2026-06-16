# SETS (CONJUNTOS)

# CREANDO LOS PRIMEROS CONJUNTOS
colores_primarios = {'Azul', 'Rojo', 'Amarillo'}
colores_secundarios = set({'Naranja', 'Verde', 'violeta'})
print(type(colores_primarios))

print(f"CONJUNTO 1: {colores_primarios}")
print(F"CONJUNTO 2: {colores_secundarios}")

# CREANDO UN CONJUNTO NUEVO CON DUPLICADOS
colores_nuevos = {'Azul', 'Rojo', 'Celesete', 'Azul', 'Rojo'}
print(f"CONJUNTO 3: {colores_nuevos}")      # EN LOS SETS NO SE CONSIDERAN DUPLICADOS

# AGREGANDO UN NUEVO ELEMNTO AL SET COLORES_NUEVOS ADD()

colores_nuevos.add('Cafe')
print(f"CONJUNTO 3 ACTUALIZADO: {colores_nuevos}")

# ELIMINANDO UN ELEMENTO DEL SET COLORES_NUEVOS  DISCARD()
colores_nuevos.discard('Cafe')
print(f"CONJUNTO 3 ACTUALIZADO SIN EL COLOR CAFE: {colores_nuevos}")

# APLICANDO EL METODO INTERSECTION()
interseccion = colores_primarios.intersection(colores_nuevos)
print(f"CONJUTNO INTERSECTADO: {interseccion}")# SETS (CONJUNTOS)

# CREANDO LOS PRIMEROS CONJUNTOS
colores_primarios = {'Azul', 'Rojo', 'Amarillo'}
colores_secundarios = set({'Naranja', 'Verde', 'violeta'})
print(type(colores_primarios))

print(f"CONJUNTO 1: {colores_primarios}")
print(F"CONJUNTO 2: {colores_secundarios}")

# CREANDO UN CONJUNTO NUEVO CON DUPLICADOS
colores_nuevos = {'Azul', 'Rojo', 'Celesete', 'Azul', 'Rojo'}
print(f"CONJUNTO 3: {colores_nuevos}")      # EN LOS SETS NO SE CONSIDERAN DUPLICADOS

# AGREGANDO UN NUEVO ELEMNTO AL SET COLORES_NUEVOS ADD()

colores_nuevos.add('Cafe')
print(f"CONJUNTO 3 ACTUALIZADO: {colores_nuevos}")

# ELIMINANDO UN ELEMENTO DEL SET COLORES_NUEVOS  DISCARD()
colores_nuevos.discard('Cafe')
print(f"CONJUNTO 3 ACTUALIZADO SIN EL COLOR CAFE: {colores_nuevos}")

# APLICANDO EL METODO INTERSECTION()
interseccion = colores_primarios.intersection(colores_nuevos)
print(f"CONJUTNO INTERSECTADO: {interseccion}")