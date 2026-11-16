import { useState } from "react";

export type FilterableListProps = { items: string[] };

export function FilterableList({ items }: FilterableListProps) {
  const [filter, setFilter] = useState("");
  const needle = filter.trim().toLowerCase();
  const visible = items.filter((item) => item.toLowerCase().includes(needle));

  return (
    <div>
      <label>
        Filter
        <input value={filter} onChange={(e) => setFilter(e.target.value)} />
      </label>
      <p>
        Showing {visible.length} of {items.length}
      </p>
      {visible.length === 0 ? (
        <p>No matches</p>
      ) : (
        <ul>
          {visible.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      )}
    </div>
  );
}
