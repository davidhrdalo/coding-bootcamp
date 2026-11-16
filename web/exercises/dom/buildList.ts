/**
 * Build a list with the DOM API
 *
 * Create elements with doc.createElement and fill them with textContent. Never build HTML
 * by gluing strings together: that is how cross-site scripting (XSS) bugs happen.
 *
 *   buildList(document, ["Tea", "Cake"])
 *   -> <ul><li class="item" data-index="0">Tea</li><li class="item" data-index="1">Cake</li></ul>
 *
 * Rules:
 * - Return a <ul> with one <li> per item, in order. Each <li> has the class "item" and a
 *   data-index attribute holding its position as text ("0", "1", ...).
 * - Set the text with textContent. An item such as "<b>hi</b>" must appear as literal text
 *   and must NOT create a <b> element.
 * - For an empty array return a <ul> holding ONE <li> with the class "empty" and the text
 *   "Nothing here yet".
 * - Create every element with the doc you are given (not the global document).
 *
 * Concepts: createElement, textContent vs innerHTML, dataset, why escaping matters.
 */
export function buildList(doc: Document, items: string[]): HTMLUListElement {
  throw new Error("Not implemented yet");
}
