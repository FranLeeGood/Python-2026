#se guarda en variables el consumo de ram en mañana,mediodia,tarde y noche y se transforman en decimales

manana = float(input("ingrese el consumo de ram de manana"))
print (manana)
mediodia = float(input("ingrese el consumo de ram de mediodia"))
print(mediodia)
tarde = float(input("ingrese el consumo de ram de tarde"))
print(tarde)
noche = float(input("ingrese el consumo de ram de noche"))
print(noche)
# El consumo de ram se guarda en una lista 
ram = [manana, mediodia, tarde, noche]
# Se saca cada consumo de ram de la lista 
consumo_manana = ram [0]
consumo_mediodia = ram [1]
consumo_tarde = ram [2]
consumo_noche = ram [3]

# Se suma el consumo total de la ram en general 
consumo_total = (consumo_manana + consumo_mediodia + consumo_tarde + consumo_noche)

#se promedia el consumo total de la ram y se divide por cada tiempo en el que se consumio
promedio = (consumo_total/4)

#muestra en pantalla el total del consumo de ram 
print(f"El consumo total es: {consumo_total} GB")
# Muestra el promedio del consumo de ram | consumo total divido en 4
print(f"El consumo promedio de RAM durante el dia es: {promedio}GB")

#se saca el consumo maximo
consumo_maximo = max(ram)
#se saca el consumo minimo
consumo_minimo = min(ram)
# es la diferencia que hay entre el consumo maximo y el minimo
rango_operacion = consumo_maximo - consumo_minimo

#se muestra en pantalla el consumo maximo, el minimo y la diferencia que hay entre el gasto de ram max y min
print(f"El consumo maximo detectado fue: {consumo_maximo}GB")
print(f"el consumo minimo detectado fue: {consumo_minimo}GB")
print(f"El rango de operacion del servidor es: {rango_operacion} GB")