# PYTHON TO CLOUD API REST

Api creada con el fin de facilitar la comunicación con mi proyecto de google cloud. Todas las peticiones se envían a través de Cloud Functions de acceso público para que los profesores puedan probarlas sin perder el tiempo con las credenciales.

Cada método responde a una serie de variables que se encuentran en el archivo ApiConfig.

#### `crawl(page)`
Pone en marcha un spider que generará un nuevo dataset de la/s página/s indicada/s. De momento solo está disponible 'YelpFood', pero cuando haya más categorías, la variable `yelp` pondrá en marcha el spider de todas las secciones de Yelp disponibles, así como la variable `food` pondría en marcha el spider de todas las páginas recogidas de restaurantes (planeo recoger datos también de otras plataformas más adelante).
> Las variables/páginas disponibles están definidas en el archivo de configuración, pero si se conocen las opciones y se quiere, se puede introducir como parámetro directamente un string indicando el crawler específico.

#### `stage(dataset, category)`
Coge del storage el dataset más reciente de la página y categoría que le indiques y lo mete en la carpeta `input/` para su posterior tratamiento. Los parámetros tienen que estar en formato str. Ej: `stage('yelp', 'food')`

#### `create_cluster()`
Levanta un cluster estándar con hadoop y hive para realizar operaciones.
>El servidor genera una respuesta de error, pero se trata de un bug de google, ya que el clúster sí que se levanta.

#### `send_job(job_name, dataset, category)`
Genera y pone en marcha un job (requiere que el cluster esté levantado). Se pueden definir tantos jobs como se quiera, luego solo habría que invocar a la función pasándole como parámetro la variable con el json. Ej: `send_job(CreateTableAirbnb)` <br>
Hay varios procesos automatizados en el archivo de configuración
>Los parámetros 'dataset' y 'category' solo se requieren para jobs del tipo 'LoadData' y deben ir en formato str.

#### `delete_cluster()`
Elimina el cluster (requiere que el cluster esté levantado o levantándose).

<br>
<span style="color:red">Algunas ejecuciones pueden tardar un tiempo en llevarse a cabo. Más adelante buscaré la manera de comprobar que una tarea requerida se haya finalizado antes de continuar con la siguiente tarea. O en su defecto mostrar un mensaje de error apropiado.</span>