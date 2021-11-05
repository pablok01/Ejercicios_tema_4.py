import re
import string
opcion = 0
while opcion!=6:
  print("1.Variables válidas. Ejemplo: suma, i, cont7, etc.\n2.Enteros y decimales. 2.7, 3.1416, 0.2, etc.\n3.Expresiones aritméticas (suma, resta, multiplicación, división, etc.). Ejemplo: suma = 2 + 1, cont = cont + 1, etc\n4.Operadores condicionales (mayor, menor, igual, diferente, etc.) Ejemplo: edad >= 18, cont < 100, etc.\n5.Cadenas de caracteres")
  opcion=int(input("ingrese una opcion "))
  # Variables válidas. Ejemplo: suma, i, cont7, etc.
  if opcion==1:
    filename= "hola.txt"
    textfile=open(filename,"r")
    regex ="[^\'\"\d][a-zA-Z_][a-zA-Z_0-9]*[^\'\"]"
    reg = re.compile(regex)
    for line in textfile:
        lista=reg.findall(line)
        print(lista)
    textfile.close()
# Enteros y decimales. 2.7, 3.1416, 0.2, etc.
  elif opcion==2:
      filename = "hola.txt"
      textfile = open(filename, "r")
      regex = "\d+\.?\d*"
      reg = re.compile(regex)
      for line in textfile:
          lista = reg.findall(line)
          print(lista)
      textfile.close()
# Expresiones aritméticas (suma, resta, multiplicación, división, etc.). Ejemplo: suma = 2 + 1, cont = cont + 1, etc
  elif opcion==3:
      filename = "hola.txt"
      textfile = open(filename, "r")
      regex = "([A-za-z]\w*|\d\.?\d*)\s?(\+|\-|\*|\/)\s?([A-za-z]\w*|\d\.?\d*)"
      reg = re.compile(regex)
      for line in textfile:
          lista = reg.findall(line)
          print(lista)
      textfile.close()
# Operadores condicionales (mayor, menor, igual, diferente, etc.) Ejemplo: edad >= 18, cont < 100, etc.
  elif opcion==4:
      filename = "hola.txt"
      textfile = open(filename, "r")
      regex = "([A-za-z]\w*|\d\.?\d*)\s?(\>|\<|\>=|\<=|=|!=|\=\=)\s?([A-za-z]\w*|\d\.?\d*)"
      reg = re.compile(regex)
      for line in textfile:
          lista = reg.findall(line)
          print(lista)
      textfile.close()
# Cadenas de caracteres
  elif opcion==5:
      # este lo use para poner todos los signos de puntuacion
      result = string.punctuation
      filename = "hola.txt"
      textfile = open(filename, "r")
      regex = "\"[\w"+result+"\s]+"
      reg = re.compile(regex)
      for line in textfile:
          lista = reg.findall(line)
          print(lista)
      textfile.close()
  else:
    print("\la opcion es incorrecta")