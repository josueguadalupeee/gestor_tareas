# Imagen base solicitada en la guía
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 1) Instalar dependencias (se cachea si requirements.txt no cambia)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) Copiar el código del proyecto
COPY . .

EXPOSE 8000

# 3) Al iniciar el contenedor: aplicar migraciones y levantar el servidor
ENTRYPOINT ["sh", "-c", "python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]
