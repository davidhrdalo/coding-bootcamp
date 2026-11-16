import { useEffect, useRef, useState } from "react";

export type CounterProps = {
  initial?: number;
  min?: number;
  max?: number;
  onChange?: (count: number) => void;
};

export function Counter({ initial = 0, min = -Infinity, max = Infinity, onChange }: CounterProps) {
  const clamp = (n: number) => Math.min(max, Math.max(min, n));
  const [count, setCount] = useState(() => clamp(initial));
  const firstRender = useRef(true);

  useEffect(() => {
    if (firstRender.current) {
      firstRender.current = false;
      return;
    }
    onChange?.(count);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [count]);

  return (
    <div>
      <p data-testid="count">{count}</p>
      <button type="button" disabled={count >= max} onClick={() => setCount((c) => clamp(c + 1))}>
        Increment
      </button>
      <button type="button" disabled={count <= min} onClick={() => setCount((c) => clamp(c - 1))}>
        Decrement
      </button>
      <button type="button" onClick={() => setCount(clamp(initial))}>
        Reset
      </button>
    </div>
  );
}
