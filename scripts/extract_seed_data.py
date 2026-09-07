#!/usr/bin/env python3
import json
import time
import urllib.request
import urllib.error
import uuid

# Catálogo ampliado de juegos oficiales de Nintendo (40 títulos reales)
ALL_GAMES = [
    # --- GAME BOY ADVANCE (GBA) ---
    {
        "title": "Pokémon Emerald",
        "wiki_page": "Pokemon_Emerald",
        "genre": "RPG",
        "genre_slug": "rpg",
        "release_year": 2004,
        "developer": "Game Freak",
        "platform": "Game Boy Advance",
        "platform_slug": "gba"
    },
    {
        "title": "The Legend of Zelda: The Minish Cap",
        "wiki_page": "The_Legend_of_Zelda:_The_Minish_Cap",
        "genre": "Aventura",
        "genre_slug": "aventura",
        "release_year": 2004,
        "developer": "Capcom",
        "platform": "Game Boy Advance",
        "platform_slug": "gba"
    },
    {
        "title": "Metroid Fusion",
        "wiki_page": "Metroid_Fusion",
        "genre": "Acción",
        "genre_slug": "accion",
        "release_year": 2002,
        "developer": "Nintendo R&D1",
        "platform": "Game Boy Advance",
        "platform_slug": "gba"
    },
    {
        "title": "Golden Sun",
        "wiki_page": "Golden_Sun_(video_game)",
        "genre": "RPG",
        "genre_slug": "rpg",
        "release_year": 2001,
        "developer": "Camelot Software Planning",
        "platform": "Game Boy Advance",
        "platform_slug": "gba"
    },
    {
        "title": "Castlevania: Aria of Sorrow",
        "wiki_page": "Castlevania:_Aria_of_Sorrow",
        "genre": "Acción",
        "genre_slug": "accion",
        "release_year": 2003,
        "developer": "Konami",
        "platform": "Game Boy Advance",
        "platform_slug": "gba"
    },
    {
        "title": "Advance Wars",
        "wiki_page": "Advance_Wars",
        "genre": "Estrategia",
        "genre_slug": "estrategia",
        "release_year": 2001,
        "developer": "Intelligent Systems",
        "platform": "Game Boy Advance",
        "platform_slug": "gba"
    },
    {
        "title": "Mario & Luigi: Superstar Saga",
        "wiki_page": "Mario_%26_Luigi:_Superstar_Saga",
        "genre": "RPG",
        "genre_slug": "rpg",
        "release_year": 2003,
        "developer": "AlphaDream",
        "platform": "Game Boy Advance",
        "platform_slug": "gba"
    },
    {
        "title": "Fire Emblem",
        "wiki_page": "Fire_Emblem_(video_game)",
        "genre": "Estrategia",
        "genre_slug": "estrategia",
        "release_year": 2003,
        "developer": "Intelligent Systems",
        "platform": "Game Boy Advance",
        "platform_slug": "gba"
    },
    {
        "title": "Super Mario Advance 4: Super Mario Bros. 3",
        "wiki_page": "Super_Mario_Advance_4:_Super_Mario_Bros._3",
        "genre": "Plataformas",
        "genre_slug": "plataformas",
        "release_year": 2003,
        "developer": "Nintendo EAD",
        "platform": "Game Boy Advance",
        "platform_slug": "gba"
    },
    {
        "title": "Mega Man Battle Network",
        "wiki_page": "Mega_Man_Battle_Network_(video_game)",
        "genre": "RPG",
        "genre_slug": "rpg",
        "release_year": 2001,
        "developer": "Capcom",
        "platform": "Game Boy Advance",
        "platform_slug": "gba"
    },

    # --- NINTENDO DS (NDS) ---
    {
        "title": "Pokémon HeartGold and SoulSilver",
        "wiki_page": "Pok%C3%A9mon_HeartGold_and_SoulSilver",
        "genre": "RPG",
        "genre_slug": "rpg",
        "release_year": 2009,
        "developer": "Game Freak",
        "platform": "Nintendo DS",
        "platform_slug": "nds"
    },
    {
        "title": "Mario Kart DS",
        "wiki_page": "Mario_Kart_DS",
        "genre": "Carreras",
        "genre_slug": "carreras",
        "release_year": 2005,
        "developer": "Nintendo EAD",
        "platform": "Nintendo DS",
        "platform_slug": "nds"
    },
    {
        "title": "The Legend of Zelda: Phantom Hourglass",
        "wiki_page": "The_Legend_of_Zelda:_Phantom_Hourglass",
        "genre": "Aventura",
        "genre_slug": "aventura",
        "release_year": 2007,
        "developer": "Nintendo EAD",
        "platform": "Nintendo DS",
        "platform_slug": "nds"
    },
    {
        "title": "New Super Mario Bros.",
        "wiki_page": "New_Super_Mario_Bros.",
        "genre": "Plataformas",
        "genre_slug": "plataformas",
        "release_year": 2006,
        "developer": "Nintendo EAD",
        "platform": "Nintendo DS",
        "platform_slug": "nds"
    },
    {
        "title": "Castlevania: Dawn of Sorrow",
        "wiki_page": "Castlevania:_Dawn_of_Sorrow",
        "genre": "Acción",
        "genre_slug": "accion",
        "release_year": 2005,
        "developer": "Konami",
        "platform": "Nintendo DS",
        "platform_slug": "nds"
    },
    {
        "title": "Pokémon Platinum",
        "wiki_page": "Pok%C3%A9mon_Platinum",
        "genre": "RPG",
        "genre_slug": "rpg",
        "release_year": 2008,
        "developer": "Game Freak",
        "platform": "Nintendo DS",
        "platform_slug": "nds"
    },
    {
        "title": "Professor Layton and the Curious Village",
        "wiki_page": "Professor_Layton_and_the_Curious_Village",
        "genre": "Puzzle",
        "genre_slug": "puzzle",
        "release_year": 2007,
        "developer": "Level-5",
        "platform": "Nintendo DS",
        "platform_slug": "nds"
    },
    {
        "title": "The World Ends with You",
        "wiki_page": "The_World_Ends_with_You",
        "genre": "RPG",
        "genre_slug": "rpg",
        "release_year": 2007,
        "developer": "Square Enix",
        "platform": "Nintendo DS",
        "platform_slug": "nds"
    },
    {
        "title": "Grand Theft Auto: Chinatown Wars",
        "wiki_page": "Grand_Theft_Auto:_Chinatown_Wars",
        "genre": "Acción",
        "genre_slug": "accion",
        "release_year": 2009,
        "developer": "Rockstar Leeds",
        "platform": "Nintendo DS",
        "platform_slug": "nds"
    },
    {
        "title": "Phoenix Wright: Ace Attorney",
        "wiki_page": "Phoenix_Wright:_Ace_Attorney",
        "genre": "Aventura",
        "genre_slug": "aventura",
        "release_year": 2005,
        "developer": "Capcom",
        "platform": "Nintendo DS",
        "platform_slug": "nds"
    },

    # --- NINTENDO WII ---
    {
        "title": "Super Mario Galaxy",
        "wiki_page": "Super_Mario_Galaxy",
        "genre": "Plataformas",
        "genre_slug": "plataformas",
        "release_year": 2007,
        "developer": "Nintendo EAD",
        "platform": "Wii",
        "platform_slug": "wii"
    },
    {
        "title": "Super Mario Galaxy 2",
        "wiki_page": "Super_Mario_Galaxy_2",
        "genre": "Plataformas",
        "genre_slug": "plataformas",
        "release_year": 2010,
        "developer": "Nintendo EAD",
        "platform": "Wii",
        "platform_slug": "wii"
    },
    {
        "title": "The Legend of Zelda: Twilight Princess",
        "wiki_page": "The_Legend_of_Zelda:_Twilight_Princess",
        "genre": "Aventura",
        "genre_slug": "aventura",
        "release_year": 2006,
        "developer": "Nintendo EAD",
        "platform": "Wii",
        "platform_slug": "wii"
    },
    {
        "title": "The Legend of Zelda: Skyward Sword",
        "wiki_page": "The_Legend_of_Zelda:_Skyward_Sword",
        "genre": "Aventura",
        "genre_slug": "aventura",
        "release_year": 2011,
        "developer": "Nintendo EAD",
        "platform": "Wii",
        "platform_slug": "wii"
    },
    {
        "title": "Super Smash Bros. Brawl",
        "wiki_page": "Super_Smash_Bros._Brawl",
        "genre": "Lucha",
        "genre_slug": "lucha",
        "release_year": 2008,
        "developer": "Sora Ltd. / Game Arts",
        "platform": "Wii",
        "platform_slug": "wii"
    },
    {
        "title": "Metroid Prime 3: Corruption",
        "wiki_page": "Metroid_Prime_3:_Corruption",
        "genre": "Shooter",
        "genre_slug": "shooter",
        "release_year": 2007,
        "developer": "Retro Studios",
        "platform": "Wii",
        "platform_slug": "wii"
    },
    {
        "title": "Mario Kart Wii",
        "wiki_page": "Mario_Kart_Wii",
        "genre": "Carreras",
        "genre_slug": "carreras",
        "release_year": 2008,
        "developer": "Nintendo EAD",
        "platform": "Wii",
        "platform_slug": "wii"
    },
    {
        "title": "Xenoblade Chronicles",
        "wiki_page": "Xenoblade_Chronicles_(video_game)",
        "genre": "RPG",
        "genre_slug": "rpg",
        "release_year": 2010,
        "developer": "Monolith Soft",
        "platform": "Wii",
        "platform_slug": "wii"
    },
    {
        "title": "Donkey Kong Country Returns",
        "wiki_page": "Donkey_Kong_Country_Returns",
        "genre": "Plataformas",
        "genre_slug": "plataformas",
        "release_year": 2010,
        "developer": "Retro Studios",
        "platform": "Wii",
        "platform_slug": "wii"
    },
    {
        "title": "Wii Sports",
        "wiki_page": "Wii_Sports",
        "genre": "Deportes",
        "genre_slug": "deportes",
        "release_year": 2006,
        "developer": "Nintendo EAD",
        "platform": "Wii",
        "platform_slug": "wii"
    },

    # --- NINTENDO 64 (N64) ---
    {
        "title": "Super Mario 64",
        "wiki_page": "Super_Mario_64",
        "genre": "Plataformas",
        "genre_slug": "plataformas",
        "release_year": 1996,
        "developer": "Nintendo EAD",
        "platform": "Nintendo 64",
        "platform_slug": "n64"
    },
    {
        "title": "The Legend of Zelda: Ocarina of Time",
        "wiki_page": "The_Legend_of_Zelda:_Ocarina_of_Time",
        "genre": "Aventura",
        "genre_slug": "aventura",
        "release_year": 1998,
        "developer": "Nintendo EAD",
        "platform": "Nintendo 64",
        "platform_slug": "n64"
    },
    {
        "title": "GoldenEye 007",
        "wiki_page": "GoldenEye_007_(1997_video_game)",
        "genre": "Shooter",
        "genre_slug": "shooter",
        "release_year": 1997,
        "developer": "Rare",
        "platform": "Nintendo 64",
        "platform_slug": "n64"
    },
    {
        "title": "Mario Kart 64",
        "wiki_page": "Mario_Kart_64",
        "genre": "Carreras",
        "genre_slug": "carreras",
        "release_year": 1996,
        "developer": "Nintendo EAD",
        "platform": "Nintendo 64",
        "platform_slug": "n64"
    },
    {
        "title": "Super Smash Bros.",
        "wiki_page": "Super_Smash_Bros._(video_game)",
        "genre": "Lucha",
        "genre_slug": "lucha",
        "release_year": 1999,
        "developer": "HAL Laboratory",
        "platform": "Nintendo 64",
        "platform_slug": "n64"
    },
    {
        "title": "Banjo-Kazooie",
        "wiki_page": "Banjo-Kazooie_(video_game)",
        "genre": "Plataformas",
        "genre_slug": "plataformas",
        "release_year": 1998,
        "developer": "Rare",
        "platform": "Nintendo 64",
        "platform_slug": "n64"
    },
    {
        "title": "Star Fox 64",
        "wiki_page": "Star_Fox_64",
        "genre": "Shooter",
        "genre_slug": "shooter",
        "release_year": 1997,
        "developer": "Nintendo EAD",
        "platform": "Nintendo 64",
        "platform_slug": "n64"
    },
    {
        "title": "Pokémon Snap",
        "wiki_page": "Pok%C3%A9mon_Snap",
        "genre": "Simulación",
        "genre_slug": "simulacion",
        "release_year": 1999,
        "developer": "HAL Laboratory",
        "platform": "Nintendo 64",
        "platform_slug": "n64"
    },
    {
        "title": "The Legend of Zelda: Majora's Mask",
        "wiki_page": "The_Legend_of_Zelda:_Majora%27s_Mask",
        "genre": "Aventura",
        "genre_slug": "aventura",
        "release_year": 2000,
        "developer": "Nintendo EAD",
        "platform": "Nintendo 64",
        "platform_slug": "n64"
    },
    {
        "title": "Paper Mario",
        "wiki_page": "Paper_Mario_(video_game)",
        "genre": "RPG",
        "genre_slug": "rpg",
        "release_year": 2000,
        "developer": "Intelligent Systems",
        "platform": "Nintendo 64",
        "platform_slug": "n64"
    }
]

def fetch_wikipedia_info(page_title):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{page_title}"
    headers = {"User-Agent": "NintendoVaultBot/1.0 (https://nintendovault.app; contact@nintendovault.app)"}

    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.status == 200:
                    return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait_time = (attempt + 1) * 3
                print(f"    [Rate limit 429] Esperando {wait_time}s antes de reintentar...")
                time.sleep(wait_time)
            else:
                print(f"    [HTTP {e.code}] Error en {page_title}: {e}")
                break
        except Exception as e:
            print(f"    [Error] {page_title}: {e}")
            break
        time.sleep(1)

    return {}

def main():
    print(f"🎮 Extrayendo información de {len(ALL_GAMES)} juegos desde Wikipedia REST API...")
    extracted_games = []

    NAMESPACE_NINTENDO = uuid.UUID("a3b89e72-5b91-4e4b-9c7f-1d8f2a4e9b60")

    for idx, item in enumerate(ALL_GAMES, 1):
        title = item["title"]
        page = item["wiki_page"]
        print(f"[{idx}/{len(ALL_GAMES)}] Obteniendo: {title} ({item['platform']})...")
        
        wiki_data = fetch_wikipedia_info(page)

        game_id = str(uuid.uuid5(NAMESPACE_NINTENDO, f"{item['platform_slug']}-{title}"))
        description = wiki_data.get("extract", "").strip()
        thumbnail = wiki_data.get("thumbnail", {}).get("source", "")
        if not thumbnail:
            thumbnail = wiki_data.get("originalimage", {}).get("source", "")

        game_record = {
            "id": game_id,
            "title": title,
            "platform": item["platform"],
            "platform_slug": item["platform_slug"],
            "genre": item["genre"],
            "genre_slug": item["genre_slug"],
            "release_year": item["release_year"],
            "developer": item["developer"],
            "description": description,
            "image_url": thumbnail,
            "source_url": f"https://en.wikipedia.org/wiki/{page}"
        }
        extracted_games.append(game_record)
        time.sleep(0.8) # Polite delay for Wikipedia rate limits

    # Guardar JSON
    json_path = "seed_games.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(extracted_games, f, indent=2, ensure_ascii=False)
    print(f"✅ Archivo JSON generado: {json_path} ({len(extracted_games)} juegos)")

    # Copiar también en nextjs/data/games.json
    with open("nextjs/data/games.json", "w", encoding="utf-8") as f:
        json.dump(extracted_games, f, indent=2, ensure_ascii=False)

    # Generar SQL para Supabase
    sql_path = "supabase_setup.sql"
    with open(sql_path, "w", encoding="utf-8") as f:
        f.write("-- Setup y Seed de Base de Datos para Nintendo Vault en Supabase\n\n")
        f.write("-- 1. Crear tabla 'games' si no existe\n")
        f.write("CREATE TABLE IF NOT EXISTS public.games (\n")
        f.write("    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),\n")
        f.write("    title TEXT NOT NULL,\n")
        f.write("    platform TEXT NOT NULL,\n")
        f.write("    platform_slug TEXT NOT NULL,\n")
        f.write("    genre TEXT NOT NULL,\n")
        f.write("    genre_slug TEXT NOT NULL,\n")
        f.write("    release_year INTEGER NOT NULL,\n")
        f.write("    developer TEXT NOT NULL,\n")
        f.write("    description TEXT NOT NULL,\n")
        f.write("    image_url TEXT NOT NULL,\n")
        f.write("    source_url TEXT,\n")
        f.write("    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL\n")
        f.write(");\n\n")

        f.write("-- Si la tabla ya existía sin platform, agregar columnas necesarias\n")
        f.write("ALTER TABLE public.games ADD COLUMN IF NOT EXISTS platform TEXT DEFAULT 'Nintendo 64';\n")
        f.write("ALTER TABLE public.games ADD COLUMN IF NOT EXISTS platform_slug TEXT DEFAULT 'n64';\n\n")

        f.write("-- 2. Habilitar Row Level Security (RLS)\n")
        f.write("ALTER TABLE public.games ENABLE ROW LEVEL SECURITY;\n\n")

        f.write("-- 3. Política de lectura pública (SELECT)\n")
        f.write("DROP POLICY IF EXISTS \"Public Read Games\" ON public.games;\n")
        f.write("DROP POLICY IF EXISTS \"Permitir lectura pública de juegos\" ON public.games;\n")
        f.write("CREATE POLICY \"Public Read Games\"\n")
        f.write("    ON public.games\n")
        f.write("    FOR SELECT\n")
        f.write("    USING (true);\n\n")

        f.write("-- 4. Poblar datos oficiales (Upsert usando id)\n")
        f.write("INSERT INTO public.games (id, title, platform, platform_slug, genre, genre_slug, release_year, developer, description, image_url, source_url)\n")
        f.write("VALUES\n")

        values_clauses = []
        for g in extracted_games:
            t = g['title'].replace("'", "''")
            plat = g['platform'].replace("'", "''")
            plat_slug = g['platform_slug'].replace("'", "''")
            genre = g['genre'].replace("'", "''")
            genre_slug = g['genre_slug'].replace("'", "''")
            dev = g['developer'].replace("'", "''")
            desc = g['description'].replace("'", "''")
            img = g['image_url'].replace("'", "''")
            src = g['source_url'].replace("'", "''")
            values_clauses.append(
                f"('{g['id']}', '{t}', '{plat}', '{plat_slug}', '{genre}', '{genre_slug}', {g['release_year']}, '{dev}', '{desc}', '{img}', '{src}')"
            )

        f.write(",\n".join(values_clauses))
        f.write("\nON CONFLICT (id) DO UPDATE SET\n")
        f.write("    title = EXCLUDED.title,\n")
        f.write("    platform = EXCLUDED.platform,\n")
        f.write("    platform_slug = EXCLUDED.platform_slug,\n")
        f.write("    genre = EXCLUDED.genre,\n")
        f.write("    genre_slug = EXCLUDED.genre_slug,\n")
        f.write("    release_year = EXCLUDED.release_year,\n")
        f.write("    developer = EXCLUDED.developer,\n")
        f.write("    description = EXCLUDED.description,\n")
        f.write("    image_url = EXCLUDED.image_url,\n")
        f.write("    source_url = EXCLUDED.source_url;\n")

    print(f"✅ Archivo SQL generado: {sql_path}")

if __name__ == "__main__":
    main()
