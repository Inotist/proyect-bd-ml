# PYTHON TO CLOUD API REST

Api creada con el fin de facilitar la comunicación con mi proyecto de google cloud. Todas las peticiones se envían a través de Cloud Functions de acceso público para que los profesores puedan probarlas sin perder el tiempo con las credenciales.

Cada método responde a una serie de variables que se encuentran en el archivo ApiConfig.

#### `crawl(page)`
Pone en marcha un spider que generará un nuevo dataset de la página indicada. De momento solo están disponibles 'yelp' y 'food'  y por ahora ambas hacen lo mismo, pero cuando haya más categorías, la variable 'yelp' pondrá en marcha el spider de todas las secciones disponibles (planeo recoger datos también de otras plataformas más adelante).
> Las variables/páginas disponibles están definidas en el archivo de configuración.

#### `stage(dataset, category)`
Coge el dataset más reciente de la página y categoría que le indiques y lo mete en la carpeta `input/` para su posterior tratamiento. Los parámetros tienen que estar en formato str. Ej: `stage('yelp', 'food')`

#### `create_cluster()`
Levanta un cluster estándar con hadoop y hive para realizar operaciones.

#### `send_job(job_name, dataset, category)`
Genera y pone en marcha un job (requiere que el cluster esté levantado). Se pueden definir tantos jobs como se quiera. Luego solo habría que invocar a la función pasándole como parámetro la variable con el json. Ej: `send_job(CreateTableAirbnb)`
>Los parámetros 'dataset' y 'category' solo se requieren para jobs del tipo 'LoadData' y deben ir en formato str.

#### `delete_cluster`
Elimina el cluster (requiere que el cluster esté levantado o levantándose).