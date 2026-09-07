import type { Metadata } from "next";
import { notFound } from "next/navigation";
import Link from "next/link";
import GameGrid from "@/components/GameGrid";
import { getGamesByPlatform, getPlatforms } from "@/lib/supabase";

interface PageProps {
  params: Promise<{ slug: string }>;
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { slug } = await params;
  const { platformName, games } = await getGamesByPlatform(slug);

  return {
    title: `${platformName} (${games.length} juegos) | Nintendo Retro Vault`,
    description: `Catálogo de videojuegos lanzados para ${platformName}.`,
  };
}

export default async function PlatformPage({ params }: PageProps) {
  const { slug } = await params;
  const [{ games, platformName }, platforms] = await Promise.all([
    getGamesByPlatform(slug),
    getPlatforms(),
  ]);

  if (games.length === 0) {
    notFound();
  }

  return (
    <div className="space-y-8">
      {/* Breadcrumbs */}
      <nav className="flex items-center gap-2 font-mono text-xs text-neutral-400 uppercase">
        <Link href="/" className="hover:text-yellow-400 transition-colors">
          INICIO
        </Link>
        <span>/</span>
        <span className="text-neutral-500">PLATAFORMA</span>
        <span>/</span>
        <span className="text-yellow-400 font-bold">{platformName}</span>
      </nav>

      {/* Header Banner */}
      <div className="bg-[#141828] border-4 border-neutral-800 p-6 sm:p-8 rounded-lg shadow-xl space-y-4">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div>
            <span className="text-xs font-mono text-yellow-400 uppercase tracking-widest block mb-1 font-bold">
              SISTEMA DE ENTRETENIMIENTO
            </span>
            <h1 className="font-pixel text-xl sm:text-2xl text-white">
              {platformName.toUpperCase()}
            </h1>
          </div>

          <div className="px-4 py-2 bg-neutral-900 border border-neutral-700 text-yellow-400 font-mono text-xs font-bold uppercase rounded">
            {games.length} {games.length === 1 ? "TÍTULO DISPONIBLE" : "TÍTULOS DISPONIBLES"}
          </div>
        </div>

        {/* Other platforms selector */}
        <div className="pt-3 border-t border-neutral-800 flex flex-wrap items-center gap-2">
          <span className="text-xs font-mono text-neutral-400 uppercase">OTRAS CONSOLAS:</span>
          <Link
            href="/"
            className="px-2.5 py-1 bg-neutral-900 border border-neutral-700 text-neutral-300 hover:border-yellow-400 hover:text-yellow-400 font-mono text-xs uppercase transition-colors"
          >
            TODAS
          </Link>
          {platforms.map((p) => (
            <Link
              key={p.slug}
              href={`/plataforma/${p.slug}`}
              className={`px-3 py-1 border font-mono text-xs uppercase transition-colors ${
                p.slug.toLowerCase() === slug.toLowerCase()
                  ? "bg-yellow-400 text-black font-bold border-yellow-400"
                  : "bg-neutral-900 border-neutral-700 text-neutral-300 hover:border-yellow-400 hover:text-yellow-400"
              }`}
            >
              {p.name} ({p.count})
            </Link>
          ))}
        </div>
      </div>

      {/* Games Grid */}
      <section className="space-y-4">
        <GameGrid games={games} />
      </section>
    </div>
  );
}
