import { useEffect, useState } from "react";

import { cliente } from "./api/cliente";

type Situacao = "verificando" | "no-ar" | "fora-do-ar";

const MENSAGENS: Record<Situacao, string> = {
  verificando: "Verificando o servidor…",
  "no-ar": "Servidor no ar",
  "fora-do-ar": "Servidor fora do ar",
};

// Sem resposta da API neste tempo, o servidor conta como fora do ar (FUND-12).
const LIMITE_EM_MS = 5000;

/**
 * Consulta /api/saude uma vez e mostra a situação do servidor (FUND-10 a
 * FUND-13). Só um 200 com situacao "ok" conta como no ar; qualquer outra
 * resposta, erro de rede ou demora acima do limite conta como fora do ar.
 */
export function SituacaoDoServidor() {
  const [situacao, setSituacao] = useState<Situacao>("verificando");

  useEffect(() => {
    // Depois que o componente sai da tela, nenhuma resposta muda o estado.
    let ativo = true;
    const controle = new AbortController();
    const temporizador = setTimeout(() => {
      controle.abort();
    }, LIMITE_EM_MS);

    async function verificar(): Promise<void> {
      try {
        const { data, response } = await cliente.GET("/api/saude", {
          signal: controle.signal,
        });
        if (ativo) {
          setSituacao(response.status === 200 && data?.situacao === "ok" ? "no-ar" : "fora-do-ar");
        }
      } catch {
        // Erro de rede ou cancelamento pelo limite de tempo.
        if (ativo) {
          setSituacao("fora-do-ar");
        }
      } finally {
        clearTimeout(temporizador);
      }
    }

    void verificar();

    return () => {
      ativo = false;
      clearTimeout(temporizador);
      controle.abort();
    };
  }, []);

  // A região role="status" faz os leitores de tela anunciarem a mudança (FUND-13).
  return <p role="status">{MENSAGENS[situacao]}</p>;
}
