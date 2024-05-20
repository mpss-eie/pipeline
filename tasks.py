from celery import Celery
from celery.schedules import timedelta
from datetime import datetime
import requests
import configparser

from models import session, TestModel

# Datos de configuración
config = configparser.ConfigParser()
config.read("pipeline.cfg")
url = config["api"]["url"]
token = config["api"]["token"]
period = int(config["scheduler"]["period"])


# Crear "app" de Celery
app = Celery("tasks", broker="redis://localhost")


# Configurar las tareas de Celery
@app.task
def test_task():
    random_fact = requests.get(url).json()["text"]
    record = TestModel(
        timestamp=int(datetime.now().timestamp()), 
        random_fact=random_fact
    )
    session.add(record)
    session.commit()
    return "¡Hola mundo!"


# ----------
# Configurar aquí las tareas de Celery para el procesamiento de los datos
# ----------

# Configurar el planificador de tareas de Celery
app.conf.beat_schedule = {
    "test-schedule": {
        "task": "tasks.test_task",
        "schedule": timedelta(seconds=period),
    },
}
