import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { debounce, throttle } from "./debounce";

beforeEach(() => {
  vi.useFakeTimers();
  vi.setSystemTime(0);
});
afterEach(() => {
  vi.useRealTimers();
});

describe("debounce", () => {
  it("runs once, after the calls stop, with the last arguments", () => {
    const fn = vi.fn();
    const debounced = debounce(fn, 300);
    debounced("a");
    debounced("b");
    debounced("c");
    expect(fn).not.toHaveBeenCalled();
    vi.advanceTimersByTime(299);
    expect(fn).not.toHaveBeenCalled();
    vi.advanceTimersByTime(1);
    expect(fn).toHaveBeenCalledTimes(1);
    expect(fn).toHaveBeenCalledWith("c");
  });

  it("restarts the timer on every call", () => {
    const fn = vi.fn();
    const debounced = debounce(fn, 100);
    debounced(1);
    vi.advanceTimersByTime(90);
    debounced(2);
    vi.advanceTimersByTime(90);
    expect(fn).not.toHaveBeenCalled();
    vi.advanceTimersByTime(10);
    expect(fn).toHaveBeenCalledWith(2);
  });

  it("can run again after a quiet period", () => {
    const fn = vi.fn();
    const debounced = debounce(fn, 50);
    debounced("first");
    vi.advanceTimersByTime(50);
    debounced("second");
    vi.advanceTimersByTime(50);
    expect(fn.mock.calls).toEqual([["first"], ["second"]]);
  });

  it("cancel drops the pending call", () => {
    const fn = vi.fn();
    const debounced = debounce(fn, 100);
    debounced("x");
    debounced.cancel();
    vi.advanceTimersByTime(1000);
    expect(fn).not.toHaveBeenCalled();
  });

  it("cancel with nothing pending is harmless and the function still works afterwards", () => {
    const fn = vi.fn();
    const debounced = debounce(fn, 10);
    debounced.cancel();
    debounced("y");
    vi.advanceTimersByTime(10);
    expect(fn).toHaveBeenCalledWith("y");
  });
});

describe("throttle", () => {
  it("runs the first call immediately", () => {
    const fn = vi.fn();
    const throttled = throttle(fn, 100);
    throttled("a");
    expect(fn).toHaveBeenCalledTimes(1);
    expect(fn).toHaveBeenCalledWith("a");
  });

  it("ignores calls inside the window", () => {
    const fn = vi.fn();
    const throttled = throttle(fn, 100);
    throttled("a");
    vi.advanceTimersByTime(50);
    throttled("b");
    vi.advanceTimersByTime(49);
    throttled("c");
    expect(fn).toHaveBeenCalledTimes(1);
  });

  it("allows a call again once the window has passed", () => {
    const fn = vi.fn();
    const throttled = throttle(fn, 100);
    throttled("a");
    vi.advanceTimersByTime(100);
    throttled("b");
    expect(fn.mock.calls).toEqual([["a"], ["b"]]);
  });

  it("measures the window from the last call that ran, not the last call made", () => {
    const fn = vi.fn();
    const throttled = throttle(fn, 100);
    throttled("a"); // runs at t=0
    vi.advanceTimersByTime(60);
    throttled("ignored"); // t=60
    vi.advanceTimersByTime(40);
    throttled("b"); // t=100: window since "a" is over
    expect(fn.mock.calls).toEqual([["a"], ["b"]]);
  });
});
