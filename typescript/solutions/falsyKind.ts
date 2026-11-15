export function falsyKind(value: unknown): string {
  if (value === null) return "null";
  if (value === undefined) return "undefined";
  if (value === false) return "false";
  if (typeof value === "number" && Number.isNaN(value)) return "nan";
  if (value === 0 || value === 0n) return "zero";
  if (value === "") return "empty-string";
  return "truthy";
}
