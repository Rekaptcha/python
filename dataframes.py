""" DATAFRAMES EN PYTHON """
"""Un dataframe es una estructura bidimensional con filas y columnas. Una tabla de datos. Es el tipo de datos esencial de librería pandas"""


""" IMPORTANDO LA LIBRERÍA PANDAS """
import pandas

""" CONSTRUIR UN DATAFRAMSE  """
#Se puede construir un dataframe de muchas formas, una a través de un archivo .csv
dataframe = pandas.read_csv('archivo.csv')
realstate = pandas.read_csv('realstate.csv')
#Un archivo csv maneja fundamentalmente estas estructuras de tabla, con columnas que indican campos y filas que indican registros. Sus celdas son los valores asociados a dichos campos. Para cada fila tenemos varios campos (uno por columna). Por ejemplo, la tabla notas de alumnos tiene por filas a los alumnos, columnas las asignaturas y en celdas las notas de cada asignatura por alumno.

#Si visualizamos su tipo de datos:
type(dataframe)
#Output: pandas.core.frame.DataFrame 
#Dentro de la librería pandas, dentro del core, del módulo frame, se llama DataFrame al tipo de datos correspondiente a esta tabla

dataframe.info()
#Devuelve los tipos de datos correspondientes a cada una de las columnas. 
#RangeIndex: Nº filas (entries), de 0 a X
#Data columns: (total nº columnas):
#Columnas  y tipo de datos de las columnas (objeto, entero (int64) y decimales(float64))


""" ACCEDER A LOS ELEMENTO DE UN DATAFRAME """

""" ACCESO A LAS COLUMNAS """
#Para seleccionar una columna, accedemos como si fuese un índice.
dataframe['columnaNombre']
#Output: devuelve los distintos valores de esa columna junto a un índice asociado a cada uno de ellos.

#Se pueden seleccionar varias columnas simultáneamente.
dataframe[['columnaNombre1', 'columnaNombre2']]

#También se pueden seleccionar una colección de columnas especificando sus índices correspondientes. Las columnas empiezan por 0 igual que arrays, listas, etc.
dataframe.columns[i:j] #El último valor del índice como siempre se excluye

#Ejemplo:
setcols = notas.columns[2:6] 
setcols

#Output: muestra las columnas, 2 3, 4 y 5 (ojo que empieza por 0 y no por 1, la 2 es la ''3'')

#También se puede seleccionar un rango + una columna suelta
list(dataframe.columns[i:j]+['columnaNombre']

#Ejemplo:
mixed = list(selcols)+['Plástica']
mixed

#Output: las 4 columnas 2, 3, 4 y 5 y la columna Plástica
     
     
""" ACCESO A LAS FILAS """    
#Seleccionamos la fila haciendo mención al número correspondiente al a fila, con la función iloc
dataframe.iloc[i]

notas.iloc[2]
#Devuelve la fila 2 de la columna completa (también comienzan por 0)

#Seleccionar varias filas, especificando ambos índices:
dataframe.iloc[[i, j]]
#O con rangos
dataframe.iloc[i:j]


""" ACCESO A FILAS Y COLUMNAS """
#Se puede combinar la selección de filas y columnas a la vez:
dataframe.iloc[fila][columna]
notas.iloc[2]['Ingles']  # << Para obtener la nota en inglés del alumno cuya fila es la 2
notas.iloc[2][3] # Otra forma de referirse a la columna, tanto por índice como por valor

#Se pueden seleccionar conjuntos de columnas y filas
dataframe[[columnas]][filas]
dataframe[['columna1', 'columna2']][i:j]
dataframe[[i:j]][f:x]

notas[['Lengua', 'Ingles']][3:8] #Obtendriamos desde la fila 3 hasta la 7 las notas de lengua e inglés.


""" OPERACIONES SOBRE EL DATAFRAME """
#Ordenar las filas de la tabla de acuerdo a X criterios. 
#Seleccionar un campo y ordenarlo de forma ascendente o descendente:
dataframe.sort_values(by='columna1', ascending=True)
notas.sort_values(by='Ingles', ascending=False) #Ordenamos por las notas de inglés de forma descendente. 

#Establecer una condición para seleccionar las filas que cumplan dicha condición
dataframe['columna'] == X

cond = notas['Ingles'] == 5  #Vemos los que han sacado un 5 en inglés
cond #Devuelve el índice de las filas con True o False indicando si cumple o no la condición
     
dataframe[cond] ## Seleccionar de la tabla las filas que sí cumplen esa condición.

#Ejemplo de condición más compleja:
cond1 = notas['Ingles'] == 5
cond2 = notas['Fisica'] == 5
notas[cond1 & cond2]  #Obtener aquellas filas que cumplen ambas condiciones

##Contar cuántos elementos hay en la tabla (esto es, cuantas filas) agrupando 
