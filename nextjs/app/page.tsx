import Link from "next/link";
import GameGrid from "@/components/GameGrid";
import { getGames, getPlatforms, getGenres } from "@/lib/supabase";

export const revalidate = 60;

export default async function HomePage() {
  const [{ games }, platforms, genres] = await Promise.all([
    getGames(),
    getPlatforms(),
    getGenres(),
  ]);

  return (
    <div className="space-y-12">
      {/* Hero Section */}
      <section className="relative overflow-hidden bg-gradient-to-b from-[#181c30] to-[#101322] border-4 border-neutral-800 p-6 sm:p-10 rounded-lg shadow-2xl">
        <div className="max-w-4xl space-y-4">
          <div className="inline-flex items-center gap-2 px-3 py-1 bg-red-600/20 border border-red-500/40 text-red-400 text-xs font-mono tracking-widest uppercase font-bold">
            COLECCIÓN OFICIAL NINTENDO
          </div>

          <h1 className="font-pixel text-xl sm:text-3xl text-yellow-400 leading-relaxed drop-shadow-md">
            BIBLIOTECA HISTÓRICA NINTENDO
          </h1>

          <p className="font-retro-body text-xl sm:text-2xl text-neutral-300 leading-relaxed">
            Una travesía cronológica por los videojuegos más influyentes de la historia de Nintendo.
            Explora títulos de cartucho y disco para <strong className="text-white">Game Boy Advance</strong>,
            <strong className="text-white"> Nintendo DS</strong>, <strong className="text-white">Nintendo 64</strong> y
            <strong className="text-white"> Wii</strong>.
          </p>

          <div className="pt-2 flex flex-wrap gap-4 font-mono text-xs text-neutral-400">
            <div className="px-3 py-1.5 bg-neutral-900/80 border border-neutral-700">
              <span className="text-white font-bold">{games.length}</span> TÍTULOS CATALOGADOS
            </div>
            <div className="px-3 py-1.5 bg-neutral-900/80 border border-neutral-700">
              <span className="text-white font-bold">{platforms.length}</span> PLATAFORMAS
            </div>
            <div className="px-3 py-1.5 bg-neutral-900/80 border border-neutral-700">
              <span className="text-white font-bold">{genres.length}</span> GÉNEROS
            </div>
          </div>
        </div>
      </section>

      {/* Platform Navigator Cards (No emojis, clean console names) */}
      <section className="space-y-4">
        <div className="flex items-center justify-between border-b-2 border-neutral-800 pb-2">
          <h2 className="font-pixel text-xs sm:text-sm text-yellow-400">
            EXPLORAR POR SISTEMA
          </h2>
          <span className="font-mono text-xs text-neutral-500 uppercase">
            SELECCIONA UNA CONSOLA
          </span>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
          {platforms.map((p) => (
            <Link
              key={p.slug}
              href={`/plataforma/${p.slug}`}
              className="group p-5 bg-[#141828] border-2 border-neutral-800 hover:border-yellow-400 rounded transition-all hover:-translate-y-1 shadow-md flex flex-col justify-between"
            >
              <div className="flex items-center justify-between mb-4">
                <span className="font-pixel text-xs text-red-500 font-bold tracking-wider">
                  [{p.code}]
                </span>
                <span className="text-[11px] font-mono px-2 py-0.5 bg-black/80 border border-neutral-700 text-neutral-300 rounded font-semibold">
                  {p.count} títulos
                </span>
              </div>
              <div>
                <h3 className="font-pixel text-xs sm:text-sm text-white group-hover:text-yellow-400 transition-colors">
                  {p.name}
                </h3>
                <span className="font-mono text-xs text-neutral-500 uppercase block mt-1">
                  Ver catálogo &gt;
                </span>
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* Genre Filter */}
      <section className="space-y-3">
        <div className="flex items-center justify-between">
          <h2 className="font-pixel text-xs sm:text-sm text-neutral-300">
            FILTRAR POR GÉNERO
          </h2>
        </div>

        <div className="flex flex-wrap gap-2">
          <Link
            href="/"
            className="px-3 py-1.5 bg-yellow-400 text-black font-mono text-xs font-bold uppercase tracking-wider hover:bg-yellow-300 transition-colors shadow"
          >
            TODOS ({games.length})
          </Link>
          {genres.map((g) => (
            <Link
              key={g.slug}
              href={`/genero/${g.slug}`}
              className="px-3 py-1.5 bg-neutral-900 border border-neutral-700 text-neutral-300 hover:border-yellow-400 hover:text-yellow-400 font-mono text-xs uppercase transition-all"
            >
              {g.name} ({g.count})
            </Link>
          ))}
        </div>
      </section>

      {/* Games Catalog Grid */}
      <section className="space-y-4">
        <div className="flex items-center justify-between border-b-2 border-neutral-800 pb-2">
          <h2 className="font-pixel text-sm sm:text-base text-white">
            CATÁLOGO GENERAL
          </h2>
          <span className="text-xs font-mono text-neutral-400 uppercase">
            {games.length} videojuegos disponibles
          </span>
        </div>

        <GameGrid games={games} />
      </section>
    </div>
  );
}
