import { describe, expect, it, vi } from "vitest";
import { HttpError, fetchJson } from "./fetchJson";

const reply = (body: BodyInit | null, status = 200) => vi.fn(async () => new Response(body, { status }));

describe("fetchJson", () => {
  it("returns the parsed JSON body", async () => {
    const fetchFn = reply(JSON.stringify({ id: 1, name: "Ada" }));
    await expect(fetchJson<{ id: number }>("/api/users/1", { fetchFn })).resolves.toEqual({ id: 1, name: "Ada" });
  });

  it("asks for JSON by default", async () => {
    const fetchFn = reply("{}");
    await fetchJson("/x", { fetchFn });
    expect(fetchFn).toHaveBeenCalledTimes(1);
    expect(fetchFn).toHaveBeenCalledWith("/x", { headers: { Accept: "application/json" } });
  });

  it("lets the caller add or override headers", async () => {
    const fetchFn = reply("{}");
    await fetchJson("/x", { fetchFn, headers: { Authorization: "Bearer t", Accept: "text/json" } });
    expect(fetchFn).toHaveBeenCalledWith("/x", {
      headers: { Accept: "text/json", Authorization: "Bearer t" },
    });
  });

  it("throws an HttpError with the status for non-ok responses", async () => {
    const fetchFn = reply(JSON.stringify({ error: "nope" }), 404);
    const error = await fetchJson("/x", { fetchFn }).catch((e: unknown) => e);
    expect(error).toBeInstanceOf(HttpError);
    expect(error).toBeInstanceOf(Error);
    expect((error as HttpError).status).toBe(404);
    expect((error as HttpError).message).toBe("HTTP 404");
    expect((error as HttpError).name).toBe("HttpError");
  });

  it("treats server errors the same way", async () => {
    await expect(fetchJson("/x", { fetchFn: reply("oops", 500) })).rejects.toMatchObject({ status: 500 });
  });

  it("returns undefined for 204 No Content", async () => {
    await expect(fetchJson("/x", { fetchFn: reply(null, 204) })).resolves.toBeUndefined();
  });

  it("throws a clear error when the body is not JSON", async () => {
    await expect(fetchJson("/x", { fetchFn: reply("<html>") })).rejects.toThrow("Invalid JSON response");
  });

  it("lets network errors through unchanged", async () => {
    const boom = new TypeError("Failed to fetch");
    const fetchFn = vi.fn(async () => {
      throw boom;
    });
    await expect(fetchJson("/x", { fetchFn })).rejects.toBe(boom);
  });
});
