import { useReducer } from "react";

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
  switch (action.type) {
    case "add": {
      const exists = state.lines.some((line) => line.id === action.item.id);
      if (exists) {
        return {
          lines: state.lines.map((line) => (line.id === action.item.id ? { ...line, qty: line.qty + 1 } : line)),
        };
      }
      return { lines: [...state.lines, { ...action.item, qty: 1 }] };
    }
    case "remove":
      return { lines: state.lines.filter((line) => line.id !== action.id) };
    case "setQty": {
      if (!state.lines.some((line) => line.id === action.id)) return state;
      if (action.qty <= 0) return { lines: state.lines.filter((line) => line.id !== action.id) };
      return { lines: state.lines.map((line) => (line.id === action.id ? { ...line, qty: action.qty } : line)) };
    }
    case "clear":
      return { lines: [] };
  }
}

export function cartTotal(state: CartState): number {
  return state.lines.reduce((sum, line) => sum + line.price * line.qty, 0);
}

export function Cart({ products }: { products: Product[] }) {
  const [state, dispatch] = useReducer(cartReducer, initialCart);
  return (
    <div>
      <div>
        {products.map((product) => (
          <button key={product.id} type="button" onClick={() => dispatch({ type: "add", item: product })}>
            Add {product.name}
          </button>
        ))}
      </div>
      {state.lines.length === 0 ? (
        <p>Cart is empty</p>
      ) : (
        <ul>
          {state.lines.map((line) => (
            <li key={line.id}>
              <span>
                {line.name} x {line.qty}
              </span>
              <button type="button" onClick={() => dispatch({ type: "remove", id: line.id })}>
                Remove {line.name}
              </button>
            </li>
          ))}
        </ul>
      )}
      <p>Total: ${(cartTotal(state) / 100).toFixed(2)}</p>
      <button type="button" onClick={() => dispatch({ type: "clear" })}>
        Clear cart
      </button>
    </div>
  );
}
