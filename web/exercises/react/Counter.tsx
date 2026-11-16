/**
 * React 2: state, events and the functional update
 *
 *   <Counter initial={5} min={0} max={10} onChange={(n) => ...} />
 *
 * Render:
 *   <p data-testid="count">5</p>
 *   buttons labelled "Increment", "Decrement" and "Reset"
 *
 * Rules:
 * - The count starts at `initial`, forced into the range min..max (defaults: no limits).
 * - Increment adds 1 and Decrement subtracts 1, but the count stays inside min..max. A
 *   button is `disabled` when pressing it could not change the count.
 * - Reset goes back to the (clamped) initial value.
 * - onChange(newCount) is called AFTER the count actually changes (not on the first render,
 *   and not when a click leaves the count the same). Hint: useEffect.
 * - Update state with the FUNCTIONAL form, setCount(c => ...), so two updates in the same
 *   event add up correctly. A test clicks twice inside one act() to check this.
 *
 * Concepts: useState, event handlers, derived values, functional updates, useEffect, useRef.
 */
export type CounterProps = {
  initial?: number;
  min?: number;
  max?: number;
  onChange?: (count: number) => void;
};

export function Counter(props: CounterProps) {
  return null;
}
