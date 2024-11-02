# SISTEMA DE GESTIÓN DE TAREAS

Este proyecto es un sistema simple para gestionar tareas, desarrollado con Django y PostgreSQL. Permite realizar operaciones básicas sobre las tareas y enviar notificaciones por correo electrónico cuando se crea o actualiza una tarea.

# PÁGINA WEB
https://yuhu-project.onrender.com/

# API (Swagger)
https://yuhu-project.onrender.com/api/docs

# CREDENCIALES DE AUTENTICACIÓN
usuario: admin@gmail.com
contraseña: admin

## Funcionalidades

* Crear, Leer, Actualizar y Eliminar Tareas: Maneja tareas con título, email y descripción.
* Notificaciones por Email: Envía notificaciones al crear o actualizar tareas (usando Celery).
* API Pública: Incluye endpoints para que desarrolladores puedan interactuar con el sistema.

## Tecnologías aplicadas
* Python
* Django REST Framework
* PostgreSQL
* Configuración de email (SMTP)
* Docker
* Render
* HTML