import { act, renderHook } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { useDebouncedValue, usePrevious, useToggle } from "./hooks";

describe("useToggle", () => {
  it("starts false by default and toggles", () => {
    const { result } = renderHook(() => useToggle());
    expect(result.current[0]).toBe(false);
    act(() => result.current[1]());
    expect(result.current[0]).toBe(true);
    act(() => result.current[1]());
    expect(result.current[0]).toBe(false);
  });

  it("accepts an initial value and can set it directly", () => {
    const { result } = renderHook(() => useToggle(true));
    expect(result.current[0]).toBe(true);
    act(() => result.current[2](false));
    expect(result.current[0]).toBe(false);
  });

  it("keeps the same toggle function between renders", () => {
    const { result, rerender } = renderHook(() => useToggle());
    const first = result.current[1];
    rerender();
    act(() => first());
    rerender();
    expect(result.current[1]).toBe(first);
  });
});

describe("useDebouncedValue", () => {
  beforeEach(() => vi.useFakeTimers());
  afterEach(() => vi.useRealTimers());

  it("returns the first value immediately", () => {
    const { result } = renderHook(() => useDebouncedValue("a", 300));
    expect(result.current).toBe("a");
  });

  it("updates only after the value has been stable for ms", () => {
    const { result, rerender } = renderHook(({ v }) => useDebouncedValue(v, 300), {
      initialProps: { v: "a" },
    });
    rerender({ v: "b" });
    act(() => void vi.advanceTimersByTime(299));
    expect(result.current).toBe("a");
    act(() => void vi.advanceTimersByTime(1));
    expect(result.current).toBe("b");
  });

  it("restarts the wait when the value changes again", () => {
    const { result, rerender } = renderHook(({ v }) => useDebouncedValue(v, 100), {
      initialProps: { v: 1 },
    });
    rerender({ v: 2 });
    act(() => void vi.advanceTimersByTime(90));
    rerender({ v: 3 });
    act(() => void vi.advanceTimersByTime(90));
    expect(result.current).toBe(1);
    act(() => void vi.advanceTimersByTime(10));
    expect(result.current).toBe(3);
  });

  it("clears its timer when unmounted", () => {
    const { rerender, unmount } = renderHook(({ v }) => useDebouncedValue(v, 100), {
      initialProps: { v: 1 },
    });
    rerender({ v: 2 });
    unmount();
    expect(vi.getTimerCount()).toBe(0);
  });
});

describe("usePrevious", () => {
  it("returns undefined first, then the value from the previous render", () => {
    const { result, rerender } = renderHook(({ v }) => usePrevious(v), { initialProps: { v: 1 } });
    expect(result.current).toBeUndefined();
    rerender({ v: 2 });
    expect(result.current).toBe(1);
    rerender({ v: 3 });
    expect(result.current).toBe(2);
    rerender({ v: 3 });
    expect(result.current).toBe(3);
  });
});
