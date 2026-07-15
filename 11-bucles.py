from colorama import init, Fore 
init() #inicializando el paquete colorama

print(Fore.YELLOW +"======bucles=====")

#bucle while
edad = 15
num = 0
#while edad <18:
    #print("eres menor de edad, no puedes manejar")

    # BUCLE INFINITO
    #WHILE EDAD < 18:
    #PRINT("ERES MENOR DE EDAD, NO PUEDES MANEJAR")


#bycle inifnito n°2
#while True:
    #print(num)
    #num  +=2


# Bucle While
# Impresion de numeros de 0 al 100 (Incrementando de 2 en 2)
while num <= 100:
    print(num)
    num += 2
print(Fore.RED + "Primer Bucle Terminado!")

# Impresion de numeros de 100 al 200 + Condicion ELSE
while num<=200:
    print(num)
    num +=2
else:
    print('Mi condicion es igual o mayor a 200')
print(Fore.CYAN + 'Segundo bucle terminado')

#Combinar While con un if dentro
while num <=300:
    print(num)
    num += 2
    if num == 250:
        print("Mi condicion es igual a 250")
print(Fore.GREEN + 'Tercer Bucle Terminado!')

# Utilizar break
while num <= 400:
    print(num)
    num +=2
    if num == 350:
        print(Fore.MAGENTA + 'Se detiene el bucle')
        break
print(num)
print(Fore.MAGENTA + "Cuarto bucle Terminado!")

#Utilizar el continue

num = 0
while num<= 50:
    print(num)
    num +=1
    if num == 40:
        continue
    print(num)

#bucle infinito + break
  #  while True:
  #   parametro = input(">>> ingrese la palabra secreta")
   #  if parametro =="exit":
  #      break
   #  else:
       #  print(parametro)


     #bucle for 
     #for n°1
print(Fore.GREEN + "====BUCLES FOR ======")
for i in (1,2,3,4,5,6,7,8,9,10):
        print(i)

#iterando una lista
listita = [1,2,3,4,5,6,7,8,9,10]

for i in listita:
    print(i)


    # iterando una tercera forma (3° For)
for i in range(1,101):
    print(i)