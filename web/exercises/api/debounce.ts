/**
 * Debounce and throttle
 *
 * Both limit how often a function runs when events fire in bursts (typing, scrolling,
 * resizing).
 *
 * debounce(fn, ms): wait until the calls have STOPPED for ms, then run fn once with the
 * arguments of the LAST call.
 *   - Every new call restarts the timer.
 *   - The returned function also has .cancel(), which drops any pending call.
 *
 * throttle(fn, ms): run fn at most once every ms, on the LEADING edge.
 *   - The first call runs immediately. Calls during the next ms milliseconds are ignored
 *     (not queued). The first call after that runs immediately again.
 *   - Use Date.now() to measure time.
 *
 * Concepts: closures, timers, leading vs trailing edge, search-as-you-type, scroll handlers.
 */
export type Debounced<A extends unknown[]> = ((...args: A) => void) & { cancel: () => void };

export function debounce<A extends unknown[]>(fn: (...args: A) => void, ms: number): Debounced<A> {
  throw new Error("Not implemented yet");
}

export function throttle<A extends unknown[]>(fn: (...args: A) => void, ms: number): (...args: A) => void {
  throw new Error("Not implemented yet");
}
