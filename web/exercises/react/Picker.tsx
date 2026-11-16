/**
 * React 10: avoiding needless re-renders (memo and useCallback)
 *
 * React re-renders a component whenever its parent re-renders, even if its props did not
 * change. Usually that is fine. For expensive children you can skip the work with
 * React.memo, but it only helps if the props are STABLE (same values, and same function
 * identities).
 *
 * This file already works. Make it efficient WITHOUT changing what it shows:
 *
 *   <Picker rows={[{ id: "a", label: "Apple" }, ...]} />
 *   - a text input labelled "Note" (unrelated state, changes on every keystroke)
 *   - one <Row> per row: <li><button>{label}</button></li>; clicking it sets the selected id
 *   - <p>Selected: {id}</p>  (or "Selected: none")
 *
 * Every time a Row renders it increases renderCounts[id] (written for you).
 * Goal: typing in the Note input, or selecting a row, must NOT re-render any Row. And when
 * the `rows` prop changes, only the rows whose id or label changed should re-render.
 *
 * Hints: wrap Row in React.memo; give Picker's select function a stable identity with
 * useCallback (state setters from useState are already stable).
 *
 * Concepts: render vs commit, referential equality, memo, useCallback. Do not reach for
 * these everywhere: measure first, and use them where they pay off.
 */
import { useState } from "react";

export const renderCounts: Record<string, number> = {};

export function resetRenderCounts(): void {
  for (const key of Object.keys(renderCounts)) delete renderCounts[key];
}

type RowProps = { id: string; label: string; onSelect: (id: string) => void };

export function Row({ id, label, onSelect }: RowProps) {
  renderCounts[id] = (renderCounts[id] ?? 0) + 1;
  return (
    <li>
      <button type="button" onClick={() => onSelect(id)}>
        {label}
      </button>
    </li>
  );
}

export function Picker({ rows }: { rows: { id: string; label: string }[] }) {
  const [note, setNote] = useState("");
  const [selected, setSelected] = useState<string | null>(null);

  return (
    <div>
      <label>
        Note
        <input value={note} onChange={(e) => setNote(e.target.value)} />
      </label>
      <ul>
        {rows.map((row) => (
          <Row key={row.id} id={row.id} label={row.label} onSelect={(id) => setSelected(id)} />
        ))}
      </ul>
      <p>Selected: {selected ?? "none"}</p>
    </div>
  );
}
