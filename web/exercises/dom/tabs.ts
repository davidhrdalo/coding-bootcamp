/**
 * Accessible tabs
 *
 * Wire up a tab widget. The HTML already exists:
 *
 *   <div id="tabs">
 *     <div role="tablist">
 *       <button role="tab" id="t1" aria-controls="p1">One</button>
 *       <button role="tab" id="t2" aria-controls="p2">Two</button>
 *     </div>
 *     <div role="tabpanel" id="p1">...</div>
 *     <div role="tabpanel" id="p2" >...</div>
 *   </div>
 *
 * initTabs(root) must:
 * - Select the FIRST tab at the start.
 * - For the selected tab: aria-selected="true" and tabindex="0". For the others:
 *   aria-selected="false" and tabindex="-1".
 * - Show only the selected tab's panel (the one whose id is in aria-controls): every other
 *   panel gets the `hidden` attribute (panel.hidden = true), the selected one does not.
 * - Clicking a tab selects it.
 * - Keyboard, when a tab has focus: ArrowRight selects AND focuses the next tab (wrap from
 *   last to first); ArrowLeft the previous (wrap from first to last); Home the first;
 *   End the last. Call event.preventDefault() for these keys.
 *
 * Concepts: ARIA roles and states, roving tabindex, keyboard accessibility, DOM events.
 */
export function initTabs(root: HTMLElement): void {
  throw new Error("Not implemented yet");
}
