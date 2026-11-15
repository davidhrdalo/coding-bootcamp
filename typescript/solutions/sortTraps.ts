export function sortNumbers(nums: number[]): number[] {
  return [...nums].sort((a, b) => a - b);
}

export function sortByLength(words: string[]): string[] {
  return [...words].sort((a, b) => a.length - b.length);
}
