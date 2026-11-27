import { cleanup, render, screen } from "@testing-library/react";
import { afterEach, expect, test, vi } from "vitest";

import { PaginaInicial } from "./PaginaInicial";

afterEach(() => {
  cleanup();
  vi.unstubAllGlobals();
});

test("FUND-01: a página mostra o título MedTeca e a situação do servidor", () => {
  // A API não responde neste teste: o que importa é a página montada.
  vi.stubGlobal("fetch", () => new Promise<Response>(() => undefined));

  render(<PaginaInicial />);

  expect(screen.getByRole("heading", { level: 1, name: "MedTeca" })).toBeTruthy();
  expect(screen.getByRole("status").textContent).toBe("Verificando o servidor…");
});
