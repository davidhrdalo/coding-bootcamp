/**
 * Event delegation
 *
 * Instead of adding a click listener to every row (and again each time you add a row),
 * add ONE listener to a parent and work out which child was clicked.
 *
 *   const stop = delegate(list, "li.row", "click", (row, event) => { ... });
 *   stop();   // removes the listener
 *
 * Rules:
 * - Add exactly one listener of the given type to root.
 * - When the event happens, find the nearest element (starting at event.target and going up,
 *   use Element.closest) that matches selector. If there is one AND it is a descendant of
 *   root (not root itself, and not something above root), call handler(match, event).
 * - Rows added to the page AFTER delegate() was called must work too.
 * - Return a function that removes the listener.
 * - Ignore events whose target is not an Element.
 *
 * Concepts: event bubbling, event.target vs the element you matched, closest(), memory leaks.
 */
export function delegate(
  root: HTMLElement,
  selector: string,
  type: string,
  handler: (match: Element, event: Event) => void,
): () => void {
  throw new Error("Not implemented yet");
}
