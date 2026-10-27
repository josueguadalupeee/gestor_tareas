# Gestor de Tareas – Django + PostgreSQL + Docker + GitHub Actions

Proyecto sencillo para la práctica de **Gestión de la Configuración de Software**
(integración y despliegue continuo).

- Proyecto Django: `config/`
- App: `tareas/` (crear, completar y eliminar tareas)
- Base de datos: PostgreSQL (en Docker y en GitHub Actions)
- Pruebas: `python manage.py test`

## Ejecutar con Docker
```powershell
docker compose up --build
```
Abrir http://localhost:8000

## Ejecutar sin Docker (usa SQLite)
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
