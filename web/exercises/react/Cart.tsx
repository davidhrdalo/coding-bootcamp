/**
 * React 8: useReducer
 *
 * When state has several related fields and several kinds of updates, a REDUCER keeps all the
 * rules in one pure function: (state, action) -> new state. Build one for a shopping cart.
 *
 * Money is in CENTS. A line is { id, name, price, qty }.
 *
 * cartReducer(state, action) -> new state. It must NOT modify the old state (tests freeze it).
 *   { type: "add", item: { id, name, price } }   add one; if the id is already there, qty + 1
 *   { type: "remove", id }                        remove that line
 *   { type: "setQty", id, qty }                   set the quantity; qty <= 0 removes the line;
 *                                                 an unknown id changes nothing
 *   { type: "clear" }                             empty the cart
 * cartTotal(state) -> sum of price * qty.
 *
 * <Cart products={[{ id, name, price }]} /> uses useReducer(cartReducer, initialCart):
 * - one button "Add <name>" for each product
 * - if the cart is empty show <p>Cart is empty</p>, otherwise a <ul> with one <li> per line
 *   containing "<name> x <qty>" (for example "Tea x 2") and a button "Remove <name>"
 * - <p>Total: $12.34</p> (cents formatted as dollars, two decimals), always shown
 * - a button "Clear cart"
 *
 * Concepts: reducers, immutability, useReducer, actions as data, pure functions are easy to test.
 */
export type Product = { id: string; name: string; price: number };
export type CartLine = Product & { qty: number };
export type CartState = { lines: CartLine[] };
export type CartAction =
  | { type: "add"; item: Product }
  | { type: "remove"; id: string }
  | { type: "setQty"; id: string; qty: number }
  | { type: "clear" };

export const initialCart: CartState = { lines: [] };

export function cartReducer(state: CartState, action: CartAction): CartState {
  throw new Error("Not implemented yet");
}

export function cartTotal(state: CartState): number {
  throw new Error("Not implemented yet");
}

export function Cart(props: { products: Product[] }) {
  return null;
}
