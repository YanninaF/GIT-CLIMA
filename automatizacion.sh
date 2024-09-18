#!/bin/bash

# 1. Activar el entorno virtual
echo "Activando el entorno virtual..."
source .venv/Scripts/activate

# 2. Instalar dependencias
echo "Instalando dependencias..."
pip install -r requirements.txt 

# 3. Ejecutar la aplicación CLI
echo "Ejecutando la aplicacion CLI..."
python api_clima.py --formato json asuncion

# 4. Mensaje final
echo "Ejecución completada con éxito."

#./automatizacion.sh