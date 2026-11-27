import { act, cleanup, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, test, vi } from "vitest";

import { SituacaoDoServidor } from "./SituacaoDoServidor";

function respostaJson(status: number, corpo: unknown): Response {
  return new Response(JSON.stringify(corpo), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}

// Respostas falsas da API: o fetch é trocado antes de cada teste.
function responder(status: number, corpo: unknown): void {
  vi.stubGlobal("fetch", () => Promise.resolve(respostaJson(status, corpo)));
}

// Uma API que só responde quando o teste mandar.
function responderQuandoLiberar(): { liberar?: (resposta: Response) => void } {
  const controle: { liberar?: (resposta: Response) => void } = {};
  vi.stubGlobal(
    "fetch",
    () =>
      new Promise<Response>((resolver) => {
        controle.liberar = resolver;
      }),
  );
  return controle;
}

// Uma API que nunca responde: a requisição só termina se for cancelada.
function nuncaResponder(): void {
  vi.stubGlobal(
    "fetch",
    (requisicao: Request) =>
      new Promise((_resolver, rejeitar) => {
        requisicao.signal.addEventListener("abort", () => {
          rejeitar(new DOMException("cancelada", "AbortError"));
        });
      }),
  );
}

function mensagem(): string | null {
  return screen.getByRole("status").textContent;
}

afterEach(() => {
  cleanup();
  vi.useRealTimers();
  vi.unstubAllGlobals();
});

describe("SituacaoDoServidor", () => {
  test("FUND-10: mostra 'Verificando o servidor…' até a resposta chegar", async () => {
    nuncaResponder();
    vi.useFakeTimers();

    render(<SituacaoDoServidor />);
    expect(mensagem()).toBe("Verificando o servidor…");

    await act(async () => {
      await vi.advanceTimersByTimeAsync(4999);
    });
    expect(mensagem()).toBe("Verificando o servidor…");
  });

  test("FUND-11: com 200 e situacao ok, mostra 'Servidor no ar'", async () => {
    responder(200, { situacao: "ok" });

    render(<SituacaoDoServidor />);

    expect(await screen.findByText("Servidor no ar")).toBeTruthy();
  });

  test("FUND-12 status 503: mostra 'Servidor fora do ar'", async () => {
    responder(503, { situacao: "indisponivel" });

    render(<SituacaoDoServidor />);

    expect(await screen.findByText("Servidor fora do ar")).toBeTruthy();
  });

  test("FUND-12 corpo inesperado: 200 sem situacao ok mostra 'Servidor fora do ar'", async () => {
    responder(200, { situacao: "talvez" });

    render(<SituacaoDoServidor />);

    expect(await screen.findByText("Servidor fora do ar")).toBeTruthy();
  });

  test("FUND-12 sem resposta em 5 segundos: mostra 'Servidor fora do ar'", async () => {
    nuncaResponder();
    vi.useFakeTimers();

    render(<SituacaoDoServidor />);
    await act(async () => {
      await vi.advanceTimersByTimeAsync(4999);
    });
    expect(mensagem()).toBe("Verificando o servidor…");

    await act(async () => {
      await vi.advanceTimersByTimeAsync(1);
    });
    expect(mensagem()).toBe("Servidor fora do ar");
  });

  test("FUND-13: a mensagem fica numa região role='status', anunciada por leitores de tela", async () => {
    const api = responderQuandoLiberar();

    render(<SituacaoDoServidor />);
    const regiao = screen.getByRole("status");
    expect(regiao.textContent).toBe("Verificando o servidor…");

    await act(async () => {
      api.liberar?.(respostaJson(200, { situacao: "ok" }));
      await Promise.resolve();
    });
    await screen.findByText("Servidor no ar");

    // A mesma região, agora com a mensagem nova: é a troca que o leitor de tela anuncia.
    expect(screen.getByRole("status")).toBe(regiao);
    expect(regiao.textContent).toBe("Servidor no ar");
  });
});
