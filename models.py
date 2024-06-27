from sqlalchemy import create_engine, Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import configparser

# Datos de configuración
config = configparser.ConfigParser()
config.read("pipeline.cfg")
system = config["db"]["system"]
name = config["db"]["name"]

# Crear la clase base de la tabla
Base = declarative_base()


# Definir los modelos
class TestData(Base):
    __tablename__ = "temblor"

    id = Column(String, primary_key=True)
    time = Column(DateTime)
    latitude = Column(Float)
    longitude = Column(Float)
    depth = Column(Float)
    mag = Column(Float)
    magType = Column(String)
    nst = Column(Float)
    gap = Column(Float)
    dmin = Column(Float)
    rms = Column(Float)
    net = Column(String)
    updated = Column(DateTime)
    place = Column(String)
    type = Column(String)
    horizontalError = Column(Float)
    depthError = Column(Float)
    magError = Column(Float)
    magNst = Column(Float)
    status = Column(String)
    locationSource = Column(String)
    magSource = Column(String)

# Crear la conexión a la base de datos SQLite3
engine = create_engine(f"{system}:///{name}")
Session = sessionmaker(bind=engine)
session = Session()

# Crear la(s) tabla(s) en la base de datos
Base.metadata.create_all(engine)
