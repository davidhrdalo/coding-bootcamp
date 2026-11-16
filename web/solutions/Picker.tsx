import { memo, useCallback, useState } from "react";

export const renderCounts: Record<string, number> = {};

export function resetRenderCounts(): void {
  for (const key of Object.keys(renderCounts)) delete renderCounts[key];
}

type RowProps = { id: string; label: string; onSelect: (id: string) => void };

export const Row = memo(function Row({ id, label, onSelect }: RowProps) {
  renderCounts[id] = (renderCounts[id] ?? 0) + 1;
  return (
    <li>
      <button type="button" onClick={() => onSelect(id)}>
        {label}
      </button>
    </li>
  );
});

export function Picker({ rows }: { rows: { id: string; label: string }[] }) {
  const [note, setNote] = useState("");
  const [selected, setSelected] = useState<string | null>(null);
  const select = useCallback((id: string) => setSelected(id), []);

  return (
    <div>
      <label>
        Note
        <input value={note} onChange={(e) => setNote(e.target.value)} />
      </label>
      <ul>
        {rows.map((row) => (
          <Row key={row.id} id={row.id} label={row.label} onSelect={select} />
        ))}
      </ul>
      <p>Selected: {selected ?? "none"}</p>
    </div>
  );
}
