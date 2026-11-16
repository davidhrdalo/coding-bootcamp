export type RetryOptions = {
  retries?: number;
  delayMs?: number;
  fetchFn?: typeof fetch;
  sleep?: (ms: number) => Promise<void>;
};

const defaultSleep = (ms: number) => new Promise<void>((resolve) => setTimeout(resolve, ms));

export async function fetchWithRetry(url: string, options: RetryOptions = {}): Promise<Response> {
  const { retries = 2, delayMs = 100, fetchFn = fetch, sleep = defaultSleep } = options;
  let lastError: unknown;
  let lastResponse: Response | undefined;

  for (let attempt = 0; attempt <= retries; attempt++) {
    lastError = undefined;
    lastResponse = undefined;
    try {
      const response = await fetchFn(url);
      if (response.status !== 429 && response.status < 500) return response;
      lastResponse = response;
    } catch (error) {
      lastError = error;
    }
    if (attempt < retries) await sleep(delayMs * 2 ** attempt);
  }

  if (lastResponse) return lastResponse;
  throw lastError;
}
