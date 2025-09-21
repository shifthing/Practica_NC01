#Usar una imagen base de Python oficial
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos para instalar las dependencias
COPY requirements.txt .

# Instalar las dependencias
RUN pip install -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Exponer el puerto que usará la aplicación
EXPOSE 8080

# Comando para correr la aplicación
CMD ["python", "app.py"]
