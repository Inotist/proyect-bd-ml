# Proyecto BD&ML
&nbsp;

## Idea general
Crear una aplicación web escalable que permita buscar apartamentos en Madrid en función de diversos factores que determinen la zona o entorno (contaminación, tasa de criminalidad, parques...) y el estilo de vida (bares, discotecas, museos, tipos de restaurante...).

## Nombre del producto
Living Madrid

## Estrategia del DAaaS
Voy a construir un datalake que me permita relacionar el dataset de airbnb con diferentes circunstancias de geolocalización utilizando herramientas Cloud que más adelante me permitan ir escalando en complejidad.

## Arquitectura
Arquitectura Cloud basada en Scrapy, Google Cloud Storage, Dataproc y Hive.

##### Crawler con scrapy que lee de las siguientes páginas:
- Yelp

```
Los scraps se realizarán mediante Cloud Functions.
```

Segmento de Google Cloud donde almacenar, en formato csv, todos los datasets y los datos que obtenga de los scraps, así como los resultados de su tratamiento.

Cluster temporal de Dataproc con Hive que accederá a los datos del segmento y creará una tabla por cada archivo csv que se necesite utilizar.

Cross Joins que crucen las coordenadas de los apartamentos de airbnb con las de otros lugares. El resultado será una nueva tabla con dos columnas que relacione por ID cada apartamento con aquellos lugares que se encuentran cerca.

Cross Join que cruce las coordenadas de los apartamentos de airbnb con los datos de contaminación, criminalidad, etc. El resultado será una nueva tabla de airbnb con nuevas columnas que indiquen el porcentaje de cada característica.

API REST local que se conecte con mi proyecto de Google Cloud y me permita, mediante una interfaz sencilla,  ejecutar Cloud Functions, levantar el clúster y ejecutar jobs con los datos que yo seleccione.

## Operating Model
Cada vez que actualice los datos usaré mi API para mantener actualizadas las relaciones.

Crearé una base de datos MariaDB con tablas basadas en mis csv y montaré una web que se conecte a la BBDD y que permita realizar búsquedas utilizando estos datos.

## [Diagrama](https://docs.google.com/drawings/d/1eZeSIpxanI0m5VTyS7f1ZGH6IZdZI5kj706luUgLsDg)