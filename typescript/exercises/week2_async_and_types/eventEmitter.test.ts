import { test } from "node:test";
import assert from "node:assert/strict";
import { EventEmitter } from "./eventEmitter.ts";

test("on and emit pass arguments to listeners", () => {
  const emitter = new EventEmitter();
  const received: unknown[][] = [];
  emitter.on("msg", (...args) => received.push(args));
  emitter.emit("msg", "hello", 42);
  assert.deepEqual(received, [["hello", 42]]);
});

test("listeners run in the order they were added", () => {
  const emitter = new EventEmitter();
  const order: string[] = [];
  emitter.on("e", () => order.push("first"));
  emitter.on("e", () => order.push("second"));
  emitter.emit("e");
  assert.deepEqual(order, ["first", "second"]);
});

test("emit returns whether anyone was listening", () => {
  const emitter = new EventEmitter();
  assert.equal(emitter.emit("nobody"), false);
  emitter.on("somebody", () => {});
  assert.equal(emitter.emit("somebody"), true);
});

test("events are independent", () => {
  const emitter = new EventEmitter();
  let calls = 0;
  emitter.on("a", () => calls++);
  emitter.emit("b");
  assert.equal(calls, 0);
});

test("off removes a listener", () => {
  const emitter = new EventEmitter();
  let calls = 0;
  const listener = () => calls++;
  emitter.on("e", listener);
  emitter.emit("e");
  emitter.off("e", listener);
  emitter.emit("e");
  assert.equal(calls, 1);
});

test("once fires a single time", () => {
  const emitter = new EventEmitter();
  let calls = 0;
  emitter.once("e", () => calls++);
  emitter.emit("e");
  emitter.emit("e");
  assert.equal(calls, 1);
});

test("off also removes a once listener before it fires", () => {
  const emitter = new EventEmitter();
  let calls = 0;
  const listener = () => calls++;
  emitter.once("e", listener);
  emitter.off("e", listener);
  emitter.emit("e");
  assert.equal(calls, 0);
});

test("a listener that removes itself does not stop the others", () => {
  const emitter = new EventEmitter();
  const order: string[] = [];
  const first = () => {
    order.push("first");
    emitter.off("e", first);
  };
  emitter.on("e", first);
  emitter.on("e", () => order.push("second"));
  emitter.emit("e");
  emitter.emit("e");
  assert.deepEqual(order, ["first", "second", "second"]);
});
