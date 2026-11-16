/**
 * React 4: derived state (do not store what you can compute)
 *
 *   <FilterableList items={["Apple", "Banana", "Cherry"]} />
 *
 * Render:
 * - An input labelled "Filter".
 * - <p>Showing X of Y</p> where X is how many items match and Y is the total.
 * - A <ul> with an <li> for each matching item, in the original order. An item matches when it
 *   CONTAINS the filter text, ignoring case and ignoring spaces at the ends of the filter.
 * - If nothing matches show <p>No matches</p> instead of the list.
 *
 * Keep only the filter text in state. The visible list is computed from props and state on
 * every render (storing the filtered list in state is the classic beginner bug).
 *
 * Concepts: controlled input, derived data, useMemo (optional here), rendering lists.
 */
export type FilterableListProps = { items: string[] };

export function FilterableList(props: FilterableListProps) {
  return null;
}
