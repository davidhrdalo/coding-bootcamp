/**
 * Limit concurrency
 *
 * Promise.all(items.map(fn)) starts EVERYTHING at once, which can overwhelm a server or an API
 * rate limit. Write mapWithConcurrency(items, limit, fn): run the async function fn on every
 * item, but never more than `limit` calls at the same time, and return the results IN THE ORIGINAL
 * ORDER. fn receives (item, index). If any call rejects, the returned promise rejects.
 * If limit < 1, reject with a RangeError.
 *
 * Idea: start `limit` worker loops. Each worker repeatedly takes the next unprocessed index until
 * none are left, awaiting fn each time.
 *
 * Concepts: async/await in loops, Promise.all, shared counters in a closure, back-pressure.
 */

export async function mapWithConcurrency<T, R>(
  items: T[],
  limit: number,
  fn: (item: T, index: number) => Promise<R>,
): Promise<R[]> {
  throw new Error("Not implemented");
}
