nota1 = float(input("ingrese su primera nota"))
nota2= float(input("ingrese su segunda nota "))
nota3= float(input("ingrese su tercera nota"))

lista_nota = []

lista_nota.append(nota1)
lista_nota.append(nota2)
lista_nota.append(nota3)

suma_nota = nota1[0] + nota2[1] + nota3[2]
promedio_nota = suma_nota/3


print("su nota final es:{promedio_nota}")