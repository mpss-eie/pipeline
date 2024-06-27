from celery import Celery
from celery.schedules import timedelta
import configparser
import pandas as pd

from models import session, TestData
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kurtosis, norm, skew

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
def cargar_datos_task():
    #cambiar esto por una conexion a un API
    df = pd.read_csv("all_week.csv")
    tembloresJsonList  =  df.to_dict('records')

    for temblor in tembloresJsonList:
        if session.query(TestData).filter_by(id=temblor["id"]).first():
            continue
        else:
            record = TestData(
                id = temblor["id"],
                #time = datetime.strptime(temblor["time"], "%Y-%m-%dT%H:%M:%S.%fZ"),
                latitude = temblor["latitude"],
                longitude = temblor["longitude"],
                depth = temblor["depth"],
                mag = temblor["mag"],
                magType = temblor["magType"],
                nst = temblor["nst"],
                gap = temblor["gap"],
                dmin = temblor["dmin"],
                rms = temblor["rms"],
                net = temblor["net"],
                #updated = datetime.strptime(temblor["updated"], "%Y-%m-%dT%H:%M:%S.%fZ"),
                place = temblor["place"],
                type = temblor["type"],
                horizontalError = temblor["horizontalError"],
                depthError = temblor["depthError"],
                magError = temblor["magError"],
                magNst = temblor["magNst"],
                status = temblor["status"],
                locationSource = temblor["locationSource"],
                magSource = temblor["magSource"]
            )
            session.add(record)
            session.commit()

    return "Datos de temblores almacenados correctamente!"

@app.task
def media_task():
    listaTemblores = session.query(TestData).all()
    listaMagnitudes = [temblor.mag for temblor in listaTemblores]
    media = np.mean(listaMagnitudes)
    valores_x = range(len(listaMagnitudes))
    plt.plot(valores_x, listaMagnitudes, marker='o', linestyle='-', label='Data Points')
    plt.axhline(y=media, color='r', linestyle='--', label=f'Media: {media:.2f}')

    plt.xlabel('Cantidad de datos')
    plt.ylabel('Magnitud')
    plt.title('Grafico de media')
    plt.legend()
    plt.savefig('media_plot.png')
    plt.clf()

    return "¡Calculo de la media exitoso!"

@app.task
def variance_task():
    listaTemblores = session.query(TestData).all()
    listaMagnitudes = [temblor.mag for temblor in listaTemblores]
    varianza = np.var(listaMagnitudes)
    valores_x = range(len(listaMagnitudes))
    plt.plot(valores_x, listaMagnitudes, marker='o', linestyle='-', label='Data Points')
    plt.axhline(y=varianza, color='r', linestyle='--', label=f'Varianza: {varianza:.2f}')

    plt.xlabel('Cantidad de datos')
    plt.ylabel('Magnitud')
    plt.title('Grafico de varianza')
    plt.legend()
    plt.savefig('varianza_plot.png')
    plt.clf()

    return "¡Calculo de la varianza exitoso!"

@app.task
def standard_deviation_task():
    listaTemblores = session.query(TestData).all()
    listaMagnitudes = [temblor.mag for temblor in listaTemblores]
    media = np.mean(listaMagnitudes)
    desviacion = np.std(listaMagnitudes)
    valores_x = range(len(listaMagnitudes))
    plt.axhline(y=media, color='g', linestyle='-', label=f'Media: {media:.2f}')
    plt.errorbar(valores_x, listaMagnitudes, yerr=desviacion, fmt='o', label=f'Data Points con DS: {desviacion:.2f}', ecolor='r', capsize=5)

    plt.xlabel('Cantidad de datos')
    plt.ylabel('Magnitud')
    plt.title('Data Points con Barras de Error de Desviación Estandar')
    plt.legend()
    plt.savefig('desviacion_estandar_plot.png')
    plt.clf()

    return "¡Calculo de la desviación estandar exitoso!"

@app.task
def kurtosis_inclinacion_task():
    listaTemblores = session.query(TestData).all()
    listaMagnitudes = [temblor.mag for temblor in listaTemblores]
    kurt = kurtosis(listaMagnitudes)
    inclinacion = skew(listaMagnitudes)
    media = np.mean(listaMagnitudes)
    desviacion = np.std(listaMagnitudes)
     
    plt.hist(listaMagnitudes, bins=50, density=True, alpha=0.7, color='blue') 
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, media, desviacion)
    plt.plot(x, p, 'k', linewidth=2)
    
    plt.title(f'Kurtosis: {kurt:.2f}, Inclinación: {inclinacion:.2f}')
    plt.xlabel('Magnitud')
    plt.legend()
    plt.savefig('kurtosis_plot.png')
    plt.clf()

    return "¡Calculo de kurtosis exitoso!"

# ----------
# Configurar aquí las tareas de Celery para el procesamiento de los datos
# ----------

# Configurar el planificador de tareas de Celery
app.conf.beat_schedule = {
    "test-cargar-datos-task": {
        "task": "tasks.cargar_datos_task",
        "schedule": timedelta(seconds=period),
    },
    "test-media-task": {
        "task": "tasks.media_task",
        "schedule": timedelta(seconds=period*2),
    },
    "test-varianza-task": {
        "task": "tasks.variance_task",
        "schedule": timedelta(seconds=period*2),
    },
    "test-desviacion-task": {
        "task": "tasks.standard_deviation_task",
        "schedule": timedelta(seconds=period*2),
    },
    "test-kurtosis-inclinacion-task": {
        "task": "tasks.kurtosis_inclinacion_task",
        "schedule": timedelta(seconds=period*2),
    },
}
