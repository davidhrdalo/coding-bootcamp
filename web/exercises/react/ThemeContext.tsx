/**
 * React 7: context
 *
 * Context shares a value with every component below a provider, without passing props
 * through each level.
 *
 *   <ThemeProvider initial="dark"> ... any depth ... const { theme, toggle } = useTheme() </ThemeProvider>
 *
 * Build:
 * - ThemeProvider({ children, initial = "light" }): holds the theme ("light" | "dark") in
 *   state and renders <div data-theme={theme}>{children}</div>.
 * - useTheme() -> { theme, toggle }. toggle() switches light <-> dark. Every component that
 *   uses useTheme sees the same, current value.
 * - Using useTheme OUTSIDE a ThemeProvider must throw an Error with the message
 *   "useTheme must be used within ThemeProvider".
 * - Keep the context value from changing identity on every render unless the theme changed
 *   (useMemo), so consumers do not re-render needlessly.
 *
 * Concepts: createContext, Provider, custom hook around useContext, failing loudly.
 */
import type { ReactNode } from "react";

export type Theme = "light" | "dark";

export function ThemeProvider(props: { children: ReactNode; initial?: Theme }) {
  return null;
}

export function useTheme(): { theme: Theme; toggle: () => void } {
  throw new Error("Not implemented yet");
}
