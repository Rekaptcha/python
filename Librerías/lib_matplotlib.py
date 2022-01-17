###### LIBRERÍA MATPLOTLIB ####### COMPLETO
"""Librería de trazado de gráficos que genera figuras de diversos tipos y formatos con gran calidad """

#### IMPORTACIÓN LIBRERÍA ####
import matplotlib.pyplot as plt ###Importamos la librería y la llamamos genéricamente plt de plot, nos permite manejar un identificador más corto a la hora de referirse a ella
plt.plot([array_y])

#Función lineal
plt.plot([1, 2, 3, 4]) #Creamos un gráfico cuyos valores de las coordenadas (verticales) serán 1, 2, 3, 4
plt.ylabel('Etiquetay') #Añade una etiqueta en el eje de las y
plt.xlabel('Etiquetax')
plt.title('Etiqueta título')
plt.show() #Muestra la figura definida

#Si sólo le pasamos como argumento 1 array a la función plot, asume que es una secuencia de valores y (ordenadas), generando los valores x automáticamente.
###Los arrays en python comienzan con 0, por tnato el vector x que ha generado por defecto tiene la misma longitud que el vector y pero en lugar de comenzar por 1, comenzará por 0, yendo de 0.0 a 0.3 (sería como si hubiésemos definido para x [0, 1, 2, 3]

plt.plot([array_x], [array_y])


#Como tercer argumento se le puede pasar un string que indica el color y el tipo de línea del plot. Las letras y símbolos del formato provienen de MATLAB, se puede concatenar un string de color con un string de tipo de línea. El formato por defecto es 'b-' (una línea azul sólida). Con 'ro' podemos crear círculos rojos.
plt.plot([array_x], [array_y], 'formato') #Creamos una función cuadrática (de segundo grado)
plt.plot([array_x], [array_y], 'ro') # r = red, o es bola, representará los valores en bolas rojas

plt.ylabel('Etiqueta') #Añade una etiqueta en el eje de las y
plt.xlabel('Etiqueta') #Añade una etiqueta en el eje de las x

"""El método plt.plot puede recibir tanto arrays de valores como pares de abcisas y sus ordenadas correspondientes para representar más de una gráfica """
#Numpy es una librería para usar arrays
points = np.linspace(10,100,100) #De 10 a 100, 90 pasos divididos en 100 pasos
def nlogn(x):
    return np.log(x) * x
plot.plot(points, np.log(points), points, points, points, nlogn(points)) ##Con numpy podemos aplicar una función a todos los puntos de un vector
plot.savefig('./figuras/plot.png', dpi=600) #Guardamos la figura en un archivo de disco, hay que hacerlo antes de mostrarla, una vez mostrada se libera de la memoria y ya no puede ser mostrada, debe ser previo al show


"""Gráficas con distinto formato en una misma representación"""
plt.plot([array_x], [array_y], 'formato', [array_x2], [array_y2], 'formato2') 
#Formato realmente es (color,forma), 'r--' = guiones rojos, 'bs' = blue square, 'g^' = green triangles..
#Cada gráfica viene dada por un conjunto de valores en las abcisas, en las ordenadas y su formato específico

"""Encapsular una gráfica en una función"""
##Una función de grado superior tiene como parámetro el nombre de una función genérica:
def my_graph(formula, x_range):
  x = np.array(x_range)
  y = formula(x)
  plt.pot(x,y)
  plt.show()
  
def formula(x)
  return x***3 - 50*x

def my_graph()
  graph(my_formula, range(-7,8))

my_graph()


"""Gráfico de dispersion"""
#Hay que definir el número de puntos que tendrá el gráfico de dispersión
n = 50
x = np.random.rand(N) #Generamos las abcisas de forma aleatoria
y = x + 10 * np.random.randn(N) #Generamos las ordenadas en base a las abcisas
color = np.random.randint(0, N, N) #Color generado aleatoriamente
tamano = np.as(np.random.randn(N)) * 250 # Tamaño generado aleatoriamente

plt.scatter(x, y, c=color, s=tamano, alpha = 0.5) #Se dibuja con scatter que es el nombre en inglés de dispersión
#plt.scatter(vector_x, vector_y, vector_colores, vector_tamaños, alpha (nivel de transparencia de los colores))
#help(plt.scatter)

"""Generar varias gráficas simultáneas pero separadas visualmente"""
#Para ello generamos subplots, por ejemplo, de un Array de 2*1 (dos filas, 1 columna cada una). Con los subpots generamos cada uno de ellos por separado y los podemos ver conjuntamente.
plt.subplot()
plt.plot()
plt.subplot()
plt.plot()


"""ANOTACIONES"""
#Con el método annotate podemos introducir anotaciones para definir puntos concretos del gráfico, se puede modificar la flecha de la anotación y las características del texto asociado (posición, color...).

plt.annotate('etiqueta_anotacion', xy=(X, Y)...)

"""Función de dos variables"""
#Se puede representar en dos dimensiones un gráfico. En lugar de representarla mediante un gráfico tridimensional, se opta por representar en dos dimensiones en la que segunda variable solamente toma una colección pequeña de variables, y para cada uno de los valores se da un color diferente, aparecen una pequeña colección de funciones que puede mostrar cómo funciona esta variable.
def f(z, t):
    return np.exp(-z)*np.sin(t-z)

z = np.linspace(0, 5, 3001)
t = np.arrange(0, 40000, 4000)
for tval in t:
    plt.plot(z, f(z, tval
plt.show()

"""Diagrama de barras"""
#Para crear un diagrama de barras se recurre al método bar. 
plt.bar()
                  
"""Definiendo los ejes, modificadores de los ejes"""
#Para customizar los ejes de abcisas y ordenadas de nuestros gráficos recurrimos a las funciones xticks e yticks
plt.xticks()
plt.yticks

#Para especificar, por ejemplo, el nombre de los ticks:
objects = ('Python', 'C++', 'Java')
plt.xticks(objects)
                  
#Mejor aún: Como objects es un array de elementos, podemos obtener su longitud y determinar la longitud de las abcisas que tenemos a partir de ellas, es decir, el numero de ticks:
y_pos = np.arrange(len(objects))
plt.xticks(y_pos, objects)
                  
#Para un diagrama de barras horizontal, modificamos xticks por yticks:
plt.yticks(y_pos, objects)                  

                  
"""Diagramas de barras conjuntos"""
#Permiten comparar características dos grupos comparándolas en diferentes elementos.
#Simplemente creamos dos plt.bar antes del plt.show
n = 4
grupo1 = (1, 2, 3, 4)
grupo2 = (2, 3, 5, 1)

fig, ax = plt.subplots()
index = np.arrange(n_groups)
ancho_barra = 0.35 
grafico1 = plt.bar(index, grupo1, ancho_barra)
grafico2 = plt.bar(index + ancho_barra, grupo2, ancho_barra) #Desplazamos el indice con el ancho de barra

"""Añadir una leyenda"""
plt.legend()
                  
"""OTROS PLOTS DE LOS QUE DISPONE MATPLOTLIB"""
##Linea plot
##Multiple subplots in one figure
##Images
##Contouring and pesudocolor
##Histograms
##Paths
##Three-diemnsional plotting
##Streamplot
##Elipses
##Bar charts
##Pie charts
##Tables
##Scatter plots
##GUI widgets
##Filled curves
##Date handling
##Log plots
##Polar plots
##Legends
##TeX-notation for text objects
##Native TeX rendering
##EEG GUI
##XKCD-style sketch plots
##Subplot example

www.matplotlib.org


