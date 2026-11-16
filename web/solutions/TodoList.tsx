import { type FormEvent, useRef, useState } from "react";

export type TodoListProps = { initial?: string[] };

type Todo = { id: number; text: string; done: boolean };

export function TodoList({ initial = [] }: TodoListProps) {
  const nextId = useRef(initial.length + 1);
  const [todos, setTodos] = useState<Todo[]>(() => initial.map((text, i) => ({ id: i + 1, text, done: false })));
  const [draft, setDraft] = useState("");

  function add(event: FormEvent) {
    event.preventDefault();
    const text = draft.trim();
    if (!text) return;
    const id = nextId.current++;
    setTodos((current) => [...current, { id, text, done: false }]);
    setDraft("");
  }

  const toggle = (id: number) =>
    setTodos((current) => current.map((t) => (t.id === id ? { ...t, done: !t.done } : t)));
  const remove = (id: number) => setTodos((current) => current.filter((t) => t.id !== id));

  return (
    <div>
      <form onSubmit={add}>
        <label>
          New todo
          <input value={draft} onChange={(e) => setDraft(e.target.value)} />
        </label>
        <button type="submit">Add</button>
      </form>
      {todos.length === 0 ? (
        <p>No todos yet</p>
      ) : (
        <ul>
          {todos.map((todo) => (
            <li key={todo.id}>
              <label>
                <input type="checkbox" checked={todo.done} onChange={() => toggle(todo.id)} />
                <span className={todo.done ? "done" : undefined}>{todo.text}</span>
              </label>
              <button type="button" aria-label={`Remove ${todo.text}`} onClick={() => remove(todo.id)}>
                Remove
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
