from celery import Celery
from celery.schedules import timedelta
from datetime import datetime
import requests

from models import session, EnvironmentalSensor

# Crear "app" de Celery
app = Celery("tasks", broker="redis://localhost")


# Configurar las tareas de Celery
@app.task
def say_hello():
    record = EnvironmentalSensor(timestamp=int(datetime.now().timestamp()))
    session.add(record)
    session.commit()
    return "Hello world!"


# Configurar el planificador de tareas de Celery
app.conf.beat_schedule = {
    "periodic-tester": {
        "task": "tasks.say_hello",
        "schedule": timedelta(seconds=10),
    },
}
