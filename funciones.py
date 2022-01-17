"""FUNCIONES en PYTHON""" #COMPLETO
"""Una función es un bloque de código que se ejecuta cada vez que se llama desde el código, evitando repeticiones de código innecesarias y posibilitando una organización del código más comprensible y limpia."""

#Las funciones en Python se definen usando la keyword ''def'':
def nombre_funcion():
  #código a ejecutar por la función

#Pueden recibir datos externos, conocidos como parámetros, para realizar sus operaciones. Los parámetros se especifican a continuación del nombre de la función, entre paréntesis. Pueden añadirse tantos argumentos como se desee, separados entre sí por comas:
def nombre_funcion(parámetro):
  #código a ejecutar por la función

def nombre_funcion(parámetro1, parámetro2):
  #código a ejecutar por la función, en el cuerpo de la definición

#Ejemplo:
def suma(num1, num2):
  num3 = num1+num2
  return num3

#Para llamar a una función basta con escribir su nombre seguido de paréntesis:
nombre_funcion()

#Podemos llamar a una función todas las veces que deseemos en el código.
#En el caso de las funciones que reciben parámetros:
nombre_funcion(parámetro)

#Ejemplo:
nombre_funcion(7, 3)
#Output: 10

#En cada llamada, los parámetros abstractos, también conocidos como formales, asumen los valores de los paráetros concretos, también llamados reales, y entonces se ejecuta el cuerpo de la función.
#Existe una diferencia a nivel de nomenclatura para los parámetros: llamamos parámetros a las variables listadas dentro de los paréntesis en la definición de la función, y argumentos al valor concreto que se le pasa a la función cuando se llama.

#Si una función se ha definido con un número concreto de parámetros, y no recibe tantos parámetros o recibe menos, dará error. Si no sabemos cuántos argumentos le pasaremos a una función, debemos añadir * delante del nombre del parámetro en la definición de la función, para qeu la función reciba una tupa de argumentos.
def nombre_funcion(*parámetro):
  #códio a ejecutar por la función
  
nombre_funcion(1, 2, 3)

#Keywords

#Definir parámetros por defecto

#Return values. Con return podemos especificar qué valores devuelve la función

#Es importante poner comentarios para documentar qué realiza cada función. La estructura de los comentarios, por convención suele ser:
"""
----
Descripción de lo que hace la función
----
Parámetros
----
Tipo que deben tener los parámetros de entrada, número y orden de parámetros que recibe:
  Parámetro1:
  Blablabla. Papel que juegan los parámetros de entrada
----
Return
-----
Qué devuelve y de qué tipo es lo que devuelve
-----
Ejemplo de uso
-----
"""

#Prerrequisitos de una función. En la documentación, en el apartado de precondition, se especifican cuáles son los requisitos que deben cumplir los parámetros de una función para que pueda garantizarse su correcto funcionamiento.
"""A continuación del apartado de parámetros de la documentación, se añade un apartado Precondition
Precondition
------------
Especificamos la precondición para poder utilizar la función
"""

#Para imponer una precondición, recurrimos a assert.
assert variable 
assert num1 > 0

#Lo primero que hará la función es comprobar si se cumple la precondición o no, si no se cumple, se puede imprimir un mensaje de error personalizado por pantalla:
assert variable, "Mensaje de error"

assert num1 => 0, "El num1 no es mayor o igual a 0"
