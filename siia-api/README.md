# Siia-Api

## Como usar la api

**Paso #1** - Activar el entorno virtual

```bash
$ # Instalacion de modulos de entorno virtual  (Linux)
$ source api-env/bin/activate
```

**Paso #2** - Instalar dependencias en el entorno virtual en caso de que no esten instaladas

```bash
$ pip install -r requirements.txt
```

**Paso #3** - Configurar `flask` para la api
```bash
$ export FLASK_APP=wsgi.py
$ export FLASK_ENV=development
```

**Paso #4** - Inizializar la base de datos si no ha sido inizializada
```bash
$ flask shell
>>> from api import db
>>> db.create_all()
```

**Paso #5** - Ejecutar el programa de la api en un servidor local `localhost:5000`
```bash
$ python run.py
```
o
```bash
$ flask run
```