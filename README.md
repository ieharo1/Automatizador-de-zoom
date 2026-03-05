# Edge de Automatización Browser con Selenium Grid y Nginx

Arquitectura de laboratorio/prod para automatización web distribuida, con gateway unificado y ejecución remota de navegador.

## Descripción

Este servidor integra controlador de automatización y Selenium Grid para ejecutar acciones de navegador en contenedores aislados.

## ¿Qué hace este proyecto?

- Expone API de control para automatizaciones.
- Provee Selenium Hub + nodo Chrome para ejecución remota.
- Centraliza endpoints técnicos mediante Nginx.
- Permite separar orquestación de ejecución browser.

## Características Principales

| Característica | Descripción |
|---|---|
| Selenium Grid | Escenario listo para automatización remota |
| API de control | Endpoint de integración para flujos automatizados |
| Gateway unificado | `/api` y `/wd/hub` bajo un host |
| Escalable | Posibilidad de aumentar nodos browser |

## Stack Tecnológico

- Python Flask
- Selenium Grid
- Nginx
- Docker Compose

## Instalación y Uso

### Levantar entorno

```bash
docker compose up -d --build
```

### Probar

- API health: `http://localhost:8084/api/health`
- Estado WebDriver: `http://localhost:8084/wd/hub/status`

## Variables de Entorno

- `NGINX_PORT`: puerto público de la plataforma.

## Estructura del Proyecto

```text
.
├── Dockerfile
├── docker-compose.yml
├── .env
├── controller/
│   ├── app.py
│   └── requirements.txt
└── nginx/
    └── default.conf
```

## Casos de Uso

- QA automatizado de aplicaciones web.
- Bots de navegación para tareas repetitivas.
- Entornos de pruebas E2E containerizados.

---

## ‍ Desarrollado por Isaac Esteban Haro Torres

**Ingeniero en Sistemas · Full Stack · Automatización · Data**

-  Email: zackharo1@gmail.com
-  WhatsApp: 098805517
-  GitHub: https://github.com/ieharo1
-  Portafolio: https://ieharo1.github.io/portafolio-isaac.haro/

---

##  Licencia

© 2026 Isaac Esteban Haro Torres - Todos los derechos reservados.
