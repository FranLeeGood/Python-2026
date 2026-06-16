from colorama import init, Fore
init()
print(Fore.RED + "Texto Rojo")
print(Fore.BLUE + "Texto Azul")
print(Fore.MAGENTA + "Texto Magneta")
print(Fore.YELLOW + "Texto Amarillo")


#condicional IF
print(Fore.MAGENTA + "\n ==== Utilizando IF y ELSE ====")

#Declarando variables
licencia = False
edad= 17
automovil = False

# utilizando condicional if y else simples 
if license:
    print(Fore.YELLOW + "Puede conducir un automovil ya que es mayor de edad y tiene licencia")
else:
    print(Fore.YELLOW + "No puede conducir un automovil porque no es mayor de edad y no tiene licencia")

#Utilizar el comando ELIF
if licencia and edad >= 18: 
    print(Fore.CYAN +"puede conducir porque es mayor de edad")
elif automovil: # en otro lenguajes como c, elif = else if
    print( Fore.BLUE +"Tegno automovil, pero no tengo licencia ni la edad necesaria para conducir")
else:
    print(Fore.RED +"No puedo conducir, ya que no tengo la edad, ni la licencia, ni el automovil")

