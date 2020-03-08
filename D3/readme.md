# Módulo Exploración y Visualización con D3
Aquí se encuentra el trabajo realizado para el módulo.

He intentado que cada archivo y bloque de código sea autoexplicativo, pero básicamente tenemos:

- Un archivo "config.js" donde se encuentran las configuraciones visuales sobre el aspecto que tiene el mapa y los gráficos.
- Un archivo "gradients.js" donde se encuentra en forma de array el gradiente utilizado para los colores del mapa (de este modo se puede ampliar la librería de colores y realizar cambios de forma sencilla).
- Un archivo llamado "static_map.js" que contiene un script que bloquea los controles del mapa. Esto impide que se haga zoom o que se pueda desplazar en cualquier dirección (por defecto lo he dejado deshabilitado en el index).
- Los archivos "styles.css" e "index.html" que cargan los estilos y los scripts respectivamente.
- El archivo "map.js" que contiene el script principal con la lógica de pintar el mapa, los charts, las leyendas, y hacer que sea interactivo.

En la carpeta "golang scripts" he creado un script que se conecta a la base de datos que tengo en google cloud sql y genera un geoJson a partir de los datos de la tabla de airbnb.