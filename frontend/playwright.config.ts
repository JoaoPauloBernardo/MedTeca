import { defineConfig, devices } from "@playwright/test";

// Testes de ponta a ponta (D-026): Chromium, e WebKit com os perfis de iPhone
// e iPad, contra a página que o serviço web do Compose serve. Rodam no
// serviço e2e, com a imagem oficial do Playwright:
//   docker compose up -d --wait db api web
//   docker compose --profile e2e run --rm e2e
export default defineConfig({
  testDir: "./e2e",
  forbidOnly: true,
  retries: 0,
  // O WebKit no contêiner é lento: com o padrão de 30 s e todos os testes em
  // paralelo, a verificação do axe estourava o tempo de vez em quando.
  timeout: 60_000,
  expect: { timeout: 10_000 },
  workers: 2,
  reporter: [["list"], ["html", { open: "never", outputFolder: "playwright-report" }]],
  use: {
    baseURL: process.env.MEDTECA_URL ?? "http://web:5173",
    trace: "retain-on-failure",
  },
  // O navegador é declarado em cada projeto: se o nome de um aparelho mudar
  // numa versão nova do Playwright, o teste falha em vez de trocar o WebKit
  // pelo Chromium sem ninguém ver.
  projects: [
    { name: "chromium", use: { ...devices["Desktop Chrome"], browserName: "chromium" } },
    { name: "webkit-iphone", use: { ...devices["iPhone 17"], browserName: "webkit" } },
    { name: "webkit-ipad", use: { ...devices["iPad (gen 11)"], browserName: "webkit" } },
  ],
});
