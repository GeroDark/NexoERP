# NexoERP

NexoERP es una aplicacion empresarial web monolitica construida con Python y Django.

## Fase 0

Esta fase contiene solamente la base inicial del proyecto:

- Proyecto Django con modulo de configuracion `config`.
- App inicial `core`.
- Base de datos SQLite.
- Ruta raiz `/` con una pagina de confirmacion.
- Carpetas base para `templates` y `static`.

## Requisitos

- Python
- Git
- Entorno virtual de Python

## Instalacion local

Desde la raiz del proyecto:

```powershell
py -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Comandos de verificacion

```powershell
python -m django --version
python manage.py migrate
python manage.py check
python manage.py runserver
```

Luego abrir:

```text
http://127.0.0.1:8000/
```

El navegador debe mostrar:

```text
NexoERP funcionando correctamente
```
