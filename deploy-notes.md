# Notas de despliegue simulado – Gestor de Tareas

## Requisitos
- Git y Docker Desktop instalados (con "Engine running").
- Acceso al repositorio en GitHub.

## Pasos
1. Crear una carpeta externa al proyecto de desarrollo:
   ```powershell
   mkdir C:\deploy-sim
   cd C:\deploy-sim
   ```
2. Descargar el proyecto:
   ```powershell
   git clone https://github.com/USUARIO/gestor-tareas.git
   cd gestor-tareas
   ```
3. Descargar el artefacto `gestor-tareas-image` desde la última ejecución
   exitosa en la pestaña **Actions** de GitHub, descomprimir el `.zip` y
   copiar `gestor-tareas-image.tar.gz` en esta carpeta.
4. Cargar la imagen generada por el pipeline:
   ```powershell
   docker load -i gestor-tareas-image.tar.gz
   ```
5. Levantar los servicios usando esa imagen (sin reconstruir):
   ```powershell
   docker compose up -d --no-build
   ```
6. Verificar los contenedores:
   ```powershell
   docker compose ps
   ```
7. Validar en el navegador: http://localhost:8000

## Detener / Rollback
- Detener: `docker compose down`
- Rollback: descargar el artefacto de una ejecución anterior, repetir los
  pasos 4 y 5.

## Versionado
Cada imagen se etiqueta con `latest` y con el SHA del commit
(`gestor-tareas:<sha>`), lo que permite saber qué versión del código está
desplegada.
