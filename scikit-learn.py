""" MACHINE LEARNING con SCIKIT-LEARN en PYTHON """
"""A partir de un conjunto n de datos, se plantea predecir el comportamiento de un dato desconocido, típicamente formado por varias características. Además de la regresión hay dos categorías fundamentales de técnicas para lograrlo: la clasificación supervisora y la no supervisora o clustering. También proporciona otras herramientas (model slection, preprocessing...) relacionadas con el aprendizaje de máquina"""

""" IMPORTAR LA LIBRERÍA """
from sklearn import datasets

#HERRAMIENTAS:
"""CLASIFICACIÓN SUPERVISADA"""
"""Partimos de un juego de observaciones X cuya categoría conocemos, y tratamos de predecir la categoría de una variable nueva usualmente llamada objetivo."""
#Usaremos el algoritmo de los nearest neighbors.
#Y el modelo de máquinas de soporte vectorial (SVM). Otro modelo de clasificación supervisada.

#El juego de datos iris identifica 3 tipos de datos iris: secosa, versicolor y virgínica. A partir de las longitudes y anchuras de los petalos. 


"""CLASIFICACIÓN NO SUPERVISADA"""
"""En la clasificación NO supervisada o clustering también conocemos un juego de observaciones de partida, pero su clasificación es desconocida para nosotros, el objetivo ahora es formar grupos de ejemplares de categorías similares. """
#Usaremos el algoritmo de los k-medias. K-Means.

https://www.youtube.com/watch?v=EMCZ1WodTrY&ab_channel=YoutubeUCM
