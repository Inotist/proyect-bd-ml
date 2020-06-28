# Práctica del módulo de Deep Learning
Práctica desarrollada en local y posteriormente subida a Google Colab:

##### Notebook 1 - Carga de datos:
Para este notebook se necesitan los archivos *airbnb-listings.csv* y *was_loaded.npy* que se encuentran en esta misma carpeta del repositorio. <br>
[https://colab.research.google.com/drive/1Vn5jiuTF4ZK8gHutTl-tKHckedvNAbSr?usp=sharing](https://colab.research.google.com/drive/1Vn5jiuTF4ZK8gHutTl-tKHckedvNAbSr?usp=sharing)

##### Notebook 2 - Transformación de los datos:
Para este notebook se necesitan los archivos *train.csv*, *val.csv* y *test.csv* que se generan con el notebook 1. Los archivos con el mismo nombre que se encuentra en esta carpeta del repositorio ya han pasado por este proceso de transformación. <br>
[https://colab.research.google.com/drive/1FJvbWQoW58B25-0D08YWvcfjc3eUudXt?usp=sharing](https://colab.research.google.com/drive/1FJvbWQoW58B25-0D08YWvcfjc3eUudXt?usp=sharing)

##### Notebook 3 - Generación de modelos:
Para este notebook se necesitan los archivos *train.csv*, *val.csv* y *test.csv* que se generan con el notebook 2 y que también se encuentran en esta misma carpeta del repositorio. También hace falta el archivo [*images.npy*](https://drive.google.com/file/d/17SMynjOAXvaEStb4Lf9Hen_kR8zIWBrH/view?usp=sharing), que pesa 2GB y por eso no se ha subido al repositorio, pero se puede [descargar aquí](https://drive.google.com/file/d/17SMynjOAXvaEStb4Lf9Hen_kR8zIWBrH/view?usp=sharing) <br>
[https://colab.research.google.com/drive/1aHssW_j3DeX4qO5GneIY3ae7ZgOv3dVf?usp=sharing](https://colab.research.google.com/drive/1aHssW_j3DeX4qO5GneIY3ae7ZgOv3dVf?usp=sharing)

##### Notebook 4 - Variables descriptivas y RNN:
Para este notebook se necesitan todos los archivos que hacen falta para el 3º y también *train\_desc.csv*, *val\_desc.csv* y *test\_desc.csv*.
[https://colab.research.google.com/drive/1TSH_kCgY0YgEAy-co7pfwfl6kN0BdHpK?usp=sharing](https://colab.research.google.com/drive/1TSH_kCgY0YgEAy-co7pfwfl6kN0BdHpK?usp=sharing)

##### Funciones de pérdidas y métricas utilizadas en mis modelos:
Olvidé explicar esta parte en los notebooks, pero básicamente utilicé la entropía cruzada (cross entropy) como función de pérdidas para el problema de clasificación, ya que estamos tratando con probabilidades, y como métrica utilizé la precisión (accuracy) para conocer la tasa de aciertos del modelo. Y en el caso de la regresión utilicé el error cuadrático medio (MSE) tanto para la función de pérdidas como para la métrica, ya que lo que buscamos en este caso es hacer una estimación y la mejor manera de puntuar el resultado es viendo cuánto se aleja dicha estimación de la realidad.