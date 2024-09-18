### GIT-WEATHERED 🌤️
-----
>Tu prónostico a Comandos

***Desarrollo de una aplicación CLI que consulte una API de clima y muestre la información climática en la terminal***


***Resumen:***
>Esta versión inicial permite consultar el clima actual de cualquier ciudad utilizando datos de WeatherAPI. La aplicación devuelve información como temperatura, condiciones climáticas, precipitación, humedad y la última actualización. Se puede obtener la salida en formato texto o JSON.

### Características:
- Consulta del clima en tiempo real.
- Formatos de salida: JSON o texto plano.
- Datos proporcionados:
- Ciudad, región y país.
- Temperatura, condiciones, precipitación y humedad.
- Fecha de última actualización.

**Uso:**
>Clima en formato texto (predeterminado):
`python script.py "Ciudad"`

>Clima en formato JSON:
`python script.py "Ciudad" --formato json`


#### Requisitos:
- Librerías: requests, argparse.
- Clave API de WeatherAPI en API_KEY.py.