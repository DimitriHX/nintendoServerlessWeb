import type { Metadata } from "next";
import { Press_Start_2P, VT323 } from "next/font/google";
import Link from "next/link";
import "./globals.css";

const pressStart = Press_Start_2P({
  weight: "400",
  subsets: ["latin"],
  variable: "--font-press-start",
  display: "swap",
});

const vt323 = VT323({
  weight: "400",
  subsets: ["latin"],
  variable: "--font-vt323",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Nintendo Retro Vault | Catálogo Histórico",
  description: "Archivo histórico de videojuegos oficiales de Nintendo para Game Boy Advance, Nintendo DS, Nintendo 64 y Wii.",
  keywords: ["Nintendo", "Retro", "GBA", "NDS", "N64", "Wii", "Catálogo"],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html
      lang="es"
      className={`${pressStart.variable} ${vt323.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col bg-[#0b0d14] text-slate-200">
        {/* Top Header Bar */}
        <div className="bg-[#e60012] text-white text-[11px] font-mono py-1 px-4 text-center tracking-widest font-semibold uppercase">
          ARCHIVO HISTÓRICO DE VIDEOJUEGOS NINTENDO
        </div>

        {/* Main Navbar */}
        <header className="sticky top-0 z-50 border-b-4 border-neutral-800 bg-[#121624]/95 backdrop-blur shadow-xl">
          <div className="max-w-7xl mx-auto px-4 py-3 sm:px-6 flex flex-wrap items-center justify-between gap-4">
            <Link href="/" className="flex items-center gap-3 group">
              <div className="w-8 h-8 bg-neutral-900 border-2 border-red-600 flex items-center justify-center text-red-500 font-pixel text-xs font-bold">
                NV
              </div>
              <div>
                <span className="font-pixel text-xs sm:text-sm text-yellow-400 group-hover:text-white transition-colors tracking-wider block">
                  NINTENDO VAULT
                </span>
                <span className="text-[10px] text-neutral-400 tracking-widest uppercase block font-mono">
                  GBA • NDS • N64 • WII
                </span>
              </div>
            </Link>

            <nav className="flex flex-wrap items-center gap-2 sm:gap-2.5 text-xs font-mono">
              <Link
                href="/"
                className="px-2.5 py-1 bg-neutral-900 border border-neutral-700 hover:border-yellow-400 hover:text-yellow-400 transition-colors uppercase font-bold"
              >
                TODOS
              </Link>
              <Link
                href="/plataforma/gba"
                className="px-2.5 py-1 bg-purple-950/60 border border-purple-800 text-purple-300 hover:bg-purple-900 transition-colors uppercase font-bold"
              >
                GBA
              </Link>
              <Link
                href="/plataforma/nds"
                className="px-2.5 py-1 bg-cyan-950/60 border border-cyan-800 text-cyan-300 hover:bg-cyan-900 transition-colors uppercase font-bold"
              >
                NDS
              </Link>
              <Link
                href="/plataforma/n64"
                className="px-2.5 py-1 bg-red-950/60 border border-red-800 text-red-300 hover:bg-red-900 transition-colors uppercase font-bold"
              >
                N64
              </Link>
              <Link
                href="/plataforma/wii"
                className="px-2.5 py-1 bg-blue-950/60 border border-blue-800 text-blue-300 hover:bg-blue-900 transition-colors uppercase font-bold"
              >
                WII
              </Link>
            </nav>
          </div>
        </header>

        {/* Content */}
        <main className="flex-1 max-w-7xl w-full mx-auto px-4 py-8 sm:px-6">
          {children}
        </main>

        {/* Production Footer */}
        <footer className="border-t-4 border-neutral-800 bg-[#07090e] py-8 text-center text-neutral-400 font-mono text-sm">
          <div className="max-w-7xl mx-auto px-4 space-y-3">
            <div className="flex flex-wrap justify-center items-center gap-3 text-xs">
              <span className="font-pixel text-[10px] text-red-500">NINTENDO VAULT</span>
              <span>•</span>
              <Link href="/plataforma/gba" className="hover:text-yellow-400">Game Boy Advance</Link>
              <span>•</span>
              <Link href="/plataforma/nds" className="hover:text-yellow-400">Nintendo DS</Link>
              <span>•</span>
              <Link href="/plataforma/n64" className="hover:text-yellow-400">Nintendo 64</Link>
              <span>•</span>
              <Link href="/plataforma/wii" className="hover:text-yellow-400">Nintendo Wii</Link>
            </div>
            <p className="text-xs text-neutral-500 max-w-2xl mx-auto">
              Todas las marcas registradas, títulos, personajes e imágenes asociadas son propiedad
              intelectual de Nintendo Co., Ltd. y de sus respectivos desarrolladores y distribuidores.
            </p>
          </div>
        </footer>
      </body>
    </html>
  );
}
