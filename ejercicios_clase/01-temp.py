# LISTA DE TEMPERATURA REGISTRADA 
temperatura = [12.5, 14.2, 11.8]
# SE SUMAN LAS TEMPERATURAS Y SE DIVIDEN POR LA CANTIDAD QUE SE ENCUENTRAN PARA CALCULAR EL PROMEDIO 
promedio = sum(temperatura) / len(temperatura)
# SE BUSCA LA TEMPERATURA MAS ALTA DE LA LISTA 
maxima = max(temperatura)
#SE BUSCA LA TEMPERATURA MAS BAJA DE LA LISTA 
minima = min(temperatura)
# SE RESTA EL VALOR MAXIMO MENOS EL MINIMO PARA LA DIFERENCIA 
diferencia = maxima - minima 
# SE MUESTRA EL RESULTADO 
print("el promedio es:", promedio)
# SE MUESTRA LA DIFERENCIA 
print("la diferencia es:", diferencia)


