import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { beforeEach, describe, expect, it } from "vitest";
import { Picker, renderCounts, resetRenderCounts } from "./Picker";

const ROWS = [
  { id: "a", label: "Apple" },
  { id: "b", label: "Banana" },
  { id: "c", label: "Cherry" },
];

beforeEach(() => resetRenderCounts());

describe("Picker: behaviour (already works)", () => {
  it("shows the rows and the selection", async () => {
    const user = userEvent.setup();
    render(<Picker rows={ROWS} />);
    expect(screen.getByText("Selected: none")).toBeInTheDocument();
    await user.click(screen.getByRole("button", { name: "Banana" }));
    expect(screen.getByText("Selected: b")).toBeInTheDocument();
  });

  it("keeps the note text", async () => {
    const user = userEvent.setup();
    render(<Picker rows={ROWS} />);
    await user.type(screen.getByLabelText("Note"), "hello");
    expect(screen.getByLabelText("Note")).toHaveValue("hello");
  });
});

describe("Picker: efficiency (your job)", () => {
  it("renders each row once at the start", () => {
    render(<Picker rows={ROWS} />);
    expect(renderCounts).toEqual({ a: 1, b: 1, c: 1 });
  });

  it("does not re-render rows while you type an unrelated note", async () => {
    const user = userEvent.setup();
    render(<Picker rows={ROWS} />);
    await user.type(screen.getByLabelText("Note"), "typing a long note");
    expect(renderCounts).toEqual({ a: 1, b: 1, c: 1 });
  });

  it("does not re-render rows when one is selected", async () => {
    const user = userEvent.setup();
    render(<Picker rows={ROWS} />);
    await user.click(screen.getByRole("button", { name: "Apple" }));
    await user.click(screen.getByRole("button", { name: "Cherry" }));
    expect(screen.getByText("Selected: c")).toBeInTheDocument();
    expect(renderCounts).toEqual({ a: 1, b: 1, c: 1 });
  });

  it("re-renders only the row whose label changed", () => {
    const { rerender } = render(<Picker rows={ROWS} />);
    rerender(
      <Picker
        rows={[
          { id: "a", label: "Apple" },
          { id: "b", label: "Banana split" },
          { id: "c", label: "Cherry" },
        ]}
      />,
    );
    expect(renderCounts).toEqual({ a: 1, b: 2, c: 1 });
  });

  it("renders a newly added row once and leaves the others alone", () => {
    const { rerender } = render(<Picker rows={ROWS} />);
    rerender(<Picker rows={[...ROWS, { id: "d", label: "Date" }]} />);
    expect(renderCounts).toEqual({ a: 1, b: 1, c: 1, d: 1 });
  });
});
