/**
 * TypeScript: unions, type guards and Result
 *
 * TypeScript's types disappear at runtime, so data from outside (JSON, APIs) must be CHECKED
 * with real code. This exercise practises the core type-system tools.
 *
 * 1. Shape is a DISCRIMINATED UNION (each variant has a `kind` tag).
 *    area(shape): circle = PI * radius^2, rectangle = width * height, square = side * side.
 *    Use a switch on shape.kind. The default branch should call assertNever(shape), which
 *    makes the compiler complain if a new variant is added and forgotten.
 *
 * 2. isShape(value: unknown): value is Shape is a TYPE GUARD. It returns true only for objects
 *    with a valid kind and positive, finite numeric dimensions (radius; width and height; side).
 *
 * 3. Result<T, E> is either {ok: true, value} or {ok: false, error}. It handles failure without
 *    throwing exceptions.
 *      ok(value), err(error)               constructors
 *      mapResult(result, fn)               apply fn to the value if ok; leave an error unchanged
 *      parseNumber(text): Result<number, string>
 *         "42" or " 3.5 " -> ok(number); "" (or only spaces) -> err("empty");
 *         anything that is not a finite number -> err("not a number")
 *
 * Concepts: union types, narrowing, type predicates (value is T), never, generics, unknown vs any.
 * Run `npm run typecheck` (after `npm install`) to see the compiler check your types.
 */

export type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "rectangle"; width: number; height: number }
  | { kind: "square"; side: number };

export function assertNever(value: never): never {
  throw new Error("Unexpected value: " + JSON.stringify(value));
}

export function area(shape: Shape): number {
  throw new Error("Not implemented");
}

export function isShape(value: unknown): value is Shape {
  throw new Error("Not implemented");
}

export type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };

export function ok<T>(value: T): Result<T, never> {
  throw new Error("Not implemented");
}

export function err<E>(error: E): Result<never, E> {
  throw new Error("Not implemented");
}

export function mapResult<T, U, E>(result: Result<T, E>, fn: (value: T) => U): Result<U, E> {
  throw new Error("Not implemented");
}

export function parseNumber(text: string): Result<number, string> {
  throw new Error("Not implemented");
}
