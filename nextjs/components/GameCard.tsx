import Link from "next/link";
import Image from "next/image";
import { Game } from "@/types/game";

const PLATFORM_STYLES: Record<string, { bg: string; text: string; border: string }> = {
  n64: { bg: "bg-red-950/70", text: "text-red-300", border: "border-red-700" },
  gba: { bg: "bg-purple-950/70", text: "text-purple-300", border: "border-purple-700" },
  nds: { bg: "bg-cyan-950/70", text: "text-cyan-300", border: "border-cyan-700" },
  wii: { bg: "bg-blue-950/70", text: "text-blue-300", border: "border-blue-700" },
};

export default function GameCard({
  game,
  isSpinning = false,
}: {
  game: Game;
  isSpinning?: boolean;
}) {
  const pStyle = PLATFORM_STYLES[game.platform_slug] || {
    bg: "bg-neutral-900",
    text: "text-neutral-300",
    border: "border-neutral-700",
  };

  return (
    <article
      className={`group relative flex flex-col bg-[#161a2b] border-2 ${
        isSpinning
          ? "border-yellow-400 shadow-[0_0_16px_rgba(250,204,21,0.35)] -translate-y-1"
          : "border-neutral-800"
      } hover:border-yellow-400 transition-all duration-300 hover:-translate-y-1 shadow-lg overflow-hidden`}
    >
      {/* Top Cartridge Notch decoration */}
      <div className="h-2 w-full bg-neutral-900 border-b border-neutral-800 flex justify-center gap-2 py-0.5">
        <span className="w-8 h-0.5 bg-neutral-700"></span>
        <span className="w-8 h-0.5 bg-neutral-700"></span>
      </div>

      {/* Game Image Banner */}
      <div className="relative w-full h-56 bg-neutral-950 overflow-hidden flex items-center justify-center p-3">
        {game.image_url ? (
          <Image
            src={game.image_url}
            alt={game.title}
            fill
            sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
            className="object-contain p-2 group-hover:scale-105 transition-transform duration-300"
            priority={false}
          />
        ) : (
          <div className="flex flex-col items-center justify-center text-neutral-600 font-pixel text-xs">
            <span>PORTADA OFICIAL</span>
          </div>
        )}

        {/* Insignia de consola animada secuencialmente */}
        <div className="absolute top-2 left-2">
          <Link
            href={`/plataforma/${game.platform_slug}`}
            className={`${
              isSpinning ? "console-badge-spinning ring-2 ring-yellow-400 brightness-125" : ""
            } px-2 py-0.5 font-mono text-[10px] font-bold uppercase rounded border ${pStyle.bg} ${pStyle.text} ${pStyle.border} shadow hover:brightness-125 transition-all`}
          >
            {game.platform}
          </Link>
        </div>

        <div className="absolute top-2 right-2">
          <span className="px-2 py-0.5 bg-black/80 border border-neutral-700 text-yellow-400 font-mono text-xs font-bold rounded shadow">
            {game.release_year}
          </span>
        </div>
      </div>

      {/* Card Content */}
      <div className="p-4 flex-1 flex flex-col justify-between space-y-3">
        <div>
          <div className="flex items-center justify-between gap-2 mb-2">
            <Link
              href={`/genero/${game.genre_slug}`}
              className="inline-block text-xs font-mono px-2 py-0.5 bg-neutral-900 text-neutral-300 border border-neutral-700 hover:border-yellow-400 hover:text-yellow-400 transition-colors uppercase"
            >
              {game.genre}
            </Link>
            <span className="text-xs font-mono text-neutral-400 truncate max-w-[130px]" title={game.developer}>
              {game.developer}
            </span>
          </div>

          <h3 className="font-pixel text-xs sm:text-sm text-yellow-300 group-hover:text-yellow-400 line-clamp-2 leading-relaxed">
            {game.title}
          </h3>

          <p className="mt-2 text-sm text-neutral-300 font-retro-body line-clamp-3 leading-snug">
            {game.description}
          </p>
        </div>

        <div className="pt-3 border-t border-neutral-800">
          <Link
            href={`/juego/${game.slug}`}
            className="w-full flex items-center justify-center py-2 px-3 bg-neutral-900 hover:bg-[#e60012] text-neutral-200 hover:text-white border border-neutral-700 hover:border-red-500 font-mono text-xs font-bold uppercase tracking-wider transition-colors"
          >
            VER FICHA TÉCNICA
          </Link>
        </div>
      </div>
    </article>
  );
}
