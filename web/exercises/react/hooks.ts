/**
 * React 5: custom hooks
 *
 * A custom hook is a function whose name starts with "use" that calls other hooks. It lets
 * you reuse stateful logic. Write three.
 *
 * useToggle(initial = false) -> [value, toggle, setValue]
 *   - toggle() flips the value. setValue(v) sets it.
 *   - `toggle` must keep the SAME function identity between renders (useCallback).
 *
 * useDebouncedValue(value, ms) -> the value, but it only changes after `value` has stopped
 *   changing for ms milliseconds. It returns the first value immediately. Clean up the timer
 *   when the value changes or the component unmounts (useEffect return).
 *
 * usePrevious(value) -> the value from the PREVIOUS render (undefined on the first render).
 *   Hint: a ref that you update in an effect, so the render still sees the old value.
 *
 * Concepts: rules of hooks, useState, useCallback, useEffect cleanup, useRef.
 */
export function useToggle(initial = false): [boolean, () => void, (value: boolean) => void] {
  throw new Error("Not implemented yet");
}

export function useDebouncedValue<T>(value: T, ms: number): T {
  throw new Error("Not implemented yet");
}

export function usePrevious<T>(value: T): T | undefined {
  throw new Error("Not implemented yet");
}
