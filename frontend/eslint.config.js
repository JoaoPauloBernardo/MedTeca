// Lint do frontend (seção 6.D): typescript-eslint com checagem de tipos,
// regras dos hooks do React, acessibilidade (jsx-a11y) e padrões perigosos
// barrados (seção 6.G.1).
import js from "@eslint/js";
import { defineConfig } from "eslint/config";
import jsxA11y from "eslint-plugin-jsx-a11y";
import reactHooks from "eslint-plugin-react-hooks";
import globals from "globals";
import tseslint from "typescript-eslint";

export default defineConfig(
  {
    ignores: ["dist", "playwright-report", "test-results", "src/api/esquema.d.ts"],
  },
  js.configs.recommended,
  tseslint.configs.strictTypeChecked,
  {
    languageOptions: {
      globals: globals.browser,
      parserOptions: {
        projectService: true,
        tsconfigRootDir: import.meta.dirname,
      },
    },
  },
  reactHooks.configs.flat.recommended,
  jsxA11y.flatConfigs.strict,
  {
    rules: {
      "no-eval": "error",
      "no-new-func": "error",
      "no-restricted-syntax": [
        "error",
        {
          selector: "JSXAttribute[name.name='dangerouslySetInnerHTML']",
          message: "HTML injetado no React é barrado (seção 6.G.1).",
        },
      ],
    },
  },
  {
    // Arquivos JavaScript de configuração ficam fora da checagem de tipos.
    files: ["**/*.js"],
    extends: [tseslint.configs.disableTypeChecked],
  },
);
