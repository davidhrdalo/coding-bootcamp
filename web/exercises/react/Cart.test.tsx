import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it } from "vitest";
import { type CartState, Cart, cartReducer, cartTotal, initialCart } from "./Cart";

const tea = { id: "tea", name: "Tea", price: 350 };
const cake = { id: "cake", name: "Cake", price: 475 };

function freeze(state: CartState): CartState {
  state.lines.forEach((line) => Object.freeze(line));
  Object.freeze(state.lines);
  return Object.freeze(state);
}

describe("cartReducer", () => {
  it("adds a new line with quantity 1", () => {
    const next = cartReducer(freeze({ lines: [] }), { type: "add", item: tea });
    expect(next).toEqual({ lines: [{ ...tea, qty: 1 }] });
  });

  it("adding the same product again increases the quantity", () => {
    let state = cartReducer(initialCart, { type: "add", item: tea });
    state = cartReducer(freeze(state), { type: "add", item: tea });
    expect(state.lines).toEqual([{ ...tea, qty: 2 }]);
  });

  it("keeps lines in the order they were first added", () => {
    let state = cartReducer(initialCart, { type: "add", item: tea });
    state = cartReducer(state, { type: "add", item: cake });
    state = cartReducer(state, { type: "add", item: tea });
    expect(state.lines.map((l) => [l.id, l.qty])).toEqual([
      ["tea", 2],
      ["cake", 1],
    ]);
  });

  it("removes a line", () => {
    let state = cartReducer(initialCart, { type: "add", item: tea });
    state = cartReducer(state, { type: "add", item: cake });
    state = cartReducer(freeze(state), { type: "remove", id: "tea" });
    expect(state.lines.map((l) => l.id)).toEqual(["cake"]);
  });

  it("sets a quantity, and removes the line at zero or below", () => {
    let state = cartReducer(initialCart, { type: "add", item: tea });
    state = cartReducer(freeze(state), { type: "setQty", id: "tea", qty: 5 });
    expect(state.lines[0].qty).toBe(5);
    state = cartReducer(freeze(state), { type: "setQty", id: "tea", qty: 0 });
    expect(state.lines).toEqual([]);
    state = cartReducer(initialCart, { type: "add", item: tea });
    expect(cartReducer(freeze(state), { type: "setQty", id: "tea", qty: -2 }).lines).toEqual([]);
  });

  it("ignores setQty for an unknown id", () => {
    const state = cartReducer(initialCart, { type: "add", item: tea });
    expect(cartReducer(freeze(state), { type: "setQty", id: "nope", qty: 3 })).toEqual(state);
  });

  it("clears the cart", () => {
    const state = cartReducer(initialCart, { type: "add", item: tea });
    expect(cartReducer(freeze(state), { type: "clear" })).toEqual({ lines: [] });
  });

  it("never modifies the state it was given", () => {
    const state = freeze(cartReducer(initialCart, { type: "add", item: tea }));
    expect(() => cartReducer(state, { type: "add", item: tea })).not.toThrow();
    expect(() => cartReducer(state, { type: "setQty", id: "tea", qty: 9 })).not.toThrow();
    expect(state.lines[0].qty).toBe(1);
  });
});

describe("cartTotal", () => {
  it("sums price times quantity", () => {
    expect(cartTotal({ lines: [] })).toBe(0);
    expect(
      cartTotal({
        lines: [
          { ...tea, qty: 2 },
          { ...cake, qty: 1 },
        ],
      }),
    ).toBe(1175);
  });
});

describe("<Cart>", () => {
  it("starts empty", () => {
    render(<Cart products={[tea, cake]} />);
    expect(screen.getByText("Cart is empty")).toBeInTheDocument();
    expect(screen.getByText("Total: $0.00")).toBeInTheDocument();
  });

  it("adds products, counts them and shows the total", async () => {
    const user = userEvent.setup();
    render(<Cart products={[tea, cake]} />);
    await user.click(screen.getByRole("button", { name: "Add Tea" }));
    await user.click(screen.getByRole("button", { name: "Add Tea" }));
    await user.click(screen.getByRole("button", { name: "Add Cake" }));
    expect(screen.getByText("Tea x 2")).toBeInTheDocument();
    expect(screen.getByText("Cake x 1")).toBeInTheDocument();
    expect(screen.getByText("Total: $11.75")).toBeInTheDocument();
    expect(screen.queryByText("Cart is empty")).not.toBeInTheDocument();
  });

  it("removes a line and clears the cart", async () => {
    const user = userEvent.setup();
    render(<Cart products={[tea, cake]} />);
    await user.click(screen.getByRole("button", { name: "Add Tea" }));
    await user.click(screen.getByRole("button", { name: "Add Cake" }));
    await user.click(screen.getByRole("button", { name: "Remove Tea" }));
    expect(screen.queryByText("Tea x 1")).not.toBeInTheDocument();
    expect(screen.getByText("Total: $4.75")).toBeInTheDocument();
    await user.click(screen.getByRole("button", { name: "Clear cart" }));
    expect(screen.getByText("Cart is empty")).toBeInTheDocument();
  });
});
