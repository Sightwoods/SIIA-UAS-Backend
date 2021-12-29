# Siia-Api

## Como usar la api

**Paso #1** - Crear el entorno virtual en caso de que no esté creado

```bash
$ python3 -m venv env
```

**Paso #2** - Activar el entorno virtual

```bash
$ # Activación de entorno virtual (Linux)
$ source env/bin/activate
```

**Paso #3** - Instalar dependencias en el entorno virtual en caso de que no esten instaladas

```bash
$ pip install -r requirements.txt
```

**Paso #4** - Configurar `flask` para la api
```bash
$ export FLASK_APP=wsgi.py
$ export FLASK_ENV=development
```

**Paso #5** - Inizializar la base de datos si no ha sido inizializada
```bash
$ flask shell
>>> from api import db
>>> db.create_all()
```

**Paso #6** - Ejecutar el programa de la api en un servidor local `localhost:5000`
```bash
$ python run.py
```
o
```bash
$ flask run
```

## Prueba logeandote y cambiando tu nip

**Desde bash**
```bash
curl -X 'POST' \
  'http://localhost:5000/api/users/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "account_number": "tu numero de cuenta",
  "nip": "tu nip"
}'
```

**Desde URL con postman u otra forma me pedir peticiones**
```bash
http://localhost:5000/api/users/login
```