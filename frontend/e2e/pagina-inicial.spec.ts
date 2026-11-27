import AxeBuilder from "@axe-core/playwright";
import { expect, test } from "@playwright/test";

// A página inicial de ponta a ponta: navegador, Vite, Django e PostgreSQL de
// verdade, nos três perfis do playwright.config.ts (D-026).

test("FUND-01: a página mostra o título e 'Servidor no ar' vindo da API e do banco", async ({
  page,
}) => {
  await page.goto("/");

  await expect(page.getByRole("heading", { level: 1, name: "MedTeca" })).toBeVisible();
  await expect(page.getByRole("status")).toHaveText("Servidor no ar");
});

test("FUND-14: a página declara o idioma pt-BR", async ({ page }) => {
  await page.goto("/");

  await expect(page.locator("html")).toHaveAttribute("lang", "pt-BR");
});

test("FUND-15: toda requisição vai à origem da própria página, inclusive /api/saude", async ({
  page,
  baseURL,
}) => {
  const origemDaPagina = new URL(baseURL ?? "").origin;
  const requisicoes: string[] = [];
  page.on("request", (requisicao) => {
    requisicoes.push(requisicao.url());
  });

  await page.goto("/");
  await expect(page.getByRole("status")).toHaveText("Servidor no ar");

  expect(requisicoes).toContain(`${origemDaPagina}/api/saude`);
  const deOutraOrigem = requisicoes.filter((url) => new URL(url).origin !== origemDaPagina);
  expect(deOutraOrigem).toEqual([]);
});

// Regras da WCAG 2.0 a 2.2, níveis A e AA (RNF-01), mais as boas práticas do
// axe. As tags ligam também regras que o axe deixa desligadas por padrão,
// como a do tamanho de alvo da WCAG 2.2 (2.5.8).
const REGRAS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa", "best-practice"];

test("FUND-16: o axe-core não acha violação séria nem crítica", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByRole("status")).toHaveText("Servidor no ar");

  const resultado = await new AxeBuilder({ page }).withTags(REGRAS).analyze();

  // A regra de tamanho de alvo precisa ter rodado, para a checagem cobrir a WCAG 2.2.
  const regrasAvaliadas = [
    ...resultado.passes,
    ...resultado.violations,
    ...resultado.incomplete,
    ...resultado.inapplicable,
  ].map((regra) => regra.id);
  expect(regrasAvaliadas).toContain("target-size");

  const graves = resultado.violations
    .filter((violacao) => violacao.impact === "serious" || violacao.impact === "critical")
    .map((violacao) => `${violacao.id}: ${violacao.help}`);

  expect(graves).toEqual([]);
});
