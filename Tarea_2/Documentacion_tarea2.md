# Tarea 1: API de la NASA 
##  APIs de la [NASA](https://api.nasa.gov/?ref=apispublicas.com#CAD) consumidas
- Asteroids NeoWS
- Mars Rovers Photos

## Asteroids NeoWS
NeoWs (Near Earth Object Web Service) por sus siglas en Ingles, es el servicio web de detección de objetos cercanos a la Tierra enfocada en asteroides.
Funcionalidades de NeoWs:
- Buscar Asteroides basado en la fecha de mayor cercanía a la tierra.
- Buscar un Asteroide específico usando el id asignado por el equipo JPL de la NASA obteniendo información generalizada del objeto.

Toda la información es tomada del proyecto de Asteriodes del equipo JPL de la NASA. [NASA JPL](http://neo.jpl.nasa.gov/)

## Mars Rover Photos
Esta API es diseñada para recopilar información de imagenes tomadas por los equipos Curiosity, Opportunity y Spirit del proyecto Rovers en Marte y hacerla más fácilmente accesible para otros desarrolladores, educadores y la comunidad científica en general.
Cada Rover tiene su propio grupo de fotos almacenado en la base de datos, las cuales pueden ser accesadas independientemente. Las fotos están organizadas por la fecha Marciana en que fueron tomadas comenzando desde el día de llegada del Rover a Marte el cual sería el día 0.
Las fotos también se pueden accessar por la fecha Terrestre correspondiente.

## Extrayendo fotos por fecha Marciana(sol)
El dato sol se determina por el día de llegada del Rover a Marte siendo el primer día sol=0 y el último el día mas reciente del que se tengan fotografías 
- Ejemplo de endpoint con fecha sol=1000 (1001 día 1001 del Rover en Marte): 
https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY

## Extrayendo fotos por fecha terrestre
Se puede también extraer fotos por fecha Terrestre en formato YYYY-MM-DD (Año, mes, día).
- Ejemplo de endpoint con fecha Terrestre de 2015-06-03: 
https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-06-03&api_key=DEMO_KEY

DEMO_KEY es una llave para extraer datos de las APIs con ciertas limitaciones en la cantidad de solicitudes que se le pueden hacer al servidor, para usos extensos de datos es necesario solicitar una KEY personal en el sitio web de la [NASA](https://api.nasa.gov/?ref=apispublicas.com#CAD)


## Datos recopilados en el proyecto
### *Asteroids NeoWs*
- Cantidad de total de Asteroides cercanos a la tierra en un rango de fechas Terrestres

### *Mars Rovers*
- Fotos totales tomadas por el Rover Curiosity y Opportunity en un día en específico con fecha terreste.

## Funciones implementadas en la tarea
### getAsteroids():
Esta función hace una solicitud a la API Asteroids NeoWs, recibe 2 argumentos(fecha inicial y fecha final) que corresponden a un rango de fechas terrestres en formato (YYYY-MM-DD) (Año, mes, día) en el cual se buscara la cantidad de asteroides cercanos a la Tierra.
El rango de fechas debe cumplir las siguientes condiciones:
- Los datos de Asteroides cercanos a la tierra esta disponible desde 1900-01-01 a la fecha actual (2023-07-04)
- El rango de fechas a escoger debe ser máximo de 5 días
### Endpoint
- https://api.nasa.gov/neo/rest/v1/feed?start_date=variable_star_date&end_date=variabe_end_date&api_key=T21hmrUCC7Y5kIsbbI1wZtYvgiJo60mx5QERfPBd
- Ejemplo: https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-09&api_key=T21hmrUCC7Y5kIsbbI1wZtYvgiJo60mx5QERfPBd

El servidor devuelve un Diccionario anidado en el cual el valor asignado a cada llave es del tipo lista, existen diferentes niveles de anidado segun la información disponible en el servidor.
La respuesta del servidor contiene la siguiente informacion de los asteroides detectados dentro del rango de fechas proporcionado por el usuario.
- id del Asteroide
- Diámetro del Asteroide em KM, Millas, pies
- Distancia mas cercana a la tierra dentro del rango de fechas dado por el usuario
- Velocidad del Asteroide entre otros muchos mas.

La función getAsteroids() le muestra al usuario la cantidad total de asteroides detectados en cada uno de los dias del rango de fechas proporcionado por el usuario.
Asi como tambien un grafico de barras representando la cantidad de fotografias tomadas cada uno de los dias del rango seleccionado.


### getOpportunity():
Esta función hace una solicitud a la API MARS ROVER PHOTOS, específicamente a la base de datos de la sonda Opportunity y devuelve la cantidad de fotos tomadas por las diferentes camaras instaladas en dicha sonda en un día determinado por el usuario.
La base de datos contiene información de las fotografías tomadas entre las fechas de 2004-01-26 hasta 2018-06-07
### Endppoint
- https://api.nasa.gov/mars-photos/api/v1/rovers/Opportunity/photos?earth_date=Variable_fecha&api_key=T21hmrUCC7Y5kIsbbI1wZtYvgiJo60mx5QERfPBd
- Ejemplo: https://api.nasa.gov/mars-photos/api/v1/rovers/Opportunity/photos?earth_date=2021-02-26&api_key=T21hmrUCC7Y5kIsbbI1wZtYvgiJo60mx5QERfPBd

Esta función recibe como argumentos (Año y mes) en el formato (YYYY-MM)  y devuelve la cantidad total de fotos tomadas por las camaras de la sonda Opportunity cada dia del mes del año escojido por el usuario.
Asi como tambien realiza una grafica de lineas de la cantidad de fotografias tomadas por la Sonda Opportunity cada uno de los dias del mes escojido por el usuario.

### getCuriosity():
Esta función hace una solicitud a la API MARS ROVER PHOTOS, específicamente a la base de datos de la sonda Curiosity y devuelve la cantidad de fotos tomadas por las diferentes camaras instaladas en dicha sonda en un día determinado por el usuario.
La base de datos contiene información de las fotografías tomadas entre las fechas de 2014-10-01 a la fecha actual (2023-08-04)
### Endpoint
- https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=Variable_fecha&api_key=T21hmrUCC7Y5kIsbbI1wZtYvgiJo60mx5QERfPBd
- Ejemplo: https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2021-02-26&api_key=T21hmrUCC7Y5kIsbbI1wZtYvgiJo60mx5QERfPBd


Esta función recibe como argumentos (Año y mes) en el formato (YYYY-MM)  y devuelve la cantidad total de fotos tomadas por las camaras de la sonda Curiosity cada dia del mes del año escojido por el usuario.
Asi como tambien realiza una grafica de lineas de la cantidad de fotografias tomadas por la Sonda Curiosity cada uno de los dias del mes escojido por el usuario.


### NOTA: Algunos de los rangos de tiempo pueden dar error debido a la falta de informacion disponible en la base de datos, en algunos casos se da por perdida de comunicacion de la Sonda con las sistemas Terrestres lo cual no permite la captura de los datos de la Sonda durante el periodo de falla.

### Tambien el programa puede dar errores para años biciestos si se escoge el mes de Febrero