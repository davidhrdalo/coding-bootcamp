import { describe, expect, it, vi } from "vitest";
import { fetchWithRetry } from "./fetchWithRetry";

const res = (status: number) => new Response("body", { status });

function sequence(...steps: Array<number | Error>) {
  let call = 0;
  return vi.fn(async () => {
    const step = steps[Math.min(call++, steps.length - 1)];
    if (step instanceof Error) throw step;
    return res(step);
  });
}

describe("fetchWithRetry", () => {
  it("returns the first successful response without sleeping", async () => {
    const fetchFn = sequence(200);
    const sleep = vi.fn(async (_ms: number) => {});
    const response = await fetchWithRetry("/x", { fetchFn, sleep });
    expect(response.status).toBe(200);
    expect(fetchFn).toHaveBeenCalledTimes(1);
    expect(sleep).not.toHaveBeenCalled();
  });

  it("retries a 503 and returns the later success", async () => {
    const fetchFn = sequence(503, 200);
    const sleep = vi.fn(async (_ms: number) => {});
    const response = await fetchWithRetry("/x", { fetchFn, sleep, delayMs: 100 });
    expect(response.status).toBe(200);
    expect(fetchFn).toHaveBeenCalledTimes(2);
    expect(sleep.mock.calls.map((c) => c[0])).toEqual([100]);
  });

  it("backs off exponentially and gives the last response back when retries run out", async () => {
    const fetchFn = sequence(500, 502, 503);
    const sleep = vi.fn(async (_ms: number) => {});
    const response = await fetchWithRetry("/x", { fetchFn, sleep, retries: 2, delayMs: 100 });
    expect(response.status).toBe(503);
    expect(fetchFn).toHaveBeenCalledTimes(3);
    expect(sleep.mock.calls.map((c) => c[0])).toEqual([100, 200]);
  });

  it("retries 429 but not other client errors", async () => {
    const sleep = vi.fn(async (_ms: number) => {});
    const limited = sequence(429, 200);
    expect((await fetchWithRetry("/x", { fetchFn: limited, sleep })).status).toBe(200);
    const missing = sequence(404, 200);
    expect((await fetchWithRetry("/x", { fetchFn: missing, sleep })).status).toBe(404);
    expect(missing).toHaveBeenCalledTimes(1);
  });

  it("retries after a network error", async () => {
    const fetchFn = sequence(new TypeError("offline"), 200);
    const sleep = vi.fn(async (_ms: number) => {});
    expect((await fetchWithRetry("/x", { fetchFn, sleep })).status).toBe(200);
    expect(fetchFn).toHaveBeenCalledTimes(2);
  });

  it("throws the last error when every attempt throws", async () => {
    const last = new TypeError("still offline");
    const fetchFn = sequence(new TypeError("offline"), new TypeError("offline"), last);
    const sleep = vi.fn(async (_ms: number) => {});
    await expect(fetchWithRetry("/x", { fetchFn, sleep, retries: 2 })).rejects.toBe(last);
    expect(fetchFn).toHaveBeenCalledTimes(3);
  });

  it("with retries 0 makes exactly one attempt", async () => {
    const fetchFn = sequence(503, 200);
    const sleep = vi.fn(async (_ms: number) => {});
    const response = await fetchWithRetry("/x", { fetchFn, sleep, retries: 0 });
    expect(response.status).toBe(503);
    expect(fetchFn).toHaveBeenCalledTimes(1);
    expect(sleep).not.toHaveBeenCalled();
  });

  it("defaults to 2 retries and a 100 ms delay", async () => {
    const fetchFn = sequence(500);
    const sleep = vi.fn(async (_ms: number) => {});
    await fetchWithRetry("/x", { fetchFn, sleep });
    expect(fetchFn).toHaveBeenCalledTimes(3);
    expect(sleep.mock.calls.map((c) => c[0])).toEqual([100, 200]);
  });

  it("passes the url on to fetch", async () => {
    const fetchFn = sequence(200);
    await fetchWithRetry("/some/path", { fetchFn });
    expect(fetchFn).toHaveBeenCalledWith("/some/path");
  });
});
