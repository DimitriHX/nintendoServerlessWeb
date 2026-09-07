import type { Metadata } from "next";
import { notFound } from "next/navigation";
import Image from "next/image";
import Link from "next/link";
import { getGameBySlug, getAdjacentGames } from "@/lib/supabase";

interface PageProps {
  params: Promise<{ slug: string }>;
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { slug } = await params;
  const { game } = await getGameBySlug(slug);

  if (!game) {
    return {
      title: "Juego no encontrado | Nintendo Retro Vault",
    };
  }

  return {
    title: `${game.title} (${game.platform}, ${game.release_year}) | Nintendo Retro Vault`,
    description: game.description.slice(0, 160),
  };
}

export default async function GameDetailPage({ params }: PageProps) {
  const { slug } = await params;
  const [{ game }, adjacent] = await Promise.all([
    getGameBySlug(slug),
    getAdjacentGames(slug),
  ]);

  if (!game) {
    notFound();
  }

  const { prev, next } = adjacent;

  return (
    <div className="space-y-8">
      {/* Breadcrumb navigation */}
      <nav className="flex items-center gap-2 font-mono text-xs text-neutral-400 uppercase">
        <Link href="/" className="hover:text-yellow-400 transition-colors">
          INICIO
        </Link>
        <span>/</span>
        <Link
          href={`/plataforma/${game.platform_slug}`}
          className="hover:text-yellow-400 transition-colors"
        >
          {game.platform}
        </Link>
        <span>/</span>
        <Link
          href={`/genero/${game.genre_slug}`}
          className="hover:text-yellow-400 transition-colors"
        >
          {game.genre}
        </Link>
        <span>/</span>
        <span className="text-neutral-200 truncate">{game.title}</span>
      </nav>

      {/* Main Cartridge / Disc Detail Card */}
      <article className="bg-[#141828] border-4 border-neutral-800 p-6 sm:p-8 rounded-lg shadow-2xl space-y-8">
        <div className="grid grid-cols-1 md:grid-cols-12 gap-8 items-start">
          {/* Cover Art Column */}
          <div className="md:col-span-5 flex flex-col items-center">
            <div className="relative w-full max-w-sm aspect-[4/3] bg-neutral-950 border-4 border-neutral-700 rounded-md overflow-hidden shadow-inner flex items-center justify-center p-4">
              {game.image_url ? (
                <Image
                  src={game.image_url}
                  alt={game.title}
                  fill
                  sizes="(max-width: 768px) 100vw, 40vw"
                  className="object-contain p-2"
                  priority
                />
              ) : (
                <span className="font-pixel text-xs text-neutral-600">SIN PORTADA DISPONIBLE</span>
              )}
            </div>

            {/* Cuadro estilístico de la consola con animación de giro cada 3s */}
            <div className="mt-5 flex flex-col items-center">
              <Link
                href={`/plataforma/${game.platform_slug}`}
                className="console-badge-spin group flex items-center gap-2 px-4 py-1.5 bg-neutral-900 border-2 border-yellow-400 text-yellow-400 font-pixel text-xs font-bold uppercase rounded shadow-[0_0_12px_rgba(250,204,21,0.25)] hover:bg-yellow-400 hover:text-black transition-colors"
                title={`Ver catálogo de ${game.platform}`}
              >
                <span>SISTEMA:</span>
                <span className="text-white font-bold ml-1">
                  {game.platform}
                </span>
              </Link>
              <span className="text-[10px] font-mono text-neutral-500 uppercase mt-1">
                Ficha oficial archivada
              </span>
            </div>
          </div>

          {/* Details Column */}
          <div className="md:col-span-7 space-y-6">
            <div>
              <div className="flex flex-wrap items-center gap-2.5 mb-3">
                {/* Cuadro de consola con animación sutil */}
                <Link
                  href={`/plataforma/${game.platform_slug}`}
                  className="console-badge-spin px-3 py-1 bg-yellow-400 text-black font-mono text-xs font-bold uppercase rounded hover:bg-yellow-300 transition-colors shadow"
                >
                  {game.platform}
                </Link>
                <Link
                  href={`/genero/${game.genre_slug}`}
                  className="px-3 py-1 bg-blue-950 border border-blue-600 text-blue-300 font-mono text-xs uppercase hover:bg-blue-900 transition-colors font-bold"
                >
                  {game.genre}
                </Link>
                <span className="px-3 py-1 bg-black/60 border border-neutral-700 text-neutral-300 font-mono text-xs font-bold">
                  AÑO {game.release_year}
                </span>
              </div>

              <h1 className="font-pixel text-xl sm:text-2xl text-yellow-400 leading-relaxed">
                {game.title}
              </h1>
            </div>

            {/* Technical Specs Box */}
            <div className="bg-neutral-950/80 border border-neutral-800 p-4 font-mono text-xs space-y-2">
              <div className="text-yellow-400 font-bold border-b border-neutral-800 pb-1 uppercase tracking-wider flex justify-between items-center">
                <span>ESPECIFICACIONES TÉCNICAS</span>
                <span className="text-neutral-500 font-normal text-[11px]">/{game.slug}</span>
              </div>
              <div className="grid grid-cols-2 gap-2 text-neutral-300">
                <div><span className="text-neutral-500">PLATAFORMA:</span> {game.platform}</div>
                <div><span className="text-neutral-500">GÉNERO:</span> {game.genre}</div>
                <div><span className="text-neutral-500">DESARROLLADOR:</span> {game.developer}</div>
                <div><span className="text-neutral-500">AÑO DE SALIDA:</span> {game.release_year}</div>
              </div>
            </div>

            {/* Synopsis / Description */}
            <div className="space-y-2">
              <h2 className="font-pixel text-xs text-neutral-400 uppercase tracking-wider">
                SINOPSIS HISTÓRICA
              </h2>
              <p className="font-retro-body text-xl sm:text-2xl text-neutral-200 leading-relaxed">
                {game.description}
              </p>
            </div>

            {/* Action Bar with Navigation Buttons */}
            <div className="pt-6 border-t border-neutral-800 space-y-4">
              {/* Fila principal: Anterior ficha (izq) | Registro Enciclopédico sin flechas (medio) | Ficha Siguiente (der) */}
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 font-mono text-xs font-bold uppercase items-center text-center">
                {/* 1. Anterior Ficha */}
                {prev ? (
                  <Link
                    href={`/juego/${prev.slug}`}
                    className="w-full px-3.5 py-2.5 bg-neutral-900 border border-neutral-700 hover:border-yellow-400 hover:text-yellow-400 transition-all text-center block"
                    title={`Anterior: ${prev.title}`}
                  >
                    &lt; ANTERIOR FICHA
                  </Link>
                ) : (
                  <span className="w-full px-3.5 py-2.5 bg-neutral-950 border border-neutral-900 text-neutral-600 block text-center cursor-not-allowed">
                    &lt; ANTERIOR FICHA
                  </span>
                )}

                {/* 2. Registro Enciclopédico (en medio, sin flechas) */}
                {game.source_url ? (
                  <a
                    href={game.source_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="w-full px-4 py-2.5 bg-neutral-950 border border-neutral-800 text-neutral-300 hover:text-white hover:border-neutral-600 transition-colors text-center block tracking-wider"
                  >
                    REGISTRO ENCICLOPÉDICO
                  </a>
                ) : (
                  <div></div>
                )}

                {/* 3. Ficha Siguiente */}
                {next ? (
                  <Link
                    href={`/juego/${next.slug}`}
                    className="w-full px-3.5 py-2.5 bg-neutral-900 border border-neutral-700 hover:border-yellow-400 hover:text-yellow-400 transition-all text-center block"
                    title={`Siguiente: ${next.title}`}
                  >
                    FICHA SIGUIENTE &gt;
                  </Link>
                ) : (
                  <span className="w-full px-3.5 py-2.5 bg-neutral-950 border border-neutral-900 text-neutral-600 block text-center cursor-not-allowed">
                    FICHA SIGUIENTE &gt;
                  </span>
                )}
              </div>

              {/* Abajo de registro enciclopédico: Volver a [PLATAFORMA] */}
              <div className="flex justify-center pt-1 font-mono text-xs font-bold uppercase">
                <Link
                  href={`/plataforma/${game.platform_slug}`}
                  className="w-full sm:w-auto sm:min-w-[280px] px-5 py-2.5 bg-neutral-900 border-2 border-neutral-700 hover:border-red-500 hover:text-white transition-all text-center text-neutral-300"
                >
                  VOLVER A {game.platform}
                </Link>
              </div>

              {/* Quick Peek of Prev/Next Titles */}
              <div className="flex justify-between text-[11px] font-mono text-neutral-500 px-1 pt-1">
                {prev ? (
                  <span className="truncate max-w-[45%]">&lt; {prev.title}</span>
                ) : (
                  <span></span>
                )}
                {next ? (
                  <span className="truncate max-w-[45%] text-right">{next.title} &gt;</span>
                ) : (
                  <span></span>
                )}
              </div>
            </div>
          </div>
        </div>
      </article>
    </div>
  );
}
