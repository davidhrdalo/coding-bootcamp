export function delegate(
  root: HTMLElement,
  selector: string,
  type: string,
  handler: (match: Element, event: Event) => void,
): () => void {
  const listener = (event: Event) => {
    const start = event.target;
    if (!(start instanceof Element)) return;
    const match = start.closest(selector);
    if (match && match !== root && root.contains(match)) {
      handler(match, event);
    }
  };
  root.addEventListener(type, listener);
  return () => root.removeEventListener(type, listener);
}
