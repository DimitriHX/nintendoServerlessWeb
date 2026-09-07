#!/usr/bin/env python3
import json

SPANISH_DESCRIPTIONS = {
    # --- GBA ---
    "Pokémon Emerald": (
        "Pokémon Esmeralda es un videojuego de rol de 2004 desarrollado por Game Freak y publicado por "
        "The Pokémon Company y Nintendo para Game Boy Advance. Es la versión definitiva y ampliada de la "
        "tercera generación en la región de Hoenn, incorporando la emblemática Batalla de la Frontera (Frente de Batalla) "
        "y la trama centrada en el legendario Rayquaza para calmar el conflicto entre Groudon y Kyogre."
    ),
    "The Legend of Zelda: The Minish Cap": (
        "The Legend of Zelda: The Minish Cap es un juego de acción y aventura desarrollado por Capcom y "
        "Flagship junto a Nintendo para Game Boy Advance. Narra el origen de la Espada Cuádruple y el malvado "
        "hechicero Vaati, introduciendo a Ezero, un sombrero mágico parlante que otorga a Link la habilidad de encogerse "
        "al diminuto tamaño de la raza Minish para explorar templos y mazmorras ocultas."
    ),
    "Metroid Fusion": (
        "Metroid Fusion es un videojuego de acción y aventura de desplazamiento lateral lanzado en 2002 para "
        "Game Boy Advance. Desarrollado por Nintendo R&D1, pone a los jugadores al mando de la cazarrecompensas "
        "Samus Aran, quien debe investigar los laboratorios de investigación biológica BSL infectados por el parásito X, "
        "mientras es acechada incansablemente por el SA-X, un clon letal con su máximo poder."
    ),
    "Golden Sun": (
        "Golden Sun es un aclamado videojuego de rol lanzado en 2001 por Camelot Software Planning y Nintendo "
        "para Game Boy Advance. Sigue la odisea de un grupo de jóvenes Adeptos liderados por Hans (Isaac) que dominan "
        "la Psinergía y deben recorrer el mundo de Weyard para evitar que los cuatro faros elementales sean encendidos, "
        "lo que liberaría el destructivo poder primordial de la Alquimia."
    ),
    "Castlevania: Aria of Sorrow": (
        "Castlevania: Aria of Sorrow es un juego de acción y exploración de estilo 'Metroidvania' publicado por Konami "
        "en 2003 para Game Boy Advance. Ambientado en el año 2035, sigue a Soma Cruz, un estudiante atrapado en el castillo "
        "de Drácula durante un eclipse solar, quien posee el exclusivo 'Poder del Dominio' que le permite absorber y utilizar "
        "las almas y habilidades de los monstruos derrotados."
    ),
    "Advance Wars": (
        "Advance Wars es un célebre videojuego de estrategia táctica por turnos desarrollado por Intelligent Systems "
        "y lanzado en 2001 para Game Boy Advance. Los jugadores asumen el rol de Oficiales en Jefe (CO) del ejército "
        "de Orange Star, dirigiendo unidades terrestres, marítimas y aéreas a través de cuadrículas estratégicas "
        "para neutralizar a las fuerzas enemigas y asegurar cuarteles clave."
    ),
    "Mario & Luigi: Superstar Saga": (
        "Mario & Luigi: Superstar Saga es un juego de rol cómico desarrollado por AlphaDream y lanzado en 2003 para "
        "Game Boy Advance. Los hermanos fontaneros viajan al Reino Judía para recuperar la voz robada de la Princesa Peach "
        "de manos de la bruja Cackletta y su secuaz Fawful, utilizando un innovador sistema de combate por turnos sincronizado "
        "donde cada botón controla a un hermano simultáneamente."
    ),
    "Fire Emblem": (
        "Fire Emblem: The Blazing Blade es un videojuego de rol táctico desarrollado por Intelligent Systems y "
        "lanzado en 2003 para Game Boy Advance, siendo el primer título de la aclamada saga en ser localizado "
        "y publicado internacionalmente. Sigue a Lyn, Eliwood y Hector en una conspiración a gran escala en el continente "
        "de Elibe, combinando combate por cuadrículas estratégicas con muerte permanente de personajes."
    ),
    "Super Mario Advance 4: Super Mario Bros. 3": (
        "Super Mario Advance 4: Super Mario Bros. 3 es una adaptación completa y remasterizada del legendario clásico "
        "de NES para Game Boy Advance, lanzada en 2003. Incluye gráficos y audio renovados, mecánicas de transformación "
        "como Mario Tanuki y Mario Rana, física pulida y compatibilidad con niveles especiales mediante la tecnología e-Reader."
    ),
    "Mega Man Battle Network": (
        "Mega Man Battle Network es un videojuego de rol táctico en tiempo real creado por Capcom en 2001 para "
        "Game Boy Advance. Ambientado en una sociedad hiperconectada de los años 2000, los jugadores controlan a Lan Hikari "
        "y a su programa de inteligencia artificial MegaMan.EXE, combatiendo virus informáticos y amenazas cibernéticas en "
        "una cuadrícula virtual dinámica de 3x3 utilizando chips de batalla coleccionables."
    ),

    # --- NDS ---
    "Pokémon HeartGold and SoulSilver": (
        "Pokémon HeartGold y SoulSilver son remakes magistrales lanzados en 2009 para Nintendo DS de los clásicos Oro y Plata. "
        "Ambientados en las regiones de Johto y Kanto, reinventaron la experiencia con gráficos tridimensionales mejorados, "
        "la mecánica de llevar a cualquier Pokémon acompañante caminando fuera de su Poké Ball y eventos cinematográficos "
        "protagonizados por Lugia y Ho-Oh."
    ),
    "Mario Kart DS": (
        "Mario Kart DS es una entrega histórica lanzada en 2005 para Nintendo DS. Introdujo por primera vez el juego multijugador "
        "en línea a través de la Conexión Wi-Fi de Nintendo, el modo Misiones exclusivo, la doble pantalla para radar y táctica, "
        "y pistas retro clásicas junto a legendarios circuitos nuevos como la Fortaleza Aérea (Airship Fortress)."
    ),
    "The Legend of Zelda: Phantom Hourglass": (
        "The Legend of Zelda: Phantom Hourglass es una aventura directa de acción secuela de The Wind Waker, desarrollada "
        "por Nintendo EAD y lanzada en 2007 para Nintendo DS. Aprovechó de forma revolucionaria la pantalla táctil y el lápiz stylus "
        "para controlar los movimientos de Link, trazar la trayectoria del búmeran, navegar en barco y explorar el desafiante Templo del Rey del Mar."
    ),
    "New Super Mario Bros.": (
        "New Super Mario Bros. es un videojuego de plataformas de desplazamiento lateral en 2.5D lanzado en 2006 para "
        "Nintendo DS. Marcó el esperado regreso de Mario al formato tradicional en 2D por primera vez desde Super Mario World, "
        "incorporando transformaciones gigantes como el Mega Champiñón y un apartado visual renovado que vendió más de 30 millones de copias."
    ),
    "Castlevania: Dawn of Sorrow": (
        "Castlevania: Dawn of Sorrow es la secuela directa de Aria of Sorrow, desarrollada por Konami en 2005 para Nintendo DS. "
        "Continúa la historia de Soma Cruz enfrentando a una peligrosa secta que busca resucitar a un nuevo señor oscuro, "
        "aprovechando la pantalla táctil para dibujar 'Sellos Mágicos' que encierran a los jefes y gestionando el sistema de almas con el mapa en pantalla superior."
    ),
    "Pokémon Platinum": (
        "Pokémon Platino es la versión mejorada de la cuarta generación en la región de Sinnoh, lanzada en 2008 para Nintendo DS. "
        "Destaca por la inclusión del Mundo Distorsión, un reino con gravedad alterada y perspectiva cambiante, la historia ampliada "
        "en torno a Giratina en su Forma Origen, la reaparición del Frente de Batalla y mejoras en la velocidad del combate."
    ),
    "Professor Layton and the Curious Village": (
        "El profesor Layton y la villa misteriosa es un aclamado juego de puzles y misterio desarrollado por Level-5 en 2007 "
        "para Nintendo DS. Sigue al arqueólogo británico Hershel Layton y a su aprendiz Luke en la villa de Saint-Mystère, "
        "resolviendo más de un centenar de ingeniosos acertijos integrados orgánicamente en una trama cautivadora estilo novela animada."
    ),
    "The World Ends with You": (
        "The World Ends with You es un innovador juego de rol de acción urbano desarrollado por Square Enix y Jupiter en 2007 "
        "para Nintendo DS. Ambientado en el bullicioso distrito de Shibuya en Tokio, los jugadores siguen a Neku Sakuraba en el mortal "
        "'Juego de los Segadores', utilizando simultáneamente la pantalla táctil inferior y los botones para controlar combates sincronizados en ambas pantallas."
    ),
    "Grand Theft Auto: Chinatown Wars": (
        "Grand Theft Auto: Chinatown Wars es un juego de acción de mundo abierto desarrollado por Rockstar Leeds y Rockstar North "
        "en 2009 para Nintendo DS. Con una perspectiva cenital modernizada y sombreado cel-shading, sigue a Huang Lee en Liberty City "
        "haciendo un uso magistral de la pantalla táctil para robar vehículos, armar cócteles molotov y gestionar el submundo del comercio clandestino."
    ),
    "Phoenix Wright: Ace Attorney": (
        "Phoenix Wright: Ace Attorney es una novela visual y drama judicial interactivo desarrollado por Capcom en 2005 para "
        "Nintendo DS. Los jugadores encarnan al novato abogado defensor Phoenix Wright, investigando escenas de crímenes, "
        "interrogando testigos y gritando ¡Protesto! en el micrófono de la consola para exponer contradicciones lógicas en tribunales implacables."
    ),

    # --- WII ---
    "Super Mario Galaxy": (
        "Super Mario Galaxy es una obra maestra de plataformas en 3D desarrollada por Nintendo EAD Tokio y lanzada en 2007 "
        "para Wii. Revolucionó los juegos de plataformas al introducir mecánicas de gravedad esférica entre planetas y galaxias, "
        "acompañado de una banda sonora orquestada en vivo y el uso del mando Wii Remote para recoger trozos de estrella y realizar giros espaciales."
    ),
    "Super Mario Galaxy 2": (
        "Super Mario Galaxy 2 es la continuación del aclamado juego espacial, lanzada por Nintendo en 2010 para Wii. "
        "Eleva el diseño de niveles a su máxima expresión creativa con nuevos potenciadores como Mario Nube y Mario Roca, "
        "además del regreso estelar del dinosaurio Yoshi con habilidades gravitacionales propias para devorar enemigos y superar retos plataformeros exigentes."
    ),
    "The Legend of Zelda: Twilight Princess": (
        "The Legend of Zelda: Twilight Princess es un juego de acción y aventura épico lanzado en 2006 para Wii como título "
        "de lanzamiento. Presenta un tono más maduro y oscuro en el reino de Hyrule, donde Link debe transformarse en lobo "
        "guiado por la misteriosa criatura Midna para liberar el mundo de la usurpación de las Sombras y restaurar la luz."
    ),
    "The Legend of Zelda: Skyward Sword": (
        "The Legend of Zelda: Skyward Sword fue lanzado en 2011 para Wii, celebrando el 25 aniversario de la franquicia. "
        "Narra el origen cronológico de la Espada Maestra y la leyenda de Hyrule, aprovechando la tecnología Wii MotionPlus "
        "para un control de espada preciso 1:1, donde cada corte y ángulo de ataque debe planificarse estratégicamente contra los enemigos."
    ),
    "Super Smash Bros. Brawl": (
        "Super Smash Bros. Brawl es la tercera entrega de la saga de lucha entre franquicias de Nintendo, lanzada en 2008 para Wii. "
        "Introdujo por primera vez personajes invitados de compañías externas como Sonic the Hedgehog y Solid Snake, el modo historia "
        "cinematográfico 'El emisario subespacial' y la mecánica de los Smash Finales que cambiaron el curso de cada combate."
    ),
    "Metroid Prime 3: Corruption": (
        "Metroid Prime 3: Corruption es la culminación de la trilogía Prime, desarrollada por Retro Studios y lanzada en 2007 para Wii. "
        "Aprovecha al máximo el puntero del Wii Remote para ofrecer una puntería y exploración inmersivas en primera persona, "
        "mientras Samus Aran combate la corrupción del Phazon en su cuerpo y se enfrenta a los cazarrecompensas oscuros y a Dark Samus."
    ),
    "Mario Kart Wii": (
        "Mario Kart Wii es uno de los videojuegos más vendidos de la historia, publicado por Nintendo en 2008. "
        "Introdujo por primera vez motocicletas con mecánicas de caballito y derrapes cerrados, carreras frenéticas de hasta 12 pilotos simultáneos, "
        "competencias en línea a nivel mundial y el accesorio Wii Wheel para control por movimiento intuitivo."
    ),
    "Xenoblade Chronicles": (
        "Xenoblade Chronicles es un aclamado juego de rol japonés de mundo abierto desarrollado por Monolith Soft y lanzado en 2010 "
        "para Wii. Ambientado sobre los cuerpos colosales de dos titanes petrificados, Bionis y Mechonis, sigue a Shulk y su legendaria espada "
        "Monado, capaz de prever el futuro inmediato para alterar el destino en un vasto mundo lleno de exploración y combate en tiempo real."
    ),
    "Donkey Kong Country Returns": (
        "Donkey Kong Country Returns es un sobresaliente juego de plataformas desarrollado por Retro Studios en 2010 para Wii. "
        "Revivió la icónica franquicia creada por Rare con un diseño de niveles implacable, gráficos vibrantes en 2.5D, modo cooperativo "
        "para dos jugadores controlando a Donkey Kong y Diddy Kong, y los clásicos niveles en carretas de mina y barriles cañón."
    ),
    "Wii Sports": (
        "Wii Sports es el histórico videojuego de simulación deportiva que acompañó a la consola Wii en su lanzamiento en 2006. "
        "Demostró el potencial de los controles de movimiento intuitivos a través de cinco disciplinas populares: tenis, béisbol, "
        "bolos, golf y boxeo, transformándose en un fenómeno cultural accesible para jugadores de todas las generaciones."
    ),

    # --- N64 ---
    "Super Mario 64": (
        "Super Mario 64 es el legendario videojuego de plataformas 3D desarrollado por Nintendo EAD y lanzado en 1996 para Nintendo 64. "
        "Estableció las bases fundamentales del movimiento de cámaras analógicas y el diseño de mundos abiertos tridimensionales en la industria. "
        "Mario debe explorar las pinturas mágicas del castillo de la Princesa Peach para recolectar las Estrellas de Poder y derrotar a Bowser."
    ),
    "The Legend of Zelda: Ocarina of Time": (
        "The Legend of Zelda: Ocarina of Time es ampliamente catalogado como uno de los mejores videojuegos jamás creados. Publicado en 1998 "
        "para Nintendo 64, introdujo el sistema de fijación de objetivos Z-Targeting y la mecánica de viajar en el tiempo siete años mediante "
        "la Ocarina del Tiempo y la Espada Maestra para detener al rey de las ladronas Ganondorf antes de que domine la Trifuerza."
    ),
    "GoldenEye 007": (
        "GoldenEye 007 es un revolucionario juego de disparos en primera persona desarrollado por Rare y lanzado en 1997 para Nintendo 64. "
        "Basado en la película de James Bond de 1995, redefinió el género en consolas al priorizar misiones con sigilo y objetivos tácticos, "
        "además de popularizar las legendarias partidas multijugador a cuatro bandas a pantalla dividida."
    ),
    "Mario Kart 64": (
        "Mario Kart 64 es el clásico videojuego de carreras desarrollado por Nintendo EAD y lanzado en 1996 para Nintendo 64. "
        "Dio el salto al modelado en tres dimensiones, introduciendo pistas emblemáticas como el Castillo de Bowser y la Senda Arcoíris, "
        "el temido caparazón azul con pinchos y soporte para carreras y batallas de globos de hasta 4 jugadores simultáneos."
    ),
    "Super Smash Bros.": (
        "Super Smash Bros. es el título original de lucha y celebración de personajes creado por HAL Laboratory y dirigido por Masahiro Sakurai "
        "en 1999 para Nintendo 64. Reunió por primera vez a íconos como Mario, Link, Samus, Pikachu y Donkey Kong en frenéticos combates donde el objetivo "
        "es acumular daño porcentual para expulsar a los adversarios de la arena."
    ),
    "Banjo-Kazooie": (
        "Banjo-Kazooie es una obra maestra de plataformas de recolección desarrollada por Rare y publicada en 1998 para Nintendo 64. "
        "Los jugadores guían al oso Banjo y a la descarada ave Kazooie a través de nueve mundos no lineales repletos de acertijos y piezas de rompecabezas (Jiggies) "
        "para rescatar a la pequeña Tooty de las garras de la bruja Gruntilda."
    ),
    "Star Fox 64": (
        "Star Fox 64 (conocido en Europa como Lylat Wars) es un aclamado juego de disparos espacial sobre rieles lanzado en 1997 para Nintendo 64. "
        "Puso a prueba los reflejos de los jugadores a bordo de la nave Arwing junto a Fox McCloud y su escuadrón, siendo el primer título en incorporar "
        "actuación de voz cinematográfica y el accesorio Rumble Pak para vibración inmersiva en el mando."
    ),
    "Pokémon Snap": (
        "Pokémon Snap es un innovador juego de fotografía y exploración en primera persona desarrollado por HAL Laboratory en 1999 para Nintendo 64. "
        "A bordo del vehículo todoterreno Zero-One en la Isla Pokémon, los jugadores deben capturar las mejores tomas de criaturas en su hábitat salvaje, "
        "utilizando manzanas y bombas de humo para provocar comportamientos únicos evaluados por el Profesor Oak."
    ),
    "The Legend of Zelda: Majora's Mask": (
        "The Legend of Zelda: Majora's Mask es la aclamada y oscura secuela directa de Ocarina of Time, lanzada en el año 2000 para Nintendo 64. "
        "Link queda atrapado en la tierra paralela de Términa, teniendo solo un ciclo recurrente de 72 horas para evitar que la Luna colisione contra la superficie, "
        "utilizando máscaras mágicas de transformación para alterar su forma y salvar a sus habitantes."
    ),
    "Paper Mario": (
        "Paper Mario es un encantador videojuego de rol desarrollado por Intelligent Systems y lanzado en el año 2000 para Nintendo 64. "
        "Combinó una original dirección de arte estilo papel en mundos tridimensionales con un sistema de combate dinámico de comandos de acción, "
        "donde Mario emprende una aventura junto a compañeros entrañables para recuperar los siete Espíritus Estelares arrebatados por Bowser."
    )
}

def update_all():
    print("Tradreciendo descripciones al español...")

    # 1. Cargar seed_games.json
    with open("seed_games.json", "r", encoding="utf-8") as f:
        games = json.load(f)

    updated_count = 0
    for g in games:
        title = g["title"]
        if title in SPANISH_DESCRIPTIONS:
            g["description"] = SPANISH_DESCRIPTIONS[title]
            updated_count += 1
        else:
            print(f"Alerta: No hay traducción para {title}")

    # Guardar seed_games.json
    with open("seed_games.json", "w", encoding="utf-8") as f:
        json.dump(games, f, indent=2, ensure_ascii=False)
    print(f"seed_games.json actualizado ({updated_count} descripciones en español)")

    # 2. Guardar nextjs/data/games.json
    with open("nextjs/data/games.json", "w", encoding="utf-8") as f:
        json.dump(games, f, indent=2, ensure_ascii=False)
    print("nextjs/data/games.json actualizado con descripciones en español")

    # 3. Actualizar supabase_setup.sql
    with open("supabase_setup.sql", "w", encoding="utf-8") as f:
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

        f.write("-- Asegurar columnas de plataforma\n")
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

        f.write("-- 4. Poblar datos oficiales en español (Upsert usando id)\n")
        f.write("INSERT INTO public.games (id, title, platform, platform_slug, genre, genre_slug, release_year, developer, description, image_url, source_url)\n")
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

    print("supabase_setup.sql actualizado exitosamente con descripciones en español")

if __name__ == "__main__":
    update_all()
