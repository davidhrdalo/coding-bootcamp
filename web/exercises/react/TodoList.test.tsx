import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it } from "vitest";
import { TodoList } from "./TodoList";

async function add(user: ReturnType<typeof userEvent.setup>, text: string) {
  await user.type(screen.getByLabelText("New todo"), text);
  await user.click(screen.getByRole("button", { name: "Add" }));
}

describe("TodoList", () => {
  it("shows an empty message", () => {
    render(<TodoList />);
    expect(screen.getByText("No todos yet")).toBeInTheDocument();
    expect(screen.queryByRole("list")).not.toBeInTheDocument();
  });

  it("shows the initial todos", () => {
    render(<TodoList initial={["Buy milk", "Walk dog"]} />);
    expect(screen.getAllByRole("listitem")).toHaveLength(2);
    expect(screen.getByRole("checkbox", { name: "Buy milk" })).not.toBeChecked();
    expect(screen.queryByText("No todos yet")).not.toBeInTheDocument();
  });

  it("adds a todo at the end and clears the input", async () => {
    const user = userEvent.setup();
    render(<TodoList initial={["a"]} />);
    await add(user, "b");
    const items = screen.getAllByRole("listitem");
    expect(items).toHaveLength(2);
    expect(items[1]).toHaveTextContent("b");
    expect(screen.getByLabelText("New todo")).toHaveValue("");
  });

  it("adds with the Enter key and trims the text", async () => {
    const user = userEvent.setup();
    render(<TodoList />);
    await user.type(screen.getByLabelText("New todo"), "  spaced  {enter}");
    expect(screen.getByRole("checkbox", { name: "spaced" })).toBeInTheDocument();
  });

  it("ignores blank todos", async () => {
    const user = userEvent.setup();
    render(<TodoList />);
    await add(user, "   ");
    expect(screen.getByText("No todos yet")).toBeInTheDocument();
  });

  it("toggles done and marks the text", async () => {
    const user = userEvent.setup();
    render(<TodoList initial={["Buy milk"]} />);
    await user.click(screen.getByRole("checkbox", { name: "Buy milk" }));
    expect(screen.getByRole("checkbox", { name: "Buy milk" })).toBeChecked();
    expect(screen.getByText("Buy milk")).toHaveClass("done");
    await user.click(screen.getByRole("checkbox", { name: "Buy milk" }));
    expect(screen.getByText("Buy milk")).not.toHaveClass("done");
  });

  it("removes a todo", async () => {
    const user = userEvent.setup();
    render(<TodoList initial={["a", "b", "c"]} />);
    await user.click(screen.getByRole("button", { name: "Remove b" }));
    expect(screen.getAllByRole("listitem").map((li) => li.textContent)).toEqual([
      expect.stringContaining("a"),
      expect.stringContaining("c"),
    ]);
    expect(screen.queryByRole("checkbox", { name: "b" })).not.toBeInTheDocument();
  });

  it("keeps the done state with the right item after another one is removed (stable keys)", async () => {
    const user = userEvent.setup();
    render(<TodoList initial={["a", "b", "c"]} />);
    await user.click(screen.getByRole("checkbox", { name: "c" }));
    await user.click(screen.getByRole("button", { name: "Remove a" }));
    expect(screen.getByRole("checkbox", { name: "c" })).toBeChecked();
    expect(screen.getByRole("checkbox", { name: "b" })).not.toBeChecked();
  });

  it("gives new todos unique identities even after removals", async () => {
    const user = userEvent.setup();
    render(<TodoList initial={["a", "b"]} />);
    await user.click(screen.getByRole("button", { name: "Remove b" }));
    await add(user, "c");
    await user.click(screen.getByRole("checkbox", { name: "c" }));
    expect(screen.getByRole("checkbox", { name: "a" })).not.toBeChecked();
    expect(screen.getByRole("checkbox", { name: "c" })).toBeChecked();
  });
});
