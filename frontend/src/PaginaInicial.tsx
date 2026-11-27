import { SituacaoDoServidor } from "./SituacaoDoServidor";

/**
 * Página inicial provisória da fundação: o título e a situação do servidor.
 * As telas de verdade chegam com o sistema de design (D-036).
 */
export function PaginaInicial() {
  return (
    <main>
      <h1>MedTeca</h1>
      <SituacaoDoServidor />
    </main>
  );
}
