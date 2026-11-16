import { defineConfig } from "vitest/config";

// Runs every *.test.ts / *.test.tsx under exercises/ in a fake browser (jsdom).
// Reference solutions live in solutions/ and are never run by `npm test`.
export default defineConfig({
  esbuild: { jsx: "automatic" },
  test: {
    environment: "jsdom",
    globals: true,
    setupFiles: ["./setup.ts"],
    include: ["exercises/**/*.test.{ts,tsx}"],
    css: false,
  },
});
