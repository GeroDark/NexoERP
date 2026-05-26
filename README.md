# NexoERP

NexoERP es una aplicacion empresarial web monolitica construida con Python y Django.

## Fase 0

La Fase 0 contiene la base inicial del proyecto:

- Proyecto Django con modulo de configuracion `config`.
- App inicial `core`.
- Base de datos SQLite.
- Ruta raiz `/` con una pagina de confirmacion.
- Carpetas base para `templates` y `static`.

## Fase 1

La Fase 1 incorpora el layout base profesional:

- Template global `base.html`.
- Navbar superior con identidad de NexoERP.
- Menu lateral con navegacion inicial.
- Pagina de inicio heredando del layout base.
- Pagina `/dashboard/` con tarjetas placeholder.
- Bootstrap 5 mediante CDN.
- Estilos propios en `static/css/styles.css`.

## Requisitos

- Python
- Git
- Entorno virtual de Python

## Instalacion local

Desde la raiz del proyecto:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
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

Tambien se puede abrir:

```text
http://127.0.0.1:8000/dashboard/
```
