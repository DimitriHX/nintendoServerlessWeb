import { createClient } from "@supabase/supabase-js";
import { Game, PlatformInfo, GenreInfo } from "@/types/game";
import fallbackGames from "@/data/games.json";

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || "";
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || "";

export const isSupabaseConfigured = Boolean(
  supabaseUrl &&
  supabaseAnonKey &&
  !supabaseUrl.includes("placeholder")
);

export const supabase = isSupabaseConfigured
  ? createClient(supabaseUrl, supabaseAnonKey)
  : null;

const PLATFORM_CODES: Record<string, string> = {
  gba: "GBA",
  nds: "NDS",
  n64: "N64",
  wii: "WII",
};

/**
 * Obtiene todos los juegos de la base de datos
 */
export async function getGames(): Promise<{ games: Game[]; isLive: boolean }> {
  if (isSupabaseConfigured && supabase) {
    try {
      const { data, error } = await supabase
        .from("games")
        .select("*")
        .order("release_year", { ascending: true });

      if (!error && data && data.length > 0) {
        return { games: data as Game[], isLive: true };
      }
    } catch {
      // Fallback silencioso
    }
  }

  return { games: fallbackGames as Game[], isLive: false };
}

/**
 * Obtiene un juego por su slug amigable (o por ID como fallback)
 */
export async function getGameBySlug(slug: string): Promise<{ game: Game | null; isLive: boolean }> {
  const cleanSlug = decodeURIComponent(slug).toLowerCase().trim();

  if (isSupabaseConfigured && supabase) {
    try {
      // Intentar primero por slug
      const { data, error } = await supabase
        .from("games")
        .select("*")
        .eq("slug", cleanSlug)
        .maybeSingle();

      if (!error && data) {
        return { game: data as Game, isLive: true };
      }

      // Fallback por id si el slug era un UUID
      const { data: dataById } = await supabase
        .from("games")
        .select("*")
        .eq("id", cleanSlug)
        .maybeSingle();

      if (dataById) {
        return { game: dataById as Game, isLive: true };
      }
    } catch {
      // Fallback silencioso
    }
  }

  const list = fallbackGames as Game[];
  const found =
    list.find((g) => g.slug === cleanSlug || g.id === cleanSlug) ||
    list.find((g) => g.slug === `super-${cleanSlug}`) ||
    list.find((g) => g.slug.endsWith(cleanSlug)) ||
    null;
  return { game: found, isLive: false };
}

/**
 * Obtiene los juegos anterior y siguiente en la secuencia para navegación fluida
 */
export async function getAdjacentGames(
  currentSlug: string,
  filterPlatform?: string
): Promise<{ prev: Game | null; next: Game | null }> {
  const { games } = await getGames();
  const list = filterPlatform
    ? games.filter((g) => g.platform_slug.toLowerCase() === filterPlatform.toLowerCase())
    : games;

  if (list.length <= 1) {
    return { prev: null, next: null };
  }

  const clean = decodeURIComponent(currentSlug).toLowerCase().trim();
  const currentIndex = list.findIndex((g) => g.slug === clean || g.id === clean);

  if (currentIndex === -1) {
    return { prev: null, next: null };
  }

  const prevIndex = (currentIndex - 1 + list.length) % list.length;
  const nextIndex = (currentIndex + 1) % list.length;

  return {
    prev: list[prevIndex],
    next: list[nextIndex],
  };
}

/**
 * Obtiene juegos por plataforma
 */
export async function getGamesByPlatform(platformSlug: string): Promise<{
  games: Game[];
  platformName: string;
  isLive: boolean;
}> {
  const normalizedSlug = decodeURIComponent(platformSlug).toLowerCase().trim();

  if (isSupabaseConfigured && supabase) {
    try {
      const { data, error } = await supabase
        .from("games")
        .select("*")
        .ilike("platform_slug", normalizedSlug)
        .order("release_year", { ascending: true });

      if (!error && data && data.length > 0) {
        return { games: data as Game[], platformName: data[0].platform, isLive: true };
      }
    } catch {
      // Fallback silencioso
    }
  }

  const filtered = (fallbackGames as Game[]).filter(
    (g) => g.platform_slug.toLowerCase() === normalizedSlug
  );
  const platformName = filtered.length > 0 ? filtered[0].platform : platformSlug.toUpperCase();

  return { games: filtered, platformName, isLive: false };
}

/**
 * Obtiene juegos por género
 */
export async function getGamesByGenre(genreSlug: string): Promise<{
  games: Game[];
  genreName: string;
  isLive: boolean;
}> {
  const normalizedSlug = decodeURIComponent(genreSlug).toLowerCase().trim();

  if (isSupabaseConfigured && supabase) {
    try {
      const { data, error } = await supabase
        .from("games")
        .select("*")
        .ilike("genre_slug", normalizedSlug)
        .order("release_year", { ascending: true });

      if (!error && data && data.length > 0) {
        return { games: data as Game[], genreName: data[0].genre, isLive: true };
      }
    } catch {
      // Fallback silencioso
    }
  }

  const filtered = (fallbackGames as Game[]).filter(
    (g) => g.genre_slug.toLowerCase() === normalizedSlug
  );
  const genreName = filtered.length > 0 ? filtered[0].genre : genreSlug;

  return { games: filtered, genreName, isLive: false };
}

/**
 * Lista de plataformas disponibles con conteo
 */
export async function getPlatforms(): Promise<PlatformInfo[]> {
  const { games } = await getGames();
  const map = new Map<string, { name: string; slug: string; count: number }>();

  games.forEach((g) => {
    const slug = g.platform_slug.toLowerCase();
    if (map.has(slug)) {
      map.get(slug)!.count += 1;
    } else {
      map.set(slug, { name: g.platform, slug: g.platform_slug, count: 1 });
    }
  });

  return Array.from(map.values()).map((p) => ({
    ...p,
    code: PLATFORM_CODES[p.slug] || p.slug.toUpperCase(),
  }));
}

/**
 * Lista de géneros disponibles con conteo
 */
export async function getGenres(): Promise<GenreInfo[]> {
  const { games } = await getGames();
  const map = new Map<string, { name: string; slug: string; count: number }>();

  games.forEach((g) => {
    const slug = g.genre_slug.toLowerCase();
    if (map.has(slug)) {
      map.get(slug)!.count += 1;
    } else {
      map.set(slug, { name: g.genre, slug: g.genre_slug, count: 1 });
    }
  });

  return Array.from(map.values());
}
