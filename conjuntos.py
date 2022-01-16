### CONJUNTOS en PYTHON ###

""" ---- --- -- CONJUNTOS -- --- ----"""
""" Un conjunto es una colección de elementos sin orden ni repetición. Las operaciones básicas de conjuntos permiten crear un conjunto, calcular la unión, la intersección, la diferencia y la diferencia simétrica """

#Creación de un conjunto, entre {}
conjunto1 = {"a", "e", "i", "o", "u"}
conjunto2 = set("abracadabra") 

#El output del conjunto 2 es = {'a', 'b', 'c', 'd', 'r'} Aunque la letra a aparece repetida varias veces en la palabra, en el conjunto sólo se almacena una vez, y las consonantes aparecen desordenadas, dado que los elementos de un conjunto no tienen NI ORDEN NI REPETICIÓN.

"""OPERACIONES entre CONJUNTOS"""
#Cálculo de la unión entre dos conjuntos
conjunto1 | conjunto2
#Output: {'a', 'b', 'c', 'd', 'e', 'i', 'o', 'r', 'u'}
#Esto mismo se puede calcular con notación orientada a objetos: conjunto1.union(conjunto2)

#Cálculo de la intersección entre dos conjuntos
conjunto1 & conjunto2
#Output: {'a'}
#Esto mismo se puede calcular con notación orientada a objetos: conjunto1.intersection(conjunto2)

#Cálculo de la diferencia simétrica entre dos conjuntos (los elementos que pertenecen a un conjunto pero no al otro)
conjunto1 ^ conjunto2
#Output: {'b', 'c', 'd', 'e', 'i', 'o', 'r', 'u'}
#Esto mismo se puede calcular con notación orientada a objetos: conjunto1.difference(conjunto2)

#Averiguar si un elemento pertenece a un conjunto o no
valor in conjunto
#Esto mismo se puede calcular con notación orientada a objetos: conjunto1.issubset(conjunto2)

"A" in conjunto1
#Output: False

"a" in conjunto1
#Output: True

#El método add permite añadir un elemento a un conjunto
conjunto.add(elemento)
conjunto1.add("A")
#Output: {"A", "a", "e", "i", "o", "u"}

#El método remove permite eliminar un elemento de un conjunto
conjunto.remove(elemento)
conjunto1.remove("A")
#Output: {"a", "e", "i", "o", "u"}


"""Notación intensional o por comprensión en CONJUNTOS"""
#Ejemplo función que calcula los divisores de un número
def divisores(n):
  """pre: n > 0 """ #El número ha de ser positivo
  return {d for d in range(2, n+1) if n % d == 0}
#Nos devuelve un conjunto de todos los divisores, al que le podemos aplicar una función
max(divisores(24))
