# Sistema de Inventario (Proyecto - Evaluación N°3 TI3041)

Aplicación web backend en Django que simula un sistema de inventario para una empresa del rubro forestal/logístico. Implementa modelos básicos, CRUD, autenticación por sesiones y seguridad mínima.

## Características implementadas
- Conexión configurable a MySQL mediante `.env` (`python-dotenv`).
- CRUD completo para dos entidades: `Item` y `Repuesto`.
- Sistema de sesiones (login / logout) usando `django.contrib.auth`.
- Rutas protegidas para crear/editar/eliminar (requieren autenticación).
- Contraseñas con hash mediante el sistema de Django.
- Validación básica con tipos de campo (p. ej. `PositiveIntegerField`).
- Manejo de mensajes de éxito/errores en plantilla base.

## Estructura relevante
- `inventario/models.py` — modelos `Item`, `Repuesto`.
- `inventario/views.py` — vistas basadas en clases (List/Detail/Create/Update/Delete).
- `inventario/urls.py` — rutas del CRUD.
- `templates/` — plantillas `base.html`, `inventario/*` y `registration/login.html`.
- `sistema_inventario/settings.py` — configurado para leer `.env` y usar MySQL por defecto.

## Requisitos
- Python 3.11+ (o la versión que uses)
- MySQL server (si planeas usar MySQL)

## Instalación y ejecución (Windows PowerShell)
1. Crear y activar entorno virtual:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```
2. Copiar `.env.example` a `.env` y editar valores (SECRET_KEY, MYSQL_PASSWORD, etc.):
```powershell
copy .env.example .env
# luego abre .env con tu editor y rellena credenciales
```
3. Aplicar migraciones y crear superusuario:
```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
4. Ejecutar servidor:
```powershell
python manage.py runserver
```
5. Acceder en el navegador:
- `http://127.0.0.1:8000/` — Lista de `Items`
- `http://127.0.0.1:8000/repuestos/` — Lista de `Repuestos`
- `http://127.0.0.1:8000/accounts/login/` — Login
- `http://127.0.0.1:8000/admin/` — Admin

## Notas sobre seguridad y buenas prácticas
- No subir el fichero `.env` al repositorio (está en `.gitignore`).
- En producción, `DEBUG` debe ser `False` y `SECRET_KEY` debe ser un secreto seguro.
- Usa conexiones seguras a la base de datos y restringe `ALLOWED_HOSTS`.
- Considera añadir validaciones en `ModelForm` para reglas de negocio más complejas.

## Sugerencias para evaluación y commits
Es recomendable realizar al menos 4 commits significativos (ya planificados por etapa):
1. `Etapa 1: configuración y conexión MySQL (.env placeholders)`
2. `Etapa 2: modelos y CRUD implementados`
3. `Etapa 3: autenticación y seguridad`
4. `Etapa 4: documentación y limpieza final`

## Extensiones posibles (no requeridas)
- API REST con Django REST Framework.
- Registro de movimientos de inventario (entradas/salidas) con historial.
- Permisos más finos (grupos/roles).

---
Si quieres, puedo también:
- Generar un script `fixtures` con datos de ejemplo.
- Añadir pruebas unitarias básicas para los modelos y vistas.
- Preparar instrucciones concretas para subir a GitHub y crear el archivo `repo_url.txt` final.
