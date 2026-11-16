import { render, renderHook, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { memo } from "react";
import { describe, expect, it, vi } from "vitest";
import { ThemeProvider, useTheme } from "./ThemeContext";

function Label({ id }: { id: string }) {
  const { theme } = useTheme();
  return <span data-testid={id}>{theme}</span>;
}

function Switch() {
  const { toggle } = useTheme();
  return <button onClick={toggle}>Switch</button>;
}

describe("ThemeContext", () => {
  it("defaults to light and exposes it through data-theme", () => {
    const { container } = render(
      <ThemeProvider>
        <Label id="a" />
      </ThemeProvider>,
    );
    expect(screen.getByTestId("a")).toHaveTextContent("light");
    expect(container.querySelector("[data-theme]")).toHaveAttribute("data-theme", "light");
  });

  it("accepts an initial theme", () => {
    render(
      <ThemeProvider initial="dark">
        <Label id="a" />
      </ThemeProvider>,
    );
    expect(screen.getByTestId("a")).toHaveTextContent("dark");
  });

  it("toggles for every consumer at once, however deep they are", async () => {
    const user = userEvent.setup();
    const { container } = render(
      <ThemeProvider>
        <Label id="a" />
        <div>
          <div>
            <Label id="b" />
          </div>
        </div>
        <Switch />
      </ThemeProvider>,
    );
    await user.click(screen.getByRole("button", { name: "Switch" }));
    expect(screen.getByTestId("a")).toHaveTextContent("dark");
    expect(screen.getByTestId("b")).toHaveTextContent("dark");
    expect(container.querySelector("[data-theme]")).toHaveAttribute("data-theme", "dark");
    await user.click(screen.getByRole("button", { name: "Switch" }));
    expect(screen.getByTestId("a")).toHaveTextContent("light");
  });

  it("throws a helpful error outside a provider", () => {
    const errors = vi.spyOn(console, "error").mockImplementation(() => {});
    expect(() => renderHook(() => useTheme())).toThrow("useTheme must be used within ThemeProvider");
    errors.mockRestore();
  });

  it("does not re-render consumers when only an unrelated parent re-renders", () => {
    let renders = 0;
    function Counted() {
      const { theme } = useTheme();
      renders++;
      return <span>{theme}</span>;
    }
    const Memoised = memo(Counted);
    const { rerender } = render(
      <ThemeProvider>
        <Memoised />
      </ThemeProvider>,
    );
    const before = renders;
    rerender(
      <ThemeProvider>
        <Memoised />
      </ThemeProvider>,
    );
    expect(renders).toBe(before);
  });
});
