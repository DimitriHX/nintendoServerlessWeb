#!/usr/bin/env python3
import json

GAME_SLUGS = {
    "Pokémon Emerald": "pokemon-emerald",
    "The Legend of Zelda: The Minish Cap": "zelda-minish-cap",
    "Metroid Fusion": "metroid-fusion",
    "Golden Sun": "golden-sun",
    "Castlevania: Aria of Sorrow": "castlevania-aria-of-sorrow",
    "Advance Wars": "advance-wars",
    "Mario & Luigi: Superstar Saga": "mario-luigi-superstar-saga",
    "Fire Emblem": "fire-emblem-blazing-blade",
    "Super Mario Advance 4: Super Mario Bros. 3": "super-mario-advance-4",
    "Mega Man Battle Network": "mega-man-battle-network",
    "Pokémon HeartGold and SoulSilver": "pokemon-heartgold-soulsilver",
    "Mario Kart DS": "mario-kart-ds",
    "The Legend of Zelda: Phantom Hourglass": "zelda-phantom-hourglass",
    "New Super Mario Bros.": "new-super-mario-bros",
    "Castlevania: Dawn of Sorrow": "castlevania-dawn-of-sorrow",
    "Pokémon Platinum": "pokemon-platinum",
    "Professor Layton and the Curious Village": "profesor-layton-villa-misteriosa",
    "The World Ends with You": "the-world-ends-with-you",
    "Grand Theft Auto: Chinatown Wars": "gta-chinatown-wars",
    "Phoenix Wright: Ace Attorney": "phoenix-wright-ace-attorney",
    "Super Mario Galaxy": "super-mario-galaxy",
    "Super Mario Galaxy 2": "super-mario-galaxy-2",
    "The Legend of Zelda: Twilight Princess": "zelda-twilight-princess",
    "The Legend of Zelda: Skyward Sword": "zelda-skyward-sword",
    "Super Smash Bros. Brawl": "super-smash-bros-brawl",
    "Metroid Prime 3: Corruption": "metroid-prime-3",
    "Mario Kart Wii": "mario-kart-wii",
    "Xenoblade Chronicles": "xenoblade-chronicles",
    "Donkey Kong Country Returns": "donkey-kong-country-returns",
    "Wii Sports": "wii-sports",
    "Super Mario 64": "super-mario-64",
    "The Legend of Zelda: Ocarina of Time": "zelda-ocarina-of-time",
    "GoldenEye 007": "goldeneye-007",
    "Mario Kart 64": "mario-kart-64",
    "Super Smash Bros.": "super-smash-bros-64",
    "Banjo-Kazooie": "banjo-kazooie",
    "Star Fox 64": "star-fox-64",
    "Pokémon Snap": "pokemon-snap",
    "The Legend of Zelda: Majora's Mask": "zelda-majoras-mask",
    "Paper Mario": "paper-mario-64"
}

def main():
    print("Actualizando slugs amigables para los 40 juegos...")

    with open("seed_games.json", "r", encoding="utf-8") as f:
        games = json.load(f)

    for g in games:
        title = g["title"]
        slug = GAME_SLUGS.get(title)
        if not slug:
            raise ValueError(f"Falta slug para: {title}")
        g["slug"] = slug

    # Guardar seed_games.json
    with open("seed_games.json", "w", encoding="utf-8") as f:
        json.dump(games, f, indent=2, ensure_ascii=False)
    print("seed_games.json actualizado")

    # Guardar nextjs/data/games.json
    with open("nextjs/data/games.json", "w", encoding="utf-8") as f:
        json.dump(games, f, indent=2, ensure_ascii=False)
    print("nextjs/data/games.json actualizado")

    # Actualizar supabase_setup.sql
    with open("supabase_setup.sql", "w", encoding="utf-8") as f:
        f.write("-- Setup y Seed de Base de Datos para Nintendo Vault en Supabase\n\n")
        f.write("-- 1. Crear tabla 'games' si no existe\n")
        f.write("CREATE TABLE IF NOT EXISTS public.games (\n")
        f.write("    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),\n")
        f.write("    slug TEXT UNIQUE NOT NULL,\n")
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

        f.write("-- Asegurar columnas si la tabla ya existía previamente\n")
        f.write("ALTER TABLE public.games ADD COLUMN IF NOT EXISTS slug TEXT;\n")
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

        f.write("-- 4. Poblar datos oficiales con slugs legibles (Upsert usando id)\n")
        f.write("INSERT INTO public.games (id, slug, title, platform, platform_slug, genre, genre_slug, release_year, developer, description, image_url, source_url)\n")
        f.write("VALUES\n")

        values_clauses = []
        for g in games:
            t = g['title'].replace("'", "''")
            plat = g['platform'].replace("'", "''")
            plat_slug = g['platform_slug'].replace("'", "''")
            genre = g['genre'].replace("'", "''")
            genre_slug = g['genre_slug'].replace("'", "''")
            dev = g['developer'].replace("'", "''")
            desc = g['description'].replace("'", "''")
            img = g['image_url'].replace("'", "''")
            src = g['source_url'].replace("'", "''")
            slug = g['slug'].replace("'", "''")
            values_clauses.append(
                f"('{g['id']}', '{slug}', '{t}', '{plat}', '{plat_slug}', '{genre}', '{genre_slug}', {g['release_year']}, '{dev}', '{desc}', '{img}', '{src}')"
            )

        f.write(",\n".join(values_clauses))
        f.write("\nON CONFLICT (id) DO UPDATE SET\n")
        f.write("    slug = EXCLUDED.slug,\n")
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

    print("supabase_setup.sql actualizado exitosamente con slugs")

if __name__ == "__main__":
    main()
