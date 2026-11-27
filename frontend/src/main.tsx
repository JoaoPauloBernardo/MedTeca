import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import { PaginaInicial } from "./PaginaInicial";

const raiz = document.getElementById("raiz");
if (raiz === null) {
  throw new Error("O index.html precisa do elemento #raiz.");
}

createRoot(raiz).render(
  <StrictMode>
    <PaginaInicial />
  </StrictMode>,
);
