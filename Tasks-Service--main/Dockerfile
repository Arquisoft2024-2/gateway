# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    gcc \
    pkg-config \
    && apt-get clean

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de dependencias
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt



# Copia el resto del proyecto
COPY . .

# Expone el puerto donde correrá la aplicación
EXPOSE 3308

# Comando para iniciar la aplicación usando fastapi
CMD ["fastapi", "dev", "app/main.py", "--host", "0.0.0.0", "--port", "3308"]
