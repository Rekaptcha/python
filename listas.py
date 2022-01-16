###### LISTAS EN PYTHON ###### COMPLETO
"""Una lista es una secuencia de datos"""
lista_datos = ["Nombre", edad, estatura, ["Hobby1", "Hobby2"]]
#Permite almacenar diferentes tipos de datos, y otras lisats dentro de sí misma.
#Comienza a indexarse por el número 0
print(lista_datos[0])
#Output: Nombre

#Para acceder a elemento de una lista que se encuentra dentro de otra lista, debo especificar las posiciones de ambos.
print(lista_datos[3][1]) #Accedemos al tercer elemento de lista_datos y al segundo elemento de ese item
#Output: Hobby2

#El método len devuelve la longitud de la lista de datos
print(len(lista_datos))

#Recorrer todos los valores de una lista:
for i in range(len(lista_datos)):  #Usamos i como índice, y con len recorremos como rango el tamaño de la lista
  print(lista_datos[i])

for elem in datos_lista:  #Recorre directamente los elementos de una lista sin referirse a los índices, más simple
  print(elem) #Para cada valor ejecutará el comando
  
  
#EJEMPLO:
def media(numeros):
    suma = 0.0
    for x in numeros:
      suma = suma + x
    return suma / len(numeros
                      
numeros = ([1.0, 2.0, 3.0, 4.0])
                  
                      

"""Listas INTENSIONALES"""
#Una forma alternativa a definir las listas por extensión (definiendo cada uno de sus elementos) es crear listas intensionales (dar una descripción genérica de los elementos)
[(i, i**2) for i in range(min, max)] #Lista formada por cada número y su cuadrado, donde cada número recorre el rango de min hasta max

#Ejemplo:
[(i, i**2) for i in range(2, 10)] 
[(2,4), (3,9), (4,16), (5,25), (6,36), (7,49), (8,64), (9,81)]

#El for es el generador, además del generador podemos usar un filtro con un if, filtramos solamente aquellos casos del generador que cumplen una condición
[(i, 120//i) for i in range(1, 120+1) if 120 % i == 0])  #Lista de cada factor hasta 120 y el factor que lo complementa hasta llegar a 120
#Output: [(1,120), (2,60), (3,40)...]  Sólo almacena aquellos valores cuyo resto = 0, esto es, son divisores de 120

#Se pueden usar varios generadores combinados entre sí y varios filtros
[(i, j) for i in range(10) for j in range(i) if i % 4 == 0 if j > 3])
#Output: [(8,4), (8,5), (8,6), (8,7)]


"""OPERACIONES con LISTAS""""
#Añadir un valor a la lista
#El método append permite añadir un valor al final de una lista
lista = [1, 2, 3, 4, 5]
lista.append(6)
#Ahora lista = [1, 2, 3, 4, 5, 6]

#Las operaciones que trabajan modificando el propio parámetro con el que trabajan se llaman operaciones in place porque trabajan en el propio lugar en el que está definida esa lista.
#La notación de estas operaciones es además OO (Orientada a objetos), porque se pone el objeto en primer lugar  objeto.operacion(dato)
#En lugar de llamarse operación, por la notación orientada a objetos se va a llamar método, y lo que recibe es un parámetro. El objeto lista admite el método append con el parámetro que le indiquemos. Trabaja in place porque la lista ha sido modificada en el propio lugar de la memoria en que haya sido situada

#El método count cuenta cuantas veces aparece un valor en la lista
lista.count(dato)
lista.count(4)
#Output: 1

#El método extend amplia los valores de una lista por la derecha con los de otra 
lista.extend([lista])
lista.extend([0,0,0])
#Output: [1, 2, 3, 4, 5, 6, 0, 0, 0]

#El método index devuelve la posición de un valor, un elemento, en la lista (la primera aparición del elemento)
lista.index(indice)
lista.index(6)
#Output: 5

#El método insert permite añadir un elemento a la lista dentro de una posición concreta
lista.insert(posicion)
lista.insert(3, 333)
#Output: [1, 2, 3, 333, 4, 5, 6, 0, 0, 0]

#El método pop permite eliminar un elemento de la lista. Si no se le indica ninguna posición, elimina el último por la derecha, también devuelve el valor de ese objeto, se podría hacer x = pop() para sacarlo y almacenarlo en una variable
lista.pop()
#Output: [1, 2, 3, 333, 4, 5, 6, 0, 0]

#Para eliminar un elemento en una posición concreta, simplemente se lo pasamos como parámetro:
lista.pop(posicion)
lista.pop(3)
#Output: [1, 2, 3, 4, 5, 6, 0, 0]

#El método sort permite ordenar una lista in place
lista.sort(key=None, reverse=False) #Valores por defecto

lista= [ 'Lee Sin', 'Lux', 'Nidalee', 'Kayn', 'Hecarim']
lista.sort()
#Output: ['Hecarim', 'Kayn', 'Lee Sin', 'Lux', 'Nidalee']  Aparecen ordenados alfabéticamente.

#Puede ordenar en sentido inverso 
lista.sort(reverse=True)
#Output: ['Nidalee','Lux','Lee Sin','Kayn', 'Hecarim']

#Por defecto ordena alfabéticamente (en caso de números, de menor a mayor), pero se pueden usar todo tipo de filtros de ordenación
lista.sort(key=len)
#Output: ['Lux', 'Kayn',...] Ordena los nombres atendiendo a la longitud del string
lista.sort(key=len, reverse=True) #Etc...

### Todos estos métodos son in place, modificando la propia lista. A continuación se muestran otros métodos que no modifican la lista in place ###

""" MÉTODOS que no funcionan IN PLACE """
sorted(lista)
#Devuelve los elementos de la lista ordenados pero no los modifica, simplemente los muestra así una vez. Se calcula y se puede guardar el resultado en una nueva variable sin que ninguna de las listas interfiera sobre la otra
lista2 = sorted(lista)


