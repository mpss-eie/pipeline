# Recopilación de datos

El análisis de datos comienza con la recopilación de datos. Podríamos separar la recopilación en dos grandes paradigmas:

- **Procesamiento por lotes** (*batch processing*): consiste en la recolección de una gran cantidad de datos históricos, típicamente una sola vez, o con una frecuencia tan baja que cada recopilación tiene una gran cantidad de datos. Ejemplos: los "famosos" datos de pasajeros del Titanic (necesariamente recolectados una sola vez) o la información que utiliza YouTube o Netflix para hacer recomendaciones, que son actualizados aproximadamente cada 24 horas y contienen millones de interacciones.
- **Procesamiento en tiempo real** (*real-time processing*): consiste en la recolección de datos al momento de su ocurrencia (basado en eventos, *event-driven*) o con una frecuencia de recopilación tan alta que solamente algunos pocos nuevos datos, o ninguno, son obtenidos en cada muestreo. Ejemplos: datos sobre terremotos o de redes de sensores.

En medio de ambos hay una "zona gris" a menudo llamada **procesamiento en tiempo casi real** (*quasi real-time processing*) que captura la dinámica del sistema sin responder directamente a eventos o a una alta frecuencia. Ejemplos: telemetría y rastreo en vehículos de transporte público, que actualizan datos cada 15 o 20 segundos, lo suficiente para tener una buena estimación, pero no totalmente "en tiempo real".

Una definición informal de "procesamiento en tiempo real" es la siguiente: un flujo de datos en el cual el procesamiento de una nueva muestra es realizado en el momento de su llegada y concluye, de preferencia, antes de la llegada de la siguiente muestra o evento.

### ¿Y de dónde vienen estos datos?

A veces de un solo archivo (ejemplo, un `.xlsx` o `.csv`), a veces directamente de un sensor (ejemplo, un Arduino con un sensor de temperatura conectado a nuestra computadora), a veces de una base de datos externa, siguiendo varios modelos de comunicación posibles.

Algunos de estos modelos de comunicación son:

- **Publicación/suscripción**: donde un *productor* *publica* un *mensaje* que coloca en un *canal* y el intermediador lo distribuye a todos los procesos que estén *suscritos*
- **WebSockets**: donde hay un canal *permanente* de comunicación *bidireccional*
- **Web API** (una *solicitud HTTP* donde el *cliente* interactúa con *recursos* del *servidor*)
- Otros

Una de las soluciones más populares es, precisamente, obtener datos de fuentes externas, y hacerlo por medio de una interfaz de programación de aplicaciones (API).

### ¿Qué haremos en el proyecto?

Para este proyecto haremos una recopilación de datos en tiempo real de fuentes externas con un Web API y lo haremos de forma periódica, utilizando un administrador y planificador de tareas.

A continuación hay una ampliación de estos conceptos.

## Datos desde fuentes externas con API

En el **PyX** [número 6](https://github.com/fabianabarca/python) hay una explicación más amplia sobre Web API y el uso del paquete `requests` de Python.

Hay una gran cantidad de datos en [Public APIs](https://publicapis.dev/)

## Recolección periódica de datos con un planificador de tareas

En Python es posible utilizar el paquete [Celery](https://docs.celeryq.dev/en/stable/index.html) como administrador de tareas (*task manager*) y como planificador de tareas (*task scheduler*) que "calendariza" tareas en frecuencias especificadas como "cada 60 segundos" o según otros criterios, como "el primer lunes del mes" o "al anochecer".

Para un canal de procesamiento de datos en tiempo real o en tiempo *casi* real podemos usar Celery para recopilar datos de forma continua y periódica.

### Administrador de tareas

Celery Worker administra la ejecución de tareas de forma asincrónica entre los "trabajadores" disponibles. Un "trabajador" puede ser simplemente un núcleo de la computadora local que está libre para ejecutar una tarea o puede ser un servidor remoto, por ejemplo, en una configuración más compleja.

"Asincrónico" significa que las tareas no bloquean unas a otras. Por ejemplo: en un flujo "sincrónico" de tareas, una tarea es ejecutada solamente hasta que la anterior haya sido terminada. En el contexto de un administrador de tareas como Celery Worker, un flujo de tareas asincrónico permite que múltiples tareas se ejecuten en paralelo, sin esperar a que las tareas anteriores se completen. Celery Worker estará a cargo de "vigilar" la cola de ejecución de las tareas y reportar sus resultados.

### Planificador de tareas

Con Celery Beat podemos definir los momentos en que las tareas son ejecutadas. Esto es útil para crear tareas periódicas, en un periodo de tiempo definido como "cada 15 segundos" o "cada 12 horas" o "todos los días a las 2:00 am" o "el segundo miércoles de cada mes", e inclusive con base en eventos solares, como "al amanecer" o "al mediodía" (que varía según la ubicación en el planeta y la época del año).

### Intermediador de mensajes

Cuando es necesaria la comunicación entre procesos en una computadora, es necesario un **intermediador de mensajes** (*message broker*) para entregar el mensaje, pues los procesos *per se* no pueden comunicarse entre sí directamente.

[Redis](https://redis.io/) es un *message broker* popular que permite varios modelos de comunicación, como publicación/suscripción. 

Redis tiene integración con Celery, y es necesario para el envío de la asignación de las tareas periódicas.

Por ejemplo, cuando Celery Beat 
