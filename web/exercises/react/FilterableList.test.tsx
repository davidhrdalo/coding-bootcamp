import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it } from "vitest";
import { FilterableList } from "./FilterableList";

const ITEMS = ["Apple", "Banana", "Cherry", "Pineapple"];
const shown = () => screen.queryAllByRole("listitem").map((li) => li.textContent);

describe("FilterableList", () => {
  it("shows everything at first", () => {
    render(<FilterableList items={ITEMS} />);
    expect(shown()).toEqual(ITEMS);
    expect(screen.getByText("Showing 4 of 4")).toBeInTheDocument();
  });

  it("filters as you type, ignoring case", async () => {
    const user = userEvent.setup();
    render(<FilterableList items={ITEMS} />);
    await user.type(screen.getByLabelText("Filter"), "APP");
    expect(shown()).toEqual(["Apple", "Pineapple"]);
    expect(screen.getByText("Showing 2 of 4")).toBeInTheDocument();
  });

  it("matches anywhere inside the item and keeps the original order", async () => {
    const user = userEvent.setup();
    render(<FilterableList items={ITEMS} />);
    await user.type(screen.getByLabelText("Filter"), "an");
    expect(shown()).toEqual(["Banana"]);
  });

  it("ignores spaces around the filter text", async () => {
    const user = userEvent.setup();
    render(<FilterableList items={ITEMS} />);
    await user.type(screen.getByLabelText("Filter"), "  cherry ");
    expect(shown()).toEqual(["Cherry"]);
  });

  it("says when nothing matches", async () => {
    const user = userEvent.setup();
    render(<FilterableList items={ITEMS} />);
    await user.type(screen.getByLabelText("Filter"), "zzz");
    expect(screen.getByText("No matches")).toBeInTheDocument();
    expect(screen.queryByRole("list")).not.toBeInTheDocument();
    expect(screen.getByText("Showing 0 of 4")).toBeInTheDocument();
  });

  it("shows everything again when the filter is cleared", async () => {
    const user = userEvent.setup();
    render(<FilterableList items={ITEMS} />);
    const input = screen.getByLabelText("Filter");
    await user.type(input, "zzz");
    await user.clear(input);
    expect(shown()).toEqual(ITEMS);
  });

  it("reacts when the items prop changes (it is derived, not copied)", () => {
    const { rerender } = render(<FilterableList items={["a"]} />);
    rerender(<FilterableList items={["a", "b"]} />);
    expect(shown()).toEqual(["a", "b"]);
  });
});
