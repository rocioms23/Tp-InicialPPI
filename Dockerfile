FROM tensorflow/tensorflow:2.10.0-gpu-python310

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos e instala las dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de tu código
COPY . .

# Expone el puerto de la aplicación
EXPOSE 7860

# Define el comando para iniciar tu aplicación Flask
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "main:app"]