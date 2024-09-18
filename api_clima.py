import requests
import json
import argparse
from API_KEY import API_KEY

def main(ciudad, formato):
    # Construir la URL para la API
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={ciudad}&lang=es"
    
    try:
        # Realizar la solicitud a la API
        respuesta = requests.get(url)
        
        # Verificar si la respuesta es exitosa
        if respuesta.status_code == 200:
            json_data = respuesta.json()
            
            # Verificar si hay un error en la respuesta JSON
            if 'error' in json_data:
                print(f"Error: {json_data['error']['message']}. Verifica la ortografía de la ciudad e intentalo nuevamente.")
            else:
                # Trae la información
                location = json_data['location']
                c = json_data['current']

                ciudad = location['name']
                region = location['region']
                pais = location['country']
                temperatura_actual = c['temp_c']  
                condicion_actual = c['condition']['text']
                precipitacion = c['precip_mm']
                humedad = c['humidity']
                fecha_actualizacion = c['last_updated']

                if formato == "json":
                    datos_resu = {
                        "ciudad": ciudad,
                        "region": region,
                        "pais": pais,
                        "temperatura_actual": temperatura_actual,
                        "condicion_actual": condicion_actual,
                        "precipitacion": precipitacion,
                        "humedad": humedad,
                        "fecha_actualizacion": fecha_actualizacion,
                    }
                    print(json.dumps(datos_resu, indent=6))
                else:
                    # Formatear y mostrar el texto plano
                    data = f"""
                    Ciudad: {ciudad}, {region}, {pais}
                    Temperatura actual: {temperatura_actual}°C
                    Condición actual: {condicion_actual}
                    Precipitación: {precipitacion}mm
                    Humedad: {humedad}
                    Última actualización: {fecha_actualizacion}
                    """
                    print(data)

        else:
            print(f"Error: No se pudo conectar a la API. Código de respuesta: {respuesta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")

if __name__ == "__main__":
    # Configurar argparse para manejar los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Consulta el clima actual de una ciudad.")
    parser.add_argument('ciudad', type=str, help='Nombre de la ciudad para consultar el clima.')
    parser.add_argument('--formato', choices=['json', 'texto'], default='texto', help='Formato de salida (json o texto).')

    args = parser.parse_args()
    
    # Llamar a la función principal con los argumentos
    main(args.ciudad, args.formato)
