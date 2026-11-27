import createClient from "openapi-fetch";

import type { paths } from "./esquema";

// Cliente da API com os tipos gerados do OpenAPI do Django Ninja (FUND-17).
// A base é a origem da própria página, então as chamadas ficam na mesma
// origem (D-020, FUND-15). Ela é absoluta porque fora do navegador, nos
// testes, um endereço relativo não forma uma requisição válida.
export const cliente = createClient<paths>({
  baseUrl: window.location.origin,
  // O fetch é procurado a cada chamada, e não guardado quando o cliente é
  // criado: assim os testes conseguem trocá-lo depois de importar o módulo.
  fetch: (requisicao: Request) => globalThis.fetch(requisicao),
});
