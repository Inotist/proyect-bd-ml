# Proyecto BD&ML
&nbsp;
![#f03c15](https://placehold.it/15/f03c15/000000?text=+) <span style="color:red">Se mostrará en rojo todo aquello que todavía no he implementado.</span>

## Idea general
Crear una aplicación web escalable que permita buscar apartamentos en Madrid en función de diversos factores que determinen la zona o entorno (contaminación, tasa de criminalidad, parques...) y el estilo de vida (bares, discotecas, museos, tipos de restaurante...).

## Nombre del producto
Living Madrid

## Estrategia del DAaaS
Voy a construir un datalake que me permita relacionar el dataset de airbnb con diferentes circunstancias de geolocalización utilizando herramientas Cloud que me permitan ir escalando en complejidad sin perder la facilidad de uso.

## Arquitectura
Arquitectura Cloud basada en Scrapy, Cloud Functions, Google Cloud Storage, Dataproc y Hive.

##### Crawler con scrapy que lee de las siguientes páginas:
- Yelp

```
Los scraps se realizarán mediante Cloud Functions para evitar problemas con la ip.
```

Segmento de Google Cloud donde almacenar, en formato csv, todos los datasets y los datos que obtenga de los scraps, así como los resultados de su tratamiento.

Cluster temporal de Dataproc con Hive que accederá a los datos del segmento y transformará selectivamente los csv en tablas, según las necesidades de cada sesión.

Joins que crucen las coordenadas de los apartamentos de airbnb con las de otros lugares. El resultado será una nueva tabla con dos columnas relacionando por nombre cada apartamento con aquellos lugares que se encuentran cerca.

![#f03c15](https://placehold.it/15/f03c15/000000?text=+) <span style="color:red">Join que cruce las coordenadas de los apartamentos de airbnb con los datos de contaminación, criminalidad, etc. El resultado será una nueva tabla de airbnb con nuevas columnas que indiquen el porcentaje de cada característica.</span>

API REST local que se conecte con mi proyecto de Google Cloud y me permita, mediante una interfaz sencilla,  ejecutar Cloud Functions, levantar el clúster y ejecutar jobs con los datos que yo seleccione.

## Operating Model
La api hará todo el trabajo por mí. Yo solo tengo que invocar a las funciones apropiadas y mi api se encargará de hacer el staging y el tratamiento de los datos:

- Primero el crawler se encarga de guardar un nuevo dataset en un directorio con la fecha del día actual.
- La función de staging recoge los datos más recientes de los datasets indicados y los copia en `input/`
- Una función se encarga de levantar el cluster.
- `send_job()` se encarga de administrar todas las tareas necesarias para realizar el tratamiento y procesamiento de los datos.
- Los resultados computados se exportan a `output/`

![#f03c15](https://placehold.it/15/f03c15/000000?text=+) <span style="color:red">Crearé una base de datos MariaDB con tablas basadas en mis csv y montaré una web que se conecte a la BBDD y que permita realizar búsquedas mediante una interfaz amigable utilizando estos datos.</span>

## [Diagrama](https://docs.google.com/drawings/d/1eZeSIpxanI0m5VTyS7f1ZGH6IZdZI5kj706luUgLsDg)
