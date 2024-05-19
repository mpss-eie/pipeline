from sqlalchemy import Column, Integer, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear la clase base de la tabla
Base = declarative_base()


# Definir los modelos
class EnvironmentalSensor(Base):
    __tablename__ = "environmental_sensor"

    timestamp = Column(Integer, primary_key=True)


# Crear la conexión a la base de datos
engine = create_engine("sqlite:///pipeline.db")
Session = sessionmaker(bind=engine)
session = Session()

# Crear la(s) tabla(s) en la base de datos
Base.metadata.create_all(engine)
