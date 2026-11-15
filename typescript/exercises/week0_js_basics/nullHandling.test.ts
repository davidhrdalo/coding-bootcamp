import { test } from "node:test";
import assert from "node:assert/strict";
import { countOrDefault, getCity } from "./nullHandling.ts";

test("getCity returns the city when present", () => {
  assert.equal(getCity({ name: "Ada", address: { city: "Brisbane" } }), "Brisbane");
});

test("getCity falls back to Unknown for missing pieces", () => {
  assert.equal(getCity(null), "Unknown");
  assert.equal(getCity(undefined), "Unknown");
  assert.equal(getCity({ name: "Ada" }), "Unknown");
  assert.equal(getCity({ name: "Ada", address: null }), "Unknown");
  assert.equal(getCity({ name: "Ada", address: {} }), "Unknown");
  assert.equal(getCity({ name: "Ada", address: { city: null } }), "Unknown");
});

test("getCity keeps an empty string (this is where || goes wrong)", () => {
  assert.equal(getCity({ name: "Ada", address: { city: "" } }), "");
});

test("countOrDefault keeps zero", () => {
  assert.equal(countOrDefault(0, 5), 0);
  assert.equal(countOrDefault(3, 5), 3);
  assert.equal(countOrDefault(undefined, 5), 5);
});
