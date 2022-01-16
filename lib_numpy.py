#####Librería NUMPY #### 
"""Paquete adecuado para cálculos numéricos eficientes, permite manejar arrays multidimensionales homogéneos (cuyos componentes son del mismo tipo), ofrece herramientas para integrar código pearson con c++, gestión de nº aleatorios.... y un largo etcétera. """

###### NUMPY. 1º STEP ######
"""El primer paso para trabajar con Numpy es IMPORTAR la librería. """

import numpy as np # La hemos llamado np, por abreviar y trabajar más cómodamente.



###### ARRAYS ### Para trabajar con arrays se debe tratar de un array de datos homogéneo (todos los datos son del mismo tipo: enteros, float...)
""" Crear un array de la librería np con dos listas, son dos filas cada una de 3 elementos. Será un array bidimensional de 2*3 reales. """
a = np.array([[1., 2., 3.],
              [4., 5., 6.]
              ])

print(a.ndim, a.shape, a.dtype)

# El método ndim devuelve el número de dimensiones del array.
# El método shape devuelve la forma del array (filas, elementos). En el ejempo será un array 2*3
# El método dtype devuelve el tipo de sus elementos.

#Con dtype también podemos forzar que los elementos sean de un determinado tipo
b = np.array([1, 2], [3, 4]], dtype=complex)


#Para trabajar con arrays grandes o dando los componentes de forma genérica se puede trabajar de diferentes maneras:
""" A partir de rangos de arrays """ 
a = np.arrange(12) # Se crea un array mediante el rango de los números del 0 al 11, los 12 primeros números naturales partiendo del 0.

""" Podemos reformar el array introduciendo los elementos en una forma de array concreta, por ejemplo, 3*4 (3 filas de 4 elementos cada una) """
b = a.reshape(3,4)

#En a tendríamos lo que técnicamente se conoce como un vector y en b lo que se llama una matriz. El primero es unidimensional y el segundo bidimensional. 
#Con shape obtenemos la forma, a.shape = (12,) (la , indica que 12 no es solamente un nº sino que es la tupla formada por un sólo componente que es 12), y b.shape = (3, 4) 
# El método size devuelve el nº total de elementos con independencia de la forma que tenga. En ambos casos dará 12, a.size y b.size

# np.arrange(10000), se crea un array de 10.000 elementos.

"""Arrays definidos genéricamente donde los componentes son todos iguales"""
#Todo ceros:
b = np.zeros((3,4))

#Todo unos:
c = np.ones((2,3,4), dtype=np.int16)  #Esto es una hipermatriz, sus dimensiones son 2*3*4

#Array vacío:
d = np.empty( (2,3) )  #Array vacío 

#Con elementos seleccionamos aleatoriamente:
e = np.random.random((2,3))


"""Arrays definidos genéricamente con secuencias de valores"""
# Secuencias de valores:
f = np.arrange( 10, 50, 5 ) ##Con un rango de valores desde (inicio, fin, incremento). El límite del fin está excluido, el incremento indica de cuanto en cuanto se añade el valor, resultado: [10, 15, 20, 25, 30, 35, 40, 45]

#Secuencias, interpolando linealmente
g = np.linspace( 0, 2, 25 ) ##Con un límite inferior y superior interpolando linealmente (lim inf, lim sup, interpolacion), es decir, a distancais iguales (divide en 25 partes idénticas y ese sería el incremento)

from numpy import pi
h = np.linspace(0, 2*pi, 50) ##Desde 0 hasta 2 pi interpolando linealmente también.


"""Aplicar una misma función a todos los números del array"""
np.sin(nombre_array) #Se aplica la función seno a todos los puntos del array. Actúa sobre cada uno de los valores del array

#También se puede realizar con cualquier otra operación aritmética o función, por ejemplo:
print(nombre_array+1)  #Estamos sumando 1 a cada uno de los elementos del array 
print(nombre_array**2) #Eleva al cuadrado cada uno de los elementos del array
print(nombre_array<4) #O vemos si es menor que 4, elemento a elemento.

"""Operaciones entre arrays"""
#Se aplican todas las funciones elemento a elemento tomando un elemento de cada uno de los arrays de forma correspondiente
print(nombre_array1+nomber_array2)  #Ojo que se aplica elemento a elemento
print(nombre_array2*nombre_array2)

"""Calcular operaciones globalmente al array"""
print(a.sum(), a.prod(), a.min(), a.max()) #La suma de todos los componentes del array, el producto, el mínimo o el máximo de todso los componentes del array
print(a.sum(axis=0), a.sum(axis=1))
