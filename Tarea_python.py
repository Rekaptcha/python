"""A. ALGUNAS OPERACIONES SENCILLAS."""
"""A.1. Redondeo de la hora. Redondear la hora despreciando los minutos."""

def redondeo_hora(hora):
    hora = hora.split(":")
    hora_redondeada = hora[0]
    return hora_redondeada

#Una opción todavía más simple:
def redondeo_hora(hora):
    return (hora[0:2])
  
##Pruebas:
print(redondeo_hora('12:48'))
for h in ['15:00', '23:15', '14:22']:
  print(redondeo_hora(h))
  

"""A.2. Rangos de edad. Codificar los rangos de edad, asignando a cada rango descrito un intervalo de dos enteros."""
def rango_edad(c):
	if (c == "DE 25 A 29 AÑOS"):
  		return '(25, 29)'
	elif (c == "MAYOR DE 74 AÑOS"):
  		return '(75,100)'
	else:
  		return 'DESCONOCIDA'
    
#Pruebas:
for c in ['DE 25 A 29 AÑOS', 'DESCONOCIDA', 'MAYOR DE 74 AÑOS']:
    print(c, " -> ", rango_edad(c))


"""A.3. Lesividad. Datos en blanco. """
#Los datos de lesividad están codificados con un número, deseamos convertirlo en un entero. Si no se requiere asistencia sanitaria, un 0. Si la lesividad no se conoce (faltan datos) también un 0.
def lesividad(c):
	if bool(c): #Comprobamos que la variable no está vacía, para que no falle cuando haga la conversión a int
    		d = int(c) #Hacemos el casteo del valor a int
		if d >=1 and d <=77:
			return(d)
	else:
		d = 0
		return(d)

#Pruebas:
for c in ['01', '02', '14', '', '77']:
	print(c, "->", lesividad(c))
    
    
 """A.4. Operaciones con una línea de datos """
#Operar con una línea del archivo separando sus piezas, extrayendo info que nos interese, aplicando las funciones de lesividad, redondeo_hora y rango_edad

def presentar_peraciones_basicas(linea):
    print("La cadena de entrada: ")
    print(linea)
    print()
    print("Piezas: ")
    linea_partida = linea.split(";")
    print(linea_partida)
    print()
    print("Distrito: ")
    print(linea_partida[5])
    print()
    print("La hora, sin y con redondeo: ")
    print(linea_partida[2])
    print(redondeo_hora(linea_partida[2]))
    print("La edad, tal como viene y en su rango: "):
    print(linea_partida[10])
    print(rango_edad(linea_partida[10])

def extraer_datos(linea):
    linea_partida = linea.split(";")
    hora_redondeada = redondeo_hora(linea_partida[2])
    distrito = linea_partida[5]
    tiempo = linea_partida[7]
    edad = rango_edad(linea_partida[10])
    grado_lesividad = lesividad(linea_partida[12])
    datos_extraidos = [hora_redondeada, distrito, tiempo, edad, grado_lesividad]
    return datos_extraidos
 
#Pruebas funcionamiento:
print(len(linea_9.split(;)))
print(extraer_datos(linea_9))

          
#   --------------------------------------------------------------------------------------------------------
#   --------------------------------------------------------------------------------------------------------          
          
"""B. LECTURA DE DATOS DEL ARCHIVO."""
"""B.1. CABECERA. Leer la cabecera del archivo de datos (la primera línea) y descomponerla en rótulos par cada una de las columnas."""
def cargar_cabecera(archivo):
    with open(archivo, 'r') as f:
        cabecera = f.readline()
        cabecera = cabecera.strip()
        cabecera = cabecera.split(";")
        return cabecera

#Pruebas funcionamiento:
cabecera = cargar_cabecera("2020_Accidentalidad.csv")
print(cabecera)

"""B.2. Lectura de algunas líneas del archivo."""
#Leer los datos a partir de la cabecera, saltandonos la primera línea con next.
def cargar_lineas(archivo,inicio = 1,fin = 11): 
    f = open(archivo, "r")
    count = 1
    lista = []
    for x in f:
        if count >= inicio+1 and count <= fin+1:
            lista.append(extraer_datos(x))
        count += 1
    return lista
          
###Pruebas funcionamiento: 
lineas_lista = cargar_lineas("2020_Accidentalidad.csv",1, 4)

###Pruebas funcionamiento: Si no le decimos qué líneas nos interesan, se cargarán por defecot las 10 primeras.
for linea in lineas_lista:
    print(linea)

lineas_lista = cargar_lineas("2020_Accidentalidad.csv")
          

""" B.3. Lectura de todas las líneas del archivo. """
#Cargar todos los datos de un archivo, excluyendo la cabecera. Que el resultado se de en una lista, cada elemento recoja la información de una línea del archivo de datos, sin la cabecera, pero incluyendo todas las líneas, sin opción a cuáles interesan.

def cargar_datos(archivo): 
    f = open(archivo, "r")
    cabecera = 1
    lista = []
    for x in f:
        if cabecera == 1:
            cabecera = 0
        else:
            lista.append(extraer_datos(x))

    return lista

#Prueba funcionamiento:
datos_lista = cargar_datos("2020_Accidentalidad.csv")

for linea in datos_lista:
    print(linea)
          
#Prueba de funcionamiento 2: (revisar porque creo que esta prueba de funcionamiento no se llegó a probar)
for linea in datos_lista[0:4]:
          print(linea)


#   --------------------------------------------------------------------------------------------------------
#   --------------------------------------------------------------------------------------------------------          
"""C. ACCIDENTALIDAD Y MORTALIDAD POR EDAD """      
"""C.1. Accidentalidad. Cómputo básico."""
#Se desea totalizar el número de accidentes de la tabla por rango de edad. Usa un diccionario en el que la clave es el rango de edad y el valor el total de accidentes para ese rango de edad. Cada accidente actualiza el diccionario tal que, si el rango de edad no está, se añade con un total de un accidente, si ya está, se añade una unidad más al total de accidentes de dicho rango. Con un diccionario con el valor 0 por defecto. 

 def totales(datos_lista):
    for linea in datos_lista:
        diccionario_accidentes = {}
        x = datos_lista[4]
        if x in diccionario_accidentes.keys():
            diccionario_accidentes[x] = diccionario_accidentes[x] + 1
        else 
            diccionario_accidentes.update({x : 0})
          
##Añadir que 0 sea el valor por defecto?
##Pruebas de funcionamiento:
total_accidentes_por_edades = totales(datos_lista)

for k, e in total_accidentes_por_edades.items()
          print(k, e)
          
          
"""C.2. Accidentalidad con mortalidad"""

          
          
#   --------------------------------------------------------------------------------------------------------
#   --------------------------------------------------------------------------------------------------------          
          
"""D. ALGUNAS GRÁFICAS."""
"""D.1. Un modelo de gráfica."""
##Diseñar un modelo de gráfica que tome como parámetro una lista de pares (x,y) y 3 rótulos explicativos opcionales que necesitamos incluir. Y que las etiquetas de las abcisas aprezcan inclinadas.

def representar_xxx_yyy (x, y, rotulox, rotuloy, titulo):
	import matplotlib.pyplot as plt
	plt.xlabel(rotulox)
	plt.ylabel(rotuloy)
	plt.title(titulo)
	plt.xticks(rotation=-30)
	plt.plot(x, y)
	plt.grid()
	plt.show()

##Pruebas de funcionamiento:
representar_xxx_yyy([])
representar_xxx_yyy([])

"""D.2. Tasas de muerte por edades."""
"""D.3. Tasas de muerte por rangos horarios."""



#   --------------------------------------------------------------------------------------------------------
#   --------------------------------------------------------------------------------------------------------          
"""E. OPERACIONES CON DATAFRAMES """ 
"""E.1. Carga del dataframe """
def cargar_dataframe_v0(archivo):
	import pandas
	dataframe = pandas.read_csv(archivo)  
	return dataframe
	  
#Prueba de funcionamiento:
tabla_pre = cargar_dataframe_v0("2020_Accidentalidad.csv")
print(tabla_pre)
	  
"""E.2. Carga del dataframe, codificano rangos de edad y lesividad """
##Modificando la lectura del dataframe para que los rangos de edad se conviertan en el intervalo correspondiente, que en el apartado de lesividad (cuyos campos en blanco se han traducido a NaN (Not A Number9 se ponga como entero tal que: 1 cuando hay lesividad y 0 cuando no se conoce la lesividad o no hay lesividad (casos codificados con un 0, un 77, un 14).

	  
"""E.3. Tabla de número de accidentes por rangos de edad """
##Devolver una tabla con dos columnas (rango edad y nº de accidentes), formando una tabla nueva. En orden ascendente de rango de edad.

def extraer_columnas(dataframe):
          dataframe_2col = dataframe[['RANGO DE EDAD', 'LESIVIDAD']]
	  dataframe_ordenado = dataframe_2col.sort_values(by='RANGO DE EDAD', ascending=True)
	  return dataframe_ordenado

tabla_accidentalidad= cargar_dataframe("2020_Accidentalidad.csv")
accidentalidad_v2 = extraer_columnas(tabla_accidentalidad)
print(accidentalidad_v2 = extraer_columnas(tabla_accidentalidad))
	  
	  
#Descartar el rango de edad (-1, -1) que no interesa. Descartar esa fila.

def

"""E.4. Accidentes con consecuencias médicas """
"""E.5. Unión de dos tablas """
"""E.6. Proporción de accidentes con lesiones """
"""E.7. Gráfico """

#   --------------------------------------------------------------------------------------------------------
#   --------------------------------------------------------------------------------------------------------          
"""F. UN CÁLCULO MASIVO CON MAP-REDUCE """ 

#   --------------------------------------------------------------------------------------------------------
#   --------------------------------------------------------------------------------------------------------          
"""G. APARTADO LIBRE """ 
##¿Pequeño ejercicio con NLTK, quizás? 
	  
#   --------------------------------------------------------------------------------------------------------
#   --------------------------------------------------------------------------------------------------------          
"""COMENTARIOS DE EVALUACIÓN""" 
#Ayuda recibida y fuentes utilizadas: Stackoverflow, W3SCHOOLS, python.org/doc, matplotlib.org, pythonchallenge, learnpython.org
#scipy.org
