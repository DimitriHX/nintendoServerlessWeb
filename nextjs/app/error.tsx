"use client";

import Link from "next/link";

export default function ErrorBoundary({
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  return (
    <div className="min-h-[50vh] flex flex-col items-center justify-center space-y-6 py-16 text-center">
      <div className="p-8 bg-[#181014] border-4 border-red-600 rounded-lg max-w-lg w-full space-y-4 shadow-2xl">
        <div className="inline-block px-3 py-1 bg-red-950 border border-red-600 text-red-400 font-pixel text-xs font-bold">
          [ ERROR DEL SISTEMA ]
        </div>

        <h2 className="font-pixel text-base sm:text-lg text-red-500">
          FALLO DE LECTURA
        </h2>

        <p className="font-retro-body text-xl text-neutral-300">
          No fue posible procesar la solicitud en este momento. Por favor reintenta la operación o regresa al catálogo.
        </p>

        <div className="pt-4 flex flex-wrap justify-center gap-4">
          <button
            onClick={() => reset()}
            className="px-4 py-2 bg-red-600 hover:bg-red-700 text-white font-mono text-xs font-bold uppercase transition-colors cursor-pointer"
          >
            REINTENTAR
          </button>
          <Link
            href="/"
            className="px-4 py-2 bg-neutral-900 border border-neutral-700 hover:border-yellow-400 hover:text-yellow-400 font-mono text-xs uppercase transition-colors"
          >
            INICIO
          </Link>
        </div>
      </div>
    </div>
  );
}
