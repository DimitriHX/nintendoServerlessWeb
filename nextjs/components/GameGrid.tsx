"use client";

import { useState, useEffect } from "react";
import { Game } from "@/types/game";
import GameCard from "./GameCard";

const ITEMS_PER_TAB = 10;

export default function GameGrid({ games }: { games: Game[] }) {
  // Paginación por pestañas: 10 fichas por pestaña
  const [activeTab, setActiveTab] = useState<number>(0);

  const totalTabs = Math.max(1, Math.ceil(games.length / ITEMS_PER_TAB));

  // Asegurar que activeTab no se desborde si cambian los juegos
  const safeTab = Math.min(activeTab, totalTabs - 1);

  // Fichas de la pestaña activa únicamente
  const currentTabGames = games.slice(
    safeTab * ITEMS_PER_TAB,
    (safeTab + 1) * ITEMS_PER_TAB
  );

  const totalInCurrentTab = currentTabGames.length;

  // step: 0 hasta (totalInCurrentTab - 1) = fichas individuales
  // step === totalInCurrentTab = giran todas las fichas de la pestaña activa al unísono
  const [step, setStep] = useState<number>(0);

  // Reiniciar la secuencia cada vez que se cambie de pestaña o de listado
  useEffect(() => {
    setStep(0);

    if (totalInCurrentTab === 0) return;

    const timer = setInterval(() => {
      setStep((prev) => {
        // Si ya llegó al clímax donde giran todas, reinicia a la primera ficha
        if (prev >= totalInCurrentTab) {
          return 0;
        }
        return prev + 1;
      });
    }, 2000); // 2 segundos exactos por ficha

    return () => clearInterval(timer);
  }, [safeTab, totalInCurrentTab]);

  return (
    <div className="space-y-6">
      {/* Barra de control: Contador Secuencial e Información de Pestaña */}
      <div className="bg-[#121524] border-2 border-neutral-800 p-4 rounded-lg flex flex-wrap items-center justify-between gap-4">
        {/* Contador secuencial en tiempo real */}
        <div className="flex items-center gap-3">
          <span className="font-pixel text-[11px] text-neutral-400">
            CADENA SECUENCIAL:
          </span>
          <div className="px-3 py-1 bg-neutral-900 border border-neutral-700 rounded text-xs font-mono font-bold">
            {step < totalInCurrentTab ? (
              <span className="text-yellow-400">
                FICHA {step + 1} DE {totalInCurrentTab}
              </span>
            ) : (
              <span className="text-emerald-400 animate-pulse font-pixel text-[10px]">
                ★ GIRO TOTAL [{totalInCurrentTab} / {totalInCurrentTab}] ★
              </span>
            )}
          </div>
        </div>

        {/* Info de títulos y ciclo */}
        <div className="font-mono text-xs text-neutral-400 flex items-center gap-3">
          <span className="hidden sm:inline text-neutral-500">
            Ciclo: 2s por ficha • Clímax al finalizar la pestaña
          </span>
          <span className="px-2 py-0.5 bg-neutral-900 border border-neutral-800 rounded text-neutral-300">
            Mostrando {currentTabGames.length} de {games.length} títulos
          </span>
        </div>
      </div>

      {/* Selector de Pestañas (10 fichas por pestaña) */}
      {totalTabs > 1 && (
        <div className="flex flex-wrap items-center justify-center gap-2 p-2 bg-[#0e111d] border border-neutral-800 rounded">
          <span className="font-pixel text-[10px] text-neutral-400 mr-2 uppercase">
            SELECCIONAR PESTAÑA:
          </span>
          {Array.from({ length: totalTabs }).map((_, idx) => {
            const start = idx * ITEMS_PER_TAB + 1;
            const end = Math.min((idx + 1) * ITEMS_PER_TAB, games.length);
            const isActive = safeTab === idx;

            return (
              <button
                key={idx}
                type="button"
                onClick={() => {
                  setActiveTab(idx);
                  setStep(0);
                }}
                className={`px-3.5 py-1.5 font-mono text-xs font-bold uppercase transition-all cursor-pointer border ${
                  isActive
                    ? "bg-yellow-400 text-black border-yellow-400 shadow-[0_0_12px_rgba(250,204,21,0.35)]"
                    : "bg-neutral-900 text-neutral-300 border-neutral-700 hover:border-yellow-400 hover:text-yellow-400"
                }`}
              >
                PESTAÑA {idx + 1} ({start}-{end})
              </button>
            );
          })}
        </div>
      )}

      {/* Cuadrícula de 10 juegos de la pestaña activa */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {currentTabGames.map((game, index) => {
          // Si el paso es totalInCurrentTab, giran todas las fichas de la pestaña activa.
          // Si el paso es 0 a totalInCurrentTab - 1, gira únicamente la ficha en la posición index === step.
          const isSpinning = step === totalInCurrentTab || index === step;

          return (
            <GameCard
              key={game.id}
              game={game}
              isSpinning={isSpinning}
            />
          );
        })}
      </div>
    </div>
  );
}
