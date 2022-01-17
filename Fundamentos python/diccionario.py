"""---- --- DICCIONARIOS en PYTHON --- ----  """ #COMPLETO
"""Un diccionario, también llamado memoria asociativa, es parecido a un array o a una lista. En lugar de dar información del elemento a partir de un índice (la posición), devuelve la información a partir de una clave cualquiera. En los arrays o listas la key siempre es la posición del elemento, su índice. En un diccionario, la definimos nosotros (puede ser un number, un string..). Son dos valores asociados. """

###Definir un diccionario:
#Definimos un conjunto de asociaciones, en el ejemplo, si decimos Lee Sin, nos devuelve jungla, si ponemos Leona, support
diccionario = {clave : valor, clave2 : valor2}
lolChamps = {"Lee Sin" : "jungla", "Leona" : "support" }

print(diccionario) #Devuelve toda la info contenida en el diccionario
#Output: {clave : valor, clave2 : valor2}

print(diccionario[clave]) #Devuelve la información asociada a esa clave, ese par clave-valor.
print(lolChamps["Lee Sin"])
#Output: "Jungla"

##Añadir un elemento al diccionario:
diccionario["clave"] = valor
lolChamps["Orianna"] = "mid"

print(lolChamps)
#Output: {"Lee Sin" : "jungla", "Leona" : "support", "Orianna" : "mid" }

#Si buscamos una clave que no se encuentra en el diccionario, dará error.
#Para saber si una clave se encuentra almacenada en un diccionario, usamos:
clave in diccionario

"Lee Sin" in diccionario
#Output: True

"Veigar" in diccionario
#Output: False


#Para ver la lista de claves de un diccionario
diccionario.keys()
#Output: dict_keys(['Lee Sin', 'Leona', 'Orianna'])

#Podemos almacenar los resultados en uan lista
list(diccionario.keys()) #Obtenemos una lista con las claves del diccionario

#Para ver la lista de valores de un diccionario
diccionario.keys()
list(diccionario.keys()) #De igua forma para almacenar las claves del diccionario en una lista

#Para obtener claves y valores de un diccionario:
diccionario.items()
list(diccionario.items()) #Así se obtienen pares clave-valor no como memoria asociativa sino como una simple lista de claves

list(lolChamps.items()) 
#Output [('Lee Sin', 'jungla'), ('Leona', 'support'), ('Orianna', 'mid')]


"""Recorrer un DICCIONARIO"""
#Para cada una de las claves imprimimos la key y el valor del diccionario asociado a esa key
for item in diccionario:
  print(item, diccionario[item])
  
for champion in lolChamps:
   print(champion, lolChamps[champion])
    
for item, elemento in diccionario.items():
   print(item, elemento) ##Obtenemos el mismo resultado, permitiendo ver la flexibilidad del recorrido de los diccionarios

"""DICCIONARIOS COMPLEJOS"""
#A los valores de un diccionario se le pueden asignar estructuras más complejas, como otros diccionarios
diccionario = {"Clave1": {"subclave1" : valor,
                          "subclave2" : valor
                          },
               "Clave2":  {"subclave1" : valor,
                           "subclave2" : valor
                          }
              }
#Es un diccionario y los valores de cada clave de este diccionario son a su vez, diccionarios
for elemento in elemento:
  print(elemento + "es un valor de" + diccionario[elemento]["subclave2)


for champion in lolChamps:
  print(champion + " juega en " + lolChamps[champion]["subclave1"])

    
