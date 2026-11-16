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
  const fetchFn = options.fetchFn ?? fetch;
  const response = await fetchFn(url, {
    headers: { Accept: "application/json", ...options.headers },
  });
  if (!response.ok) throw new HttpError(response.status);
  if (response.status === 204) return undefined as T;
  try {
    return (await response.json()) as T;
  } catch {
    throw new Error("Invalid JSON response");
  }
}
