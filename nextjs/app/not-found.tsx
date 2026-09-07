import Link from "next/link";

export default function NotFound() {
  return (
    <div className="min-h-[50vh] flex flex-col items-center justify-center space-y-6 py-16 text-center">
      <div className="p-8 bg-[#181510] border-4 border-yellow-500 rounded-lg max-w-lg w-full space-y-4 shadow-2xl">
        <div className="inline-block px-3 py-1 bg-yellow-950 border border-yellow-600 text-yellow-400 font-pixel text-xs font-bold">
          [ ERROR 404 ]
        </div>

        <h2 className="font-pixel text-base sm:text-lg text-yellow-400 mt-2">
          TÍTULO NO ENCONTRADO
        </h2>

        <p className="font-retro-body text-xl text-neutral-300">
          El videojuego o categoría solicitada no se encuentra registrada en el archivo.
        </p>

        <div className="pt-4">
          <Link
            href="/"
            className="px-5 py-2.5 bg-yellow-400 hover:bg-yellow-300 text-black font-mono text-xs font-bold uppercase transition-colors inline-block"
          >
            VOLVER AL CATÁLOGO
          </Link>
        </div>
      </div>
    </div>
  );
}
