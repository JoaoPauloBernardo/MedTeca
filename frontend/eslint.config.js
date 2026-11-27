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
        // Código do navegador (tsconfig.json) e código que roda no Node,
        // como a configuração do Vite (tsconfig.node.json).
        project: ["./tsconfig.json", "./tsconfig.node.json"],
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
      // HTML montado a partir de texto é barrado em todas as formas que dá
      // para ver no código (seção 6.G.1). Props espalhadas vindas de fora
      // ({...props}) não dão para ver: aí vale a revisão.
      "no-restricted-syntax": [
        "error",
        {
          selector: "JSXAttribute[name.name='dangerouslySetInnerHTML']",
          message: "HTML injetado no React é barrado (seção 6.G.1).",
        },
        {
          selector: "Property[key.name='dangerouslySetInnerHTML']",
          message: "HTML injetado no React é barrado, também num objeto de props (seção 6.G.1).",
        },
        {
          selector: "AssignmentExpression[left.property.name=/^(innerHTML|outerHTML)$/]",
          message: "Gravar HTML direto no DOM é barrado (seção 6.G.1).",
        },
        {
          selector: "CallExpression[callee.property.name='insertAdjacentHTML']",
          message: "Gravar HTML direto no DOM é barrado (seção 6.G.1).",
        },
        {
          selector:
            "CallExpression[callee.object.name='document'][callee.property.name=/^(write|writeln)$/]",
          message: "document.write é barrado (seção 6.G.1).",
        },
      ],
    },
  },
  {
    // Arquivos JavaScript ficam fora da checagem de tipos, mas continuam
    // com as outras regras; o .jsx entra aqui para não escapar do lint.
    files: ["**/*.{js,jsx,mjs,cjs}"],
    extends: [tseslint.configs.disableTypeChecked],
    rules: {
      // A versão com tipos desta regra fica desligada acima; esta não precisa deles.
      "no-implied-eval": "error",
    },
  },
);
