export default function Loading() {
  return (
    <div className="min-h-[50vh] flex flex-col items-center justify-center space-y-6 py-16">
      {/* Retro Cartridge Loading Animation */}
      <div className="relative">
        <div className="w-16 h-16 bg-neutral-900 border-4 border-yellow-400 flex items-center justify-center animate-bounce shadow-[0_0_20px_rgba(250,204,21,0.4)]">
          <span className="font-pixel text-xs text-yellow-400 font-bold">NV</span>
        </div>
        <div className="absolute -bottom-2 left-1/2 -translate-x-1/2 w-12 h-1 bg-black/50 blur-sm rounded-full"></div>
      </div>

      <div className="text-center space-y-2">
        <p className="font-pixel text-xs sm:text-sm text-yellow-400 tracking-widest animate-pulse uppercase">
          CARGANDO ARCHIVO...
        </p>
        <p className="font-mono text-xs text-neutral-500 uppercase">
          Sincronizando información de la biblioteca
        </p>
      </div>

      {/* Retro Skeleton Grid */}
      <div className="w-full max-w-5xl grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 pt-6 opacity-40">
        {[1, 2, 3, 4].map((i) => (
          <div
            key={i}
            className="h-72 bg-neutral-900/60 border-2 border-neutral-800 animate-pulse rounded"
          ></div>
        ))}
      </div>
    </div>
  );
}
