/**
 * Retry with exponential backoff
 *
 * Networks and servers fail for a moment. Retry the request a few times, waiting longer
 * each time.
 *
 *   const response = await fetchWithRetry("/api/items", { retries: 2, delayMs: 100 });
 *
 * Options (all optional): retries (default 2), delayMs (default 100), fetchFn (default the
 * global fetch), sleep(ms) -> Promise (default: a setTimeout promise).
 *
 * Rules:
 * - Make up to retries + 1 attempts in total.
 * - RETRY when fetchFn throws (a network error) or the response status is 429 or 500 or
 *   higher. Do NOT retry other statuses (a 404 will not fix itself): return that response.
 * - Before attempt number n+1 (counting attempts from 0), wait delayMs * 2 ** n by calling
 *   sleep. So with delayMs 100 the waits are 100, 200, 400...
 * - If every attempt fails: when the last attempt returned a response, RETURN it (do not
 *   throw); when the last attempt threw, throw that error.
 * - Do not wait after the final attempt.
 *
 * Concepts: transient failures, exponential backoff, which errors are safe to retry
 * (see the Python status_codes exercise), injecting sleep so tests run instantly.
 */
export type RetryOptions = {
  retries?: number;
  delayMs?: number;
  fetchFn?: typeof fetch;
  sleep?: (ms: number) => Promise<void>;
};

export async function fetchWithRetry(url: string, options: RetryOptions = {}): Promise<Response> {
  throw new Error("Not implemented yet");
}
