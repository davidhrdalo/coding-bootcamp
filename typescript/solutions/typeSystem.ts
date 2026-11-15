export type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "rectangle"; width: number; height: number }
  | { kind: "square"; side: number };

export function assertNever(value: never): never {
  throw new Error("Unexpected value: " + JSON.stringify(value));
}

export function area(shape: Shape): number {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "rectangle":
      return shape.width * shape.height;
    case "square":
      return shape.side * shape.side;
    default:
      return assertNever(shape);
  }
}

function isPositive(n: unknown): n is number {
  return typeof n === "number" && Number.isFinite(n) && n > 0;
}

export function isShape(value: unknown): value is Shape {
  if (typeof value !== "object" || value === null || Array.isArray(value)) return false;
  const v = value as Record<string, unknown>;
  switch (v.kind) {
    case "circle":
      return isPositive(v.radius);
    case "rectangle":
      return isPositive(v.width) && isPositive(v.height);
    case "square":
      return isPositive(v.side);
    default:
      return false;
  }
}

export type Result<T, E> = { ok: true; value: T } | { ok: false; error: E };

export function ok<T>(value: T): Result<T, never> {
  return { ok: true, value };
}

export function err<E>(error: E): Result<never, E> {
  return { ok: false, error };
}

export function mapResult<T, U, E>(result: Result<T, E>, fn: (value: T) => U): Result<U, E> {
  return result.ok ? ok(fn(result.value)) : result;
}

export function parseNumber(text: string): Result<number, string> {
  const trimmed = text.trim();
  if (trimmed === "") return err("empty");
  const n = Number(trimmed);
  return Number.isFinite(n) ? ok(n) : err("not a number");
}
