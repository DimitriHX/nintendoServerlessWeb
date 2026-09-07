# Nintendo Retro Vault

[![Next.js](https://img.shields.io/badge/Next.js-16.3-black?logo=next.js)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React-19-blue?logo=react)](https://react.dev/)
[![Supabase](https://img.shields.io/badge/Supabase-Serverless%20PostgreSQL-3ECF8E?logo=supabase)](https://supabase.com/)
[![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-v4-38B2AC?logo=tailwind-css)](https://tailwindcss.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)](https://www.docker.com/)
[![Vercel](https://img.shields.io/badge/Deploy-Vercel-black?logo=vercel)](https://vercel.com/)

Nintendo Retro Vault es una aplicacion web orientada a la consulta y preservacion digital de videojuegos clasicos de Nintendo. La biblioteca contiene un catalogo curado de 40 titulos historicos para cuatro consolas: Game Boy Advance (GBA), Nintendo DS (NDS), Nintendo 64 (N64) y Nintendo Wii.

Desarrollada con Next.js 16 (App Router), React 19 Server Components, Tailwind CSS v4, persistencia serverless en Supabase con politicas de acceso seguro (Row Level Security), y un pipeline de extraccion automatizada en Python para la ingesta de datos oficiales desde Wikipedia.

---

## Caracteristicas Principales

### 1. Arquitectura y Rendimiento
* **Server Components (RSC):** Consultas directas en servidor para optimizar tiempos de respuesta, indexacion SEO y mantener las peticiones internas protegidas del cliente.
* **Capa de Resiliencia:** Fallback y tolerancia a fallos ante posibles interrupciones de conexion externa.
* **Manejo de Estados de Carga y Excepciones:**
  * `loading.tsx`: Animacion de carga y estructura visual retro.
  * `error.tsx`: Manejo seguro de fallos sin exposicion de trazas internas del servidor ni datos de infraestructura.
  * `not-found.tsx`: Pagina 404 personalizada para rutas inexistentes con retorno guiado.
* **Seguridad:** Configuracion de cabeceras HTTP de proteccion y mitigacion de divulgacion de datos.

### 2. Navegacion y Rutas Dinamicas
La aplicacion organiza su contenido mediante rutas dinamicas con slugs legibles:
* `/juego/[slug]`: Ficha tecnica con sinopsis en espanol, especificaciones, enlace enciclopedico y navegacion adyacente entre titulos.
* `/plataforma/[slug]`: Filtrado por sistema (`/plataforma/gba`, `/plataforma/nds`, `/plataforma/n64`, `/plataforma/wii`).
* `/genero/[slug]`: Filtrado tematico por categoria (`/genero/rpg`, `/genero/plataformas`, `/genero/aventura`, etc.).

### 3. Experiencia de Usuario
* **Paginacion por Pestanas:** 10 titulos por pestana para un rendimiento fluido y organizado.
* **Animacion Secuencial en Cadena:** Giro 3D escalonado cada 2 segundos entre las fichas activas, concluyendo con un giro sincronizado antes de reiniciar el ciclo.
* **Optimizacion de Escala (Zoom 115%):** Dimensionado adaptado para lectura confortable en computadoras portatiles.
* **Diseno Retro Sobrio:** Estetica inspirada en consolas clasicas sin uso de emojis, con tipografias de estilo arcade.

### 4. Pipeline de Datos con Python
* **Extraccion Oficial:** Recopilacion automatizada de especificaciones tecnicas, sinopsis y portadas desde la API REST de Wikipedia, garantizando fidelidad historica y licencias abiertas sin datos ficticios.
* **Procesamiento y Estandarizacion:** Scripts en Python encargados del saneado de texto, traduccion al espanol y generacion de slugs limpios para cada registro.

---

## Base de Datos (Supabase Serverless)

La persistencia de datos se gestiona a traves de una base de datos PostgreSQL serverless en Supabase protegida por politicas Row Level Security (RLS) que restringen el acceso anonimo a solo lectura (`SELECT`).

### Inicializacion:
1. Crea un nuevo proyecto en [Supabase](https://supabase.com).
2. Dirigete a la seccion **SQL Editor** en el panel de control.
3. Ejecuta el archivo de inicializacion provisto en el repositorio: [`supabase_setup.sql`](./supabase_setup.sql).
4. El script creara la estructura necesaria, aplicara las reglas de seguridad RLS y cargara los 40 registros oficiales con sus portadas e informacion en espanol.

---

## Variables de Entorno

La aplicacion requiere configurar dos variables publicas de conexion para comunicarse con Supabase.

Crea un archivo `.env.local` dentro del directorio `nextjs/` (o configuralas en el panel de Vercel):

```env
# URL base de tu proyecto en Supabase (Project Settings > API)
NEXT_PUBLIC_SUPABASE_URL=https://tu-proyecto.supabase.co

# Clave publica anonima (anon key) con permisos RLS de solo lectura
NEXT_PUBLIC_SUPABASE_ANON_KEY=tu-clave-anonima-publica
```

> **Aviso de Seguridad:** Utiliza unicamente la clave publica `anon`. Nunca configures ni expongas la clave `service_role` (clave maestra de administracion) en variables con prefijo `NEXT_PUBLIC_`, ya que dicha clave elude las reglas RLS.

Existe una plantilla de referencia disponible en [`.env.example`](./.env.example).

---

## Puesta en Marcha Local

### Opcion 1: Con Docker (Recomendado)
No requiere instalar Node.js en la maquina host:

```bash
# Iniciar contenedor en segundo plano
docker compose up -d

# Monitorear logs de ejecucion
docker logs -f nextjs_dev

# Abrir en el navegador
http://localhost:3000
```

Para detener el contenedor:
```bash
docker compose down
```

### Opcion 2: Con Node.js local (v20 o superior)

```bash
cd nextjs
npm install
npm run dev
# Abrir en el navegador: http://localhost:3000
```

Para validar la compilacion de produccion:
```bash
cd nextjs
npm run build
```

---

## Despliegue en Vercel

1. **Subir cambios a tu repositorio en GitHub:**
   ```bash
   git add .
   git commit -m "docs: actualizar documentacion de despliegue"
   git push origin main
   ```

2. **Configurar el proyecto en Vercel:**
   * Inicia sesion en [Vercel](https://vercel.com).
   * Haz clic en **Add New...** > **Project** y selecciona tu repositorio.
   * En la configuracion del proyecto:
     * **Root Directory:** Selecciona `nextjs`.
     * **Framework Preset:** `Next.js` (detectado automaticamente).
   * En la seccion **Environment Variables**, ingresa:
     * `NEXT_PUBLIC_SUPABASE_URL`
     * `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   * Haz clic en **Deploy**.

---

## Estructura del Proyecto

```text
.
├── Docker-Nextjs.yml            # Configuracion de entorno Docker
├── docker-compose.yml           # Alias Docker Compose
├── supabase_setup.sql           # Script de estructura y carga de datos para Supabase
├── .env.example                 # Plantilla de variables de entorno
├── scripts/                     # Automatizacion en Python para extraccion y saneado de datos
└── nextjs/
    ├── app/
    │   ├── layout.tsx           # Layout raiz con fuentes y navegacion
    │   ├── globals.css          # Estilos globales, zoom 115% y animaciones 3D
    │   ├── page.tsx             # Pagina principal
    │   ├── loading.tsx          # Estado de carga
    │   ├── error.tsx            # Manejador de excepciones seguro
    │   ├── not-found.tsx        # Pagina 404 personalizada
    │   ├── juego/[slug]/        # Ruta dinamica: Ficha tecnica
    │   ├── plataforma/[slug]/   # Ruta dinamica: Filtro por consola
    │   └── genero/[slug]/       # Ruta dinamica: Filtro por genero
    ├── components/
    │   ├── GameCard.tsx         # Tarjeta individual con insignia interactiva
    │   └── GameGrid.tsx         # Cuadricula paginada por pestanas (10 fichas)
    ├── data/
    │   └── games.json           # Catalogo local de contingencia
    ├── lib/
    │   └── supabase.ts          # Modulo cliente Supabase y funciones de consulta
    └── types/
        └── game.ts              # Definicion de tipos TypeScript
```

---

## Licencia y Aviso Legal

Este proyecto ha sido desarrollado con fines de preservacion cultural e investigacion de desarrollo web. La informacion y recursos graficos han sido obtenidos mediante scripts de automatizacion en Python consumiendo la API REST de Wikipedia bajo licencias Creative Commons (CC-BY-SA). Todos los nombres comerciales, marcas registradas y derechos de personajes pertenecen a Nintendo Co., Ltd. y a sus correspondientes licenciatarios.
