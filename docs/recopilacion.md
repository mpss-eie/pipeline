# Recopilación de datos

## Datos desde fuentes externas con API

Hay una gran cantidad de datos en [Public APIs](https://publicapis.dev/)

## Recolección periódica de datos con un planificador de tareas

En Python es posible utilizar el paquete [Celery](https://docs.celeryq.dev/en/stable/index.html) como administrador de tareas (*task manager*) y como planificador de tareas (*task scheduler*) que "calendariza" tareas en frecuencias especificadas como "cada 60 segundos" o según otros criterios, como "el primer lunes del mes" o "al anochecer".

Para un canal de procesamiento de datos en tiempo real o en tiempo *casi* real podemos usar Celery para recopilar datos de forma continua y periódica.

### Administrador de tareas

Celery Worker

### Planificador de tareas

Con Celery Beat podemos definir 

### Intermediador de mensajes

Cuando es necesaria la comunicación entre procesos en una computadora, es necesario un **intermediador de mensajes** (*message broker*) para entregar el mensaje, pues los procesos *per se* no pueden comunicarse entre sí directamente.

[Redis](https://redis.io/) es un *message broker* popular que permite varios modelos de comunicación, como publicación/suscripción (donde un *productor* *publica* un *mensaje* que coloca en un *canal* y el intermediador lo distribuye a todos los procesos que estén *suscritos*). 

Redis tiene integración con Celery, y es necesario para el envío de la asignación de las tareas periódicas.
