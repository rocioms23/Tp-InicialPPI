# Usa una imagen oficial de Python
FROM python:3.11-slim

# Instala las dependencias de sistema para OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de tu código
COPY . .

# Define el comando para iniciar tu aplicación Flask
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]