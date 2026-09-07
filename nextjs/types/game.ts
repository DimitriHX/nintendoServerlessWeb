export interface Game {
  id: string;
  slug: string;
  title: string;
  platform: string;
  platform_slug: string;
  genre: string;
  genre_slug: string;
  release_year: number;
  developer: string;
  description: string;
  image_url: string;
  source_url?: string;
  created_at?: string;
}

export interface PlatformInfo {
  name: string;
  slug: string;
  code: string;
  count: number;
}

export interface GenreInfo {
  name: string;
  slug: string;
  count: number;
}
