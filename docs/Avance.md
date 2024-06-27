# Proyecto de programación

Este es el proyecto de:

- Hillary Blanco Meneses. B81148.
- Johnnixia Valdes Cespedes. C07997
- Maia Torres Castro. C07821


Esta es la documentación del proyecto de programación de IE0405 - Modelos Probabilísticos de Señales y Sistemas.

## Objetivo general

Analizar las probabilidades de ocurrencia de sismos en diferentes regiones del mundo utilizando datos estadísticos y geológicos.

## Objetivos específicos

1. Determinar las áreas geográficas con mayor probabilidad de frecuencia sísmica mediante el análisis de datos históricos para estimar probabilidades
2. Evaluar las magnitudes y profundidades de los sismos más frecuentes en distintas regiones para determinar patrones y tendencias.
3. Desarrollar modelos predictivos basados en datos estadísticos y geológicos que permitan estimar la probabilidad de futuros eventos sísmicos en diversas zonas del mundo.

## Dominio al que Pertenecen los Datos: Programa de Peligros de Terremotos
Los datos utilizados en este análisis provienen del Programa de Peligros de Terremotos, gestionado por el USGS (United States Geological Survey). Este programa se dedica al monitoreo, análisis y estudio de la actividad sísmica tanto en los Estados Unidos como a nivel global.

El dominio de los datos corresponden específicamente a los peligros de terremotos, los cuales son investigados para comprender mejor y mitigar los riesgos asociados con estos eventos naturales. A través del monitoreo continuo de datos sísmicos, el USGS busca identificar patrones, evaluar la probabilidad de futuros sismos y proporcionar información crítica que pueda ser utilizada para mejorar la preparación y respuesta ante terremotos. Este esfuerzo incluye la recopilación de datos geológicos y estadísticos, que son esenciales para la creación de modelos predictivos y la evaluación de la vulnerabilidad sísmica de diversas regiones.

## Introducción 
Los sismos son fenómenos naturales que ocurren con frecuencia en todo el mundo, incluyendo Costa Rica, debido a la actividad tectónica en la región. Costa Rica se encuentra en una zona altamente sísmica debido a la convergencia de varias placas tectónicas, lo que hace que el estudio de los sismos sea particularmente relevante para la seguridad y el desarrollo sostenible del país.

A nivel global, la comprensión de los patrones y probabilidades de los sismos es esencial para la mitigación de riesgos y la protección de vidas y bienes. La aplicación de métodos probabilísticos en la sismología permite identificar las regiones más propensas a experimentar sismos y evaluar la probabilidad de ocurrencia en diferentes zonas. Este enfoque probabilístico no solo ayuda a prever eventos futuros, sino que también es crucial para la planificación urbana, el diseño de infraestructuras resistentes a terremotos y la formulación de políticas públicas efectivas.

El análisis de datos estadísticos y geológicos proporciona una base sólida para entender los mecanismos de los sismos y desarrollar modelos predictivos que mejoren nuestra capacidad de respuesta ante estos eventos. En un mundo donde los desastres naturales pueden tener consecuencias devastadoras, el uso de la probabilidad aplicada a la sismología se convierte en una herramienta indispensable para la gestión de riesgos y la creación de sociedades más resilientes.

## Fuente de los Datos: USGS Earthquake Hazards Program

Los datos utilizados en este análisis provienen de una base de datos pública administrada por el USGS Earthquake Hazards Program. Este programa proporciona acceso a una amplia gama de datos sísmicos, incluyendo monitoreo en tiempo real, registros de estaciones sísmicas y otros datos diversos relacionados con la actividad sísmica.

El USGS Earthquake Hazards Program facilita el acceso a productos de datos que pueden ser visualizados y descargados por investigadores, profesionales y el público en general. Esta fuente de datos es fundamental para el estudio y la comprensión de los peligros sísmicos a nivel global, permitiendo la investigación científica, el desarrollo de modelos predictivos y la mejora de estrategias de preparación y respuesta ante terremotos.

## Descripción de los Datos: 
En el USGS Earthquake Hazards Program, puedes acceder a una variedad de datos sobre la actividad sísmica global en diferentes formatos. Puedes descargar los resultados en archivos como:
 ÁTOMO para estructuras XML
CSV para hojas de cálculo, 
GeoJSON para desarrolladores de aplicaciones que trabajan con datos geoespaciales
KML para visualización en Google Earth. Además
KML animados que muestran cambios en la edad y profundidad de los sismos a lo largo del tiempo. 

Estos formatos permiten explorar y analizar fácilmente la actividad sísmica, ofreciendo una visión detallada de los terremotos en todo el mundo. En nuestro caso se utilizan los datos en GeoJSON utilizando unidades de latitud y longitud en grados para determinar la ubicación precisa de los sismos. Además, registran el tiempo de ocurrencia en segundos y la profundidad del sismo en kilómetros, al igual que su magnitud en ml proporcionando información crucial para estudios detallados y análisis científicos. 

Para el caso del avance se utilizó un archivo csv, sin embargo se deberá tomar en cuenta para el trabajo final cambiar a alguna página web de sismos que posea API, ya que estos nos permitiría por decirlo asi guindarse directamente de la página web y no tener que descargar el csv, es decir armar la base de datos en base a la información constantemente actualizada de la página web y no tomarla de un archivo csv que se debe descargar  para poder actualizar los datos.

## Sistema de aerta 

Un sistema de alertas basado en la magnitud de los sismos permite notificar la ocurrencia de eventos sísmicos significativos según criterios predefinidos. En este caso, el sistema estará configurado para enviar mensajes de alerta para casos en que un nuevo sismo registrado sobrepase ya sea un valor definido o un valor que puede cambiar, como lo es un valor calculado como la media, es decir por ejemplo que se la media se encuentra en x magnitud, y sucede un sismo con  una magnitud mayor a la media, ese sismo en el momento en que el program vuelva a revisar periódicamente los datos suministrados por la página web y lo incluya a la base de datos, generará una alerta para notificar.