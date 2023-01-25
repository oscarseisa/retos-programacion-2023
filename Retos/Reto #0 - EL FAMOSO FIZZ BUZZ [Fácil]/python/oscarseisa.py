"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

numero = 0

while numero <= 99:
  numero += 1

  #Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"

  if numero % 3 == 0 and numero % 5 == 0:
    print("fizzbuzz")

  #Múltiplos de 3 por la palabra "fizz".

  elif numero % 3 == 0:
    print("fizz")

  #Múltiplos de 5 por la palabra "buzz"

  elif numero % 5 == 0:
    print("buzz")

  #Si no se cumplen las anteriores, imprime número

  else:
    print(numero)
