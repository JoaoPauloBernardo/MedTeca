import createClient from "openapi-fetch";

import type { paths } from "./esquema";

// Cliente da API com os tipos gerados do OpenAPI do Django Ninja (FUND-17).
// Sem baseUrl: as chamadas vão para a mesma origem da página (D-020, FUND-15).
export const cliente = createClient<paths>({ baseUrl: "" });
