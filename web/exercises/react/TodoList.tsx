/**
 * React 3: lists, keys and a controlled input
 *
 *   <TodoList initial={["Buy milk"]} />
 *
 * Render:
 * - A form with an input labelled "New todo" and a submit button "Add".
 *     Submitting trims the text. Blank text is ignored. A real todo is added at the END and
 *     the input is cleared. (Use onSubmit and event.preventDefault().)
 * - If there are no todos show <p>No todos yet</p>, otherwise a <ul> with one <li> per todo:
 *     a checkbox whose accessible name is the todo text (wrap checkbox and text in one
 *     <label>), the text in a <span> that has className "done" while the todo is done, and a
 *     button with aria-label "Remove <text>" and the visible text "Remove".
 * - Ticking the checkbox toggles done. Remove deletes that todo.
 *
 * Use a stable id as the React `key` (NOT the array index), so state stays with the right
 * item after earlier items are removed. Do not mutate state: build new arrays.
 *
 * Concepts: controlled inputs, onSubmit, keys, immutable updates, conditional rendering.
 */
export type TodoListProps = { initial?: string[] };

export function TodoList(props: TodoListProps) {
  return null;
}
