export function buildList(doc: Document, items: string[]): HTMLUListElement {
  const ul = doc.createElement("ul");
  if (items.length === 0) {
    const li = doc.createElement("li");
    li.className = "empty";
    li.textContent = "Nothing here yet";
    ul.append(li);
    return ul;
  }
  items.forEach((text, index) => {
    const li = doc.createElement("li");
    li.className = "item";
    li.dataset.index = String(index);
    li.textContent = text;
    ul.append(li);
  });
  return ul;
}
