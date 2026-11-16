/**
 * A safe fetch wrapper
 *
 * fetch() only rejects on network failure: a 404 or 500 is a normal Response. Wrap it so
 * callers get a typed result and a clear error.
 *
 *   const user = await fetchJson<User>("/api/users/1");
 *
 * Rules:
 * - Call fetchFn(url, { headers }) where headers = { Accept: "application/json", ...options.headers }
 *   (so the caller can override Accept). fetchFn defaults to the global fetch.
 * - If response.ok is false, throw an HttpError: status = the response status and
 *   message = `HTTP ${status}`.
 * - A 204 No Content response returns undefined and must not try to read a body.
 * - Otherwise parse the body with response.json(). If that fails, throw an Error with the
 *   message "Invalid JSON response".
 *
 * HttpError is written for you.
 *
 * Concepts: fetch semantics, error handling, generics, dependency injection (fetchFn) so
 * tests need no real network.
 */
export class HttpError extends Error {
  readonly status: number;

  constructor(status: number) {
    super(`HTTP ${status}`);
    this.name = "HttpError";
    this.status = status;
  }
}

export type FetchJsonOptions = {
  fetchFn?: typeof fetch;
  headers?: Record<string, string>;
};

export async function fetchJson<T>(url: string, options: FetchJsonOptions = {}): Promise<T> {
  throw new Error("Not implemented yet");
}
