# Usamos la imagen base de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos los archivos necesarios al contenedor
COPY . .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto 5000 en el contenedor
EXPOSE 5000

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["python", "app.py"]
