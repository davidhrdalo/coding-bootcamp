export interface User {
  name: string;
  address?: { city?: string | null } | null;
}

export function getCity(user: User | null | undefined): string {
  return user?.address?.city ?? "Unknown";
}

export function countOrDefault(count: number | undefined, fallback: number): number {
  return count ?? fallback;
}
