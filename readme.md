# KryptoMonedas, tu APP para invertir en  crypto monedas

## Instalación

### Descargar repositorio de GitHub

 --> Descarga la aplicación en tu ordenador con el siguiente comando desde la terminal: git clone https://github.com/evil-wombat/Krypto.git {file_name}, donde <file_name> es el nombre de la carpeta donde quieres guardar el repositorio.


### Creación de entorno virtual

 --> Una vez creada la carpeta, creamos un entorno virtual. Para ello, dentro de la carpeta donde está descargado el repositorio, introducimos el siguiente comando desde la terminal: <python -m venv {name}>, donde name es el nombre de tu entorno virtual. Un buen nombre es venv.

 Nota: Una vez creado el entorno virtual, para activarlo debes introducir el siguiente comando desde la terminal:      <. {name}/bin/activate>. Una vez activado, te aparecerá a la izquierda el nombre de tu venv entre parentis.


### Instalación de dependencias

 --> Con el entorno virtual activado, ejecutar: <pip install -r requirements.txt>


### Creación archivo config.py

 -->  dentro de nuestra carpeta con el repositorio, existe un archivo config_template.py. Crear un nuevo archivo config.py usando el mandato: cp config_template.py config.py

 --> modificamos los datos del config.py con el siguiente mandato: nano config.py. Aparecera una ventana con los siguientes valores:

 -   SECRET_KEY='pon aquí tu clave para CSRF'. 
        -> Entre las comillas escribe la clave que tú quieras.
 -   API_KEY = 'Pon aquí tu clave API' 
        -> Entre las comillas escribe tu clave API. (Para conseguir tu clave API ver apartado API_KEY)
 -   DBFILE = 'ruta a fichero sqlite' (ver apartado Creación base de datos)
        -> Entre las comillas escribe 'krypto/data/{name_db}.db, donde name_db es el nombre que escojas para tú base de datos

### Creación de la base de datos:

 --> Nos colocamos sobre la carpeta data utilizando el siguiente mandato: cd krypto/data

 --> Una vez dentro de la carpeta, ejecutamos el programa sqlite con el siguiente comando: sqlite3 {name_db}.db. Utiliza el mismo nombre que utilizaste en el archivo config.py

 --> Una vez ejecutado el mandato ya estarás dentro de sqlite. A continuación ejecuta .read/migrations/initial.sql

 --> Como comprobación para ver que se ha creado nuestra nueva base de datos podemos ejecutar los mandatos .table, donde te mostrára el nombre de la tabla creado o .schema donde te mostrará la secuencia ejecutada por SQL.

 --> Utiliza .q para salir de sqlite.

### Obtención de la API_KEY

 --> Para obtener tu API_KEY entra en la pagina de coinmarketcap con el siguiente enlace: https://coinmarketcap.com/api/

 --> Una vez dentro registrate siguiendo los pasos de la web. Una vez creada tu cuenta en Coinmarketcap, podrás obtener tu API_KEY.

 --> Utiliza esta API_KEY en el archivo config.py (ver creación archivo config.py)

 ### Ejecución APP

 --> Por último ejecuta el siguiente mandato: export APP_FLASK=run.py

 --> Para ejecutar la aplicación ejecuta: flask run.


 Disfruta de la APP KryptoMonedas!!















