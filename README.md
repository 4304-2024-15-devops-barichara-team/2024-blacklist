# 2024-blacklist

## Project Overview
El objetivo de este microservicio es que cientos de sistemas internos puedan consultar si un email está en la lista negra global de la empresa o no, así como agregar emails a la lista negra global.

## Estructura del proyecto


```
.
├── .github                # Archivos de configuración de GitHub
├── .gitignore             # Archivo de configuración de Git
├──  blacklists            # Módulo de la aplicación
├──  blacklists-deployment # Módulo de la aplicación para despliegue en AWS
├──  docker-compose.yml    # Archivo de configuración de Docker Compose
├──  README.md             # Archivo de documentación

```

## Pre-requisitos

Para ejecutar la aplicación, debe tener instalado lo siguiente:

- [Python ~3.10](https://www.python.org/downloads/)
- [Pipenv](https://pypi.org/project/pipenv/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Ejecución

### Instalar dependencias

Utilizamos pipenv para gestionar las dependencias (verificar la sección de [Pre-requisitos](#Pre-requisitos)), inicia el
shell de pipenv para activar el entorno virtual con el siguiente comando:

```bash
pipenv shell
``` 

Luego ejecuta el comando de instalación.

```bash
pipenv install --dev  # puede omitir --dev si no desea instalar las dependencias de desarrollo pero son requeridas para ejecutar las pruebas unitarias
```

Esto instalará las dependencias solo dentro del entorno virtual, así que recuerda activarlo cuando estés trabajando con
el microservicio. Para obtener más información sobre pipenv, consulta la documentación oficial
en https://pipenv-es.readthedocs.io.

Para salir del entorno virtual, utiliza el siguiente comando:

```bash
deactivate
```

### Variables de entorno

El servidor Flask y las pruebas unitarias utilizan variables de entorno para configurar las credenciales de la base de
datos y encontrar algunas configuraciones adicionales en tiempo de ejecución. A alto nivel, esas variables son:

```
- RDS_USERNAME: Usuario de la base de datos Postgres
- RDS_PASSWORD: Contraseña de la base de datos Postgres
- RDS_HOSTNAME: Host de la base de datos Postgres
- RDS_PORT: Puerto de la base de datos Postgres
- RDS_DB_NAME: Nombre de la base de datos Postgres
- FLASK_APP: Ruta del archivo de la aplicación Flask
- VERSION: Versión de la aplicación
- STATIC_TOKEN: Token estático para autenticar las peticiones
```

### Ejecutar la aplicación

#### Localmente

Crea un archivo `.env` en la raíz del proyecto y establece las variables de entorno necesarias. A continuación, se
muestra un ejemplo de cómo se vería el archivo `.env`:

```
VERSION=1.0
FLASK_APP=src/app.py
RDS_HOSTNAME=localhost
RDS_DB_NAME=blacklist_db
RDS_PASSWORD=postgres
RDS_PORT=5432
RDS_USERNAME=postgres
STATIC_TOKEN=pmxGDZLki/xhBD?IgXAvzWB/!xoGv6=lc=dgiBT/sRAoDFNghGU9n6EMo8nis8xw
```

Para ejecutar la aplicación, utiliza el siguiente comando:

```bash
flask run -h 0.0.0.0 -p 3000
```

#### Docker

Para ejecutar la aplicación en un contenedor Docker dirijase a la raíz del proyecto y ejecute el siguiente comando:

```bash
docker-compose up 
```

## Uso

Puede encontrar la documentación de la API en el siguiente enlace: [Documentación de la API](https://documenter.getpostman.com/view/34258162/2sAXxWb9tA)


## Autor

- Cristian Camilo Pinzon hernandez – [cc.pinzonh1@uniandes.edu.co](mailto:cc.pinzonh1@uniandes.edu.co)
- Juan Carlos De Jesus Mirelles – [j.dejesus@uniandes.edu.co](mailto:j.dejesus@uniandes.edu.co)
- Edgar Fernando Melara – [e.melara@uniandes.edu.co](mailto:e.melara@uniandes.edu.co)

## Contributing
Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.
```