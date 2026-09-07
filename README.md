# Nintendo Retro Vault

[![Next.js](https://img.shields.io/badge/Next.js-16.3-black?logo=next.js)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React-19-blue?logo=react)](https://react.dev/)
[![Supabase](https://img.shields.io/badge/Supabase-Serverless%20PostgreSQL-3ECF8E?logo=supabase)](https://supabase.com/)
[![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-v4-38B2AC?logo=tailwind-css)](https://tailwindcss.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)](https://www.docker.com/)
[![Vercel](https://img.shields.io/badge/Deploy-Vercel-black?logo=vercel)](https://vercel.com/)

Nintendo Retro Vault es una aplicacion web orientada a la preservacion, difusion y consulta enciclopedica de videojuegos clasicos oficiales de Nintendo. La plataforma alberga un catalogo historico de 40 titulos distribuidos equilibradamente entre cuatro consolas: Game Boy Advance (GBA), Nintendo DS (NDS), Nintendo 64 (N64) y Nintendo Wii.

Construida con Next.js 16 (App Router), React 19 Server Components, Tailwind CSS v4 y persistencia serverless en Supabase (PostgreSQL con Row Level Security).

---

## Caracteristicas Tecnicas

### 1. Arquitectura Next.js 16 (App Router & Server Components)
* **Server Components (RSC):** Renderizado directo en el servidor para maxima velocidad de respuesta, SEO optimizado y eliminacion de llamadas API expuestas en el navegador del cliente.
* **Resiliencia de Datos:** Capa de acceso a datos con cacheo inteligente y fallback offline que garantiza disponibilidad ante cualquier contingencia de red.
* **Manejo de Estados y Excepciones:**
  * `loading.tsx`: Estado visual de carga con estetica retro arcade.
  * `error.tsx`: Manejo seguro de errores sin filtrar trazas internas, consultas SQL ni datos de infraestructura sensible.
  * `not-found.tsx`: Pagina 404 personalizada con navegacion de retorno asistida.
* **Endurecimiento de Seguridad HTTP:** Configuracion en `next.config.ts` de cabeceras de proteccion (`X-Frame-Options: SAMEORIGIN`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy`, y `poweredByHeader: false`).

### 2. Rutas Dinamicas Implementadas
La plataforma implementa 3 dimensiones de enrutamiento dinamico amigable (slugs legibles sin identificadores aleatorios):
* `/juego/[slug]`: Ficha tecnica individual con especificaciones de hardware, sinopsis en espanol, navegacion adyacente entre fichas y enlace enciclopedico.
* `/plataforma/[slug]`: Catalogo filtrado por sistema (`/plataforma/gba`, `/plataforma/nds`, `/plataforma/n64`, `/plataforma/wii`).
* `/genero/[slug]`: Catalogo filtrado por genero (`/genero/rpg`, `/genero/plataformas`, `/genero/carreras`, etc.).

### 3. Interfaz y Experiencia de Usuario
* **Paginacion por Pestanas (10 Fichas):** Organizacion en bloques de 10 juegos por pestana para evitar saturacion visual y optimizar el consumo de recursos.
* **Animacion Secuencial en Cadena:** En la pestana activa, las insignias de consola de cada ficha realizan un giro 3D de forma escalonada cada 2 segundos. Al completar el ciclo de las 10 fichas, todas giran simultaneamente antes de reiniciar la secuencia.
* **Escala Visual (Zoom 115%):** Optimizacion CSS para lectura comoda y nitida en pantallas de laptops y ordenadores portatiles.
* **Sin Emojis:** Identidad visual sobria con tipografias clasicas (`Press Start 2P`, `VT323`) y estetica arcade retro.

---

## Modelo de Datos y Supabase Serverless

La persistencia se gestiona en Supabase PostgreSQL mediante la tabla `public.games`. El script completo para la creacion de la tabla, las politicas RLS y el sembrado de los 40 titulos se encuentra en [`supabase_setup.sql`](./supabase_setup.sql):

```sql
-- Creacion de la tabla
CREATE TABLE IF NOT EXISTS public.games (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    slug TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    platform TEXT NOT NULL,
    platform_slug TEXT NOT NULL,
    genre TEXT NOT NULL,
    genre_slug TEXT NOT NULL,
    release_year INTEGER NOT NULL,
    developer TEXT NOT NULL,
    description TEXT NOT NULL,
    image_url TEXT NOT NULL,
    source_url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- Habilitacion de Row Level Security (RLS)
ALTER TABLE public.games ENABLE ROW LEVEL SECURITY;

-- Politica de lectura publica (SELECT)
CREATE POLICY "Public Read Games"
    ON public.games
    FOR SELECT
    USING (true);
```

### Configuracion en Supabase:
1. Crea un proyecto en [Supabase](https://supabase.com).
2. Dirigete a la seccion **SQL Editor** en el panel lateral.
3. Pega el contenido de [`supabase_setup.sql`](./supabase_setup.sql) y haz clic en **Run**. Se creara la tabla, la politica RLS y se insertaran los 40 registros oficiales con sus portadas y sinopsis en espanol.

---

## Variables de Entorno

Para conectar la aplicacion a Supabase, configura las siguientes variables en tu archivo `.env.local` dentro de `nextjs/` (o en la configuracion del proyecto en Vercel):

```env
# URL del proyecto en Supabase (Project Settings > API)
NEXT_PUBLIC_SUPABASE_URL=https://tu-proyecto.supabase.co

# Llave publica anonima con permisos de solo lectura RLS
NEXT_PUBLIC_SUPABASE_ANON_KEY=tu-anon-key-aqui
```

> **Nota:** Puedes consultar la plantilla en [`.env.example`](./.env.example) o [`nextjs/.env.example`](./nextjs/.env.example). No expongas credenciales privadas (service_role) en el repositorio publico.

---

## Puesta en Marcha Local

### Opcion A: Con Docker (Recomendado)
No requiere tener instalado Node.js en la maquina host:

```bash
# 1. Iniciar el contenedor de desarrollo en segundo plano
docker compose up -d

# 2. Monitorear los logs del servidor
docker logs -f nextjs_dev

# 3. Abrir en el navegador
http://localhost:3000
```

Para detener el contenedor:
```bash
docker compose down
```

### Opcion B: Con Node.js local (v20+)

```bash
cd nextjs
npm install
npm run dev
# Acceder a http://localhost:3000
```

Para generar la compilacion de produccion:
```bash
cd nextjs
npm run build
```

---

## Despliegue en Vercel (Paso a Paso)

1. **Subir los cambios a GitHub:**
   ```bash
   git add .
   git commit -m "feat: Nintendo Retro Vault complete production build"
   git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   git push -u origin main
   ```

2. **Vincular en Vercel:**
   * Inicia sesion en [Vercel](https://vercel.com).
   * Haz clic en **Add New...** > **Project** y selecciona tu repositorio de GitHub.
   * En la configuracion del proyecto:
     * **Root Directory:** Haz clic en *Edit* y selecciona la carpeta `nextjs`.
     * **Framework Preset:** `Next.js` (detectado automaticamente).
   * En el apartado **Environment Variables**, anade:
     * `NEXT_PUBLIC_SUPABASE_URL`
     * `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   * Haz clic en **Deploy**.

---

## Estructura del Proyecto

```text
.
├── Docker-Nextjs.yml            # Configuracion de Docker (Node 22 Alpine)
├── docker-compose.yml           # Alias para Docker Compose
├── supabase_setup.sql           # Script SQL completo: esquema, RLS y 40 juegos
├── seed_games.json              # Datos fuente estructurados en JSON
├── .env.example                 # Plantilla de variables de entorno
├── scripts/
│   ├── extract_seed_data.py     # Script extractor de Wikipedia REST API
│   ├── translate_descriptions.py# Traduccion de sinopsis a espanol
│   └── update_slugs.py          # Generador de slugs cortos y legibles
└── nextjs/
    ├── app/
    │   ├── layout.tsx           # Layout principal, fuentes retro y estructura comun
    │   ├── globals.css          # Estilos globales, zoom 115% y animaciones 3D
    │   ├── page.tsx             # Pagina principal con selector de consolas y generos
    │   ├── loading.tsx          # Pantalla de carga animada
    │   ├── error.tsx            # Manejo seguro de errores
    │   ├── not-found.tsx        # Pagina 404 personalizada
    │   ├── juego/
    │   │   └── [slug]/
    │   │       └── page.tsx     # Ruta Dinamica 1: Detalle de juego con navegacion adyacente
    │   ├── plataforma/
    │   │   └── [slug]/
    │   │       └── page.tsx     # Ruta Dinamica 2: Filtrado por consola (GBA, NDS, N64, Wii)
    │   └── genero/
    │       └── [slug]/
    │           └── page.tsx     # Ruta Dinamica 3: Filtrado por categoria
    ├── components/
    │   ├── GameCard.tsx         # Tarjeta de juego con animacion de insignia
    │   └── GameGrid.tsx         # Cuadricula con pestanas (10 juegos) y giro en cadena
    ├── data/
    │   └── games.json           # Copia local de datos para resiliencia y fallback offline
    ├── lib/
    │   └── supabase.ts          # Cliente Supabase resiliente
    ├── types/
    │   └── game.ts              # Tipos TypeScript de la entidad Game
    └── .env.example             # Plantilla de variables de entorno para Vercel/local
```

---

## Licencia y Aviso Legal

Este proyecto ha sido desarrollado con fines de preservacion y divulgacion cultural. Las sinopsis y portadas provienen de la [API REST de Wikipedia](https://www.mediawiki.org/wiki/API:REST_API) bajo licencias Creative Commons (CC-BY-SA). Todas las marcas registradas, nombres de juegos, consolas y personajes son propiedad exclusiva de Nintendo Co., Ltd. y de sus respectivos desarrolladores y distribuidores.
