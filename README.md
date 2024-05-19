# Proyecto de programación de IE0405 - Modelos Probabilísticos de Señales y Sistemas

## Documentación e instrucciones del proyecto

Las intrucciones del proyecto están disponibles en la página:

[https://mpss-eie.github.io/pipeline](https://mpss-eie.github.io/pipeline)

## Instrucciones para ejecución local

Algunos de los paquetes y funcionalidades del proyecto solamente operan en los sistemas operativos tipo Unix como Linux y macOS.

Por esta razón, las personas que tengan Windows deben utilizar WSL (*Windows Subsystem for Linux*).

Las [instrucciones de instalación](https://learn.microsoft.com/es-mx/windows/wsl/install) indican que solamente es necesario la siguiente instrucción en la terminal, que instala Ubuntu por defecto:

```bash
wsl --install
```

Es necesario tener un usuario con privilegios `sudo`. Es posible configurarlo con:

```bash
adduser <username>
```

donde `<username>` puede ser, por ejemplo, `bayes` o `laplace` o `markov`, y luego

```bash
usermod -aG sudo <username>
```

para actualizar los permisos. Para cambiar de usuario `root` a `<username>` y empezar una nueva sesión de terminal con ese usuario, utilizar

```bash
su <username>
```

También es recomendado utilizar la [Terminal Windows](https://learn.microsoft.com/es-es/windows/terminal/install), que ofrece mejores herramientas para manejar múltiples terminales, tanto en Windows como en el WSL. 

Nótese que WSL no es ni una máquina virtual ni una configuración de arranque dual (*dual boot*), sino que opera nativamente en Windows. Además, los archivos de Windows están disponibles desde Linux y viceversa.

Una vez instalado WSL, las instrucciones a partir de ahora aplican para una terminal Unix con `bash` o `zsh`.

### Crear un ambiente virtual de Python

En una terminal, en el directorio raíz del repositorio, utilizar:

```bash
python3 -m venv env
```

donde `env` es el nombre del ambiente. Esto crea una carpeta con ese nombre.

Para activar el ambiente virtual, utilizar:

```bash
source env/bin/activate
```

donde `env/bin/activate` es el `PATH`. El *prompt* de la terminal cambiará para algo similar a:

```bash
base env ~/.../pipeline $
```

En este ambiente virtual no hay paquetes de Python instalados. Es posible verificar esto con `pip list`, que devolverá algo como:

```bash
Package    Version
---------- -------
pip        24.0
setuptools 65.5.0
```

### Instalar los paquetes necesarios para ejecutar el proyecto

Con el ambiente virtual activado, instalar los paquetes indicados en el archivo `requirements.txt`, con:

```bash
pip install -r requirements.txt
```

Para verificar la instalación, es posible usar nuevamente `pip list`, que ahora mostrará una buena cantidad de nuevos paquetes y sus dependencias.

### Para editar y visualizar la documentación

En una terminal, en el directorio raíz del repositorio, utilizar:

```bash
mkdocs serve
```

Abrir en un navegador web la página del "servidor local" en el puerto 8000, en [http://127.0.0.1:8000/](http://127.0.0.1:8000/) o en [http://localhost:8000/](http://localhost:8000/).

Cada cambio en los documentos de la carpeta `docs/` o en el archivo `mkdocs.yml` generan un refrescamiento de la página.

Para salir de la visualización, utilizar `Ctrl + C`, de otro modo dejar el proceso corriendo mientras edita la documentación.

### Para ejecutar el proyecto

- En una nueva terminal ejecutar el siguiente comando para activar **Redis** (más detalles en la documentación): 

```bash
redis-server
```

dejar esta terminal "corriendo".

Nota: en sistemas Linux usualmente ya está corriendo como *servicio del sistema* y por tanto dará un error de que ya está ocupado el proceso. En ese caso es posible ignorar este paso.

- En una nueva terminal ejecutar el siguiente comando para activar **Celery Worker** (más detalles en la documentación):

```bash
celery -A tasks worker --loglevel=INFO
```

dejar esta terminal "corriendo".

- En una nueva terminal ejecutar el siguiente comando para activar **Celery Beat** (más detalles en la documentación):

```bash
celery -A tasks beat --loglevel=INFO
```

dejar esta terminal "corriendo".

En este punto, ya el código de ejemplo debería estar importando y guardando datos en la base de datos, según está detallado en `models.py` y `tasks.py`.
