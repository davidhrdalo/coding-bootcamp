export function groupBy<T>(items: T[], keyFn: (item: T) => string): Record<string, T[]> {
  const groups: Record<string, T[]> = {};
  for (const item of items) {
    const key = keyFn(item);
    (groups[key] ??= []).push(item);
  }
  return groups;
}

export function chunk<T>(items: T[], size: number): T[][] {
  if (size < 1) throw new RangeError("size must be at least 1");
  const chunks: T[][] = [];
  for (let i = 0; i < items.length; i += size) {
    chunks.push(items.slice(i, i + size));
  }
  return chunks;
}

export function unique<T>(items: T[]): T[] {
  return [...new Set(items)];
}

export function zip<A, B>(a: A[], b: B[]): [A, B][] {
  const length = Math.min(a.length, b.length);
  const pairs: [A, B][] = [];
  for (let i = 0; i < length; i++) {
    pairs.push([a[i], b[i]]);
  }
  return pairs;
}
