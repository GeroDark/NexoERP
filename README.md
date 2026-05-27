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

## Fase 2

La Fase 2 incorpora autenticacion basica con Django:

- Login en `/accounts/login/`.
- Logout mediante formulario POST.
- Dashboard protegido para usuarios autenticados.
- Estado de sesion visible en el navbar.
- Enlace al admin para usuarios staff o superuser.
- Comando `setup_roles` para crear grupos base.

Grupos base:

- Administrador
- Gerencia
- Analista
- Invitado

## Fase 3

La Fase 3 incorpora el modulo de empresas/clientes:

- App Django `empresas`.
- Modelo `Empresa` con desactivacion logica.
- Listado protegido en `/empresas/`.
- Busqueda por razon social, nombre comercial, documento o correo.
- Creacion, detalle, edicion y desactivacion de empresas.
- Registro del modelo en Django Admin.
- Validaciones basicas de documento, correo, codigo de pais y telefono.

## Fase 4

La Fase 4 incorpora el modulo de contactos empresariales:

- App Django `contactos`.
- Modelo `Contacto` relacionado con `Empresa`.
- Listado protegido en `/contactos/`.
- Busqueda por nombre, cargo, correo, telefono, celular o empresa.
- Validaciones de correo, telefono y celular.
- Codigos de pais para telefono y celular.
- Creacion, detalle, edicion y desactivacion logica de contactos.
- Creacion de contactos desde el detalle de una empresa.
- Visualizacion de contactos asociados dentro del detalle de empresa.
- Registro del modelo en Django Admin.

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
python manage.py makemigrations empresas
python manage.py makemigrations contactos
python manage.py migrate
python manage.py setup_roles
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

Modulo de empresas:

```text
http://127.0.0.1:8000/empresas/
```

Modulo de contactos:

```text
http://127.0.0.1:8000/contactos/
```

Si no existe un superusuario local, se puede crear con:

```powershell
python manage.py createsuperuser
```
