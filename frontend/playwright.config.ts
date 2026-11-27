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
  reporter: [["list"], ["html", { open: "never", outputFolder: "playwright-report" }]],
  use: {
    baseURL: process.env.MEDTECA_URL ?? "http://web:5173",
    trace: "retain-on-failure",
  },
  projects: [
    { name: "chromium", use: { ...devices["Desktop Chrome"] } },
    { name: "webkit-iphone", use: { ...devices["iPhone 17"] } },
    { name: "webkit-ipad", use: { ...devices["iPad (gen 11)"] } },
  ],
});
