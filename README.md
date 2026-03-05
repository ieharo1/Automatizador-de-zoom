# Automatizador-de-zoom - Nginx Edge + Selenium Grid

Arquitectura estilo laboratorio de automatizacion de reuniones con Selenium Grid expuesto por Nginx.

## Arquitectura

- `zoom-controller`: API para acciones de automatizacion.
- `selenium-hub` + `chrome`: grid para ejecucion de navegacion remota.
- `zoom-nginx`: expone API y WebDriver con un solo punto de entrada.

## Levantar

```bash
docker compose up -d --build
```

Endpoints:

- `http://localhost:8084/api/health`
- `http://localhost:8084/wd/hub/status`

## Variables

- `NGINX_PORT`: puerto del edge.

## Valor para perfil

- Integracion de testing browser automation en entorno servidor.
- Nginx como fachada de servicios internos.

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
