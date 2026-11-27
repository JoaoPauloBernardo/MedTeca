import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// Servidor de desenvolvimento do MedTeca (design da fundação).
export default defineConfig({
  plugins: [react()],
  server: {
    host: "0.0.0.0",
    port: 5173,
    strictPort: true,
    // "web" é o nome do serviço no Compose, pelo qual o Playwright chega à
    // página (FUND-16). O Vite recusa nomes de host fora desta lista.
    allowedHosts: ["web"],
    // A API fica na mesma origem da página (D-020, FUND-15).
    proxy: { "/api": "http://api:8000" },
    // A pasta vem do Windows, e as mudanças só chegam ao contêiner por
    // varredura; a V43 mede o custo.
    watch: { usePolling: true, interval: 300 },
  },
});
