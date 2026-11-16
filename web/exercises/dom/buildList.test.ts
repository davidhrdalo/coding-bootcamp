import { describe, expect, it } from "vitest";
import { buildList } from "./buildList";

describe("buildList", () => {
  it("makes a ul with one li per item, in order", () => {
    const ul = buildList(document, ["Tea", "Cake"]);
    expect(ul.tagName).toBe("UL");
    expect([...ul.children].map((li) => li.tagName)).toEqual(["LI", "LI"]);
    expect([...ul.children].map((li) => li.textContent)).toEqual(["Tea", "Cake"]);
  });

  it("gives each li the class item and a data-index", () => {
    const ul = buildList(document, ["a", "b", "c"]);
    const items = [...ul.children] as HTMLElement[];
    expect(items.map((li) => li.className)).toEqual(["item", "item", "item"]);
    expect(items.map((li) => li.dataset.index)).toEqual(["0", "1", "2"]);
  });

  it("treats item text as text, not HTML", () => {
    const ul = buildList(document, ["<img src=x onerror=alert(1)>", "<b>bold</b>"]);
    expect(ul.querySelector("img")).toBeNull();
    expect(ul.querySelector("b")).toBeNull();
    expect(ul.children[0].textContent).toBe("<img src=x onerror=alert(1)>");
    expect(ul.children[1].textContent).toBe("<b>bold</b>");
  });

  it("shows a placeholder for an empty list", () => {
    const ul = buildList(document, []);
    expect(ul.children).toHaveLength(1);
    expect(ul.children[0].className).toBe("empty");
    expect(ul.children[0].textContent).toBe("Nothing here yet");
  });

  it("creates the elements with the document it is given", () => {
    const other = document.implementation.createHTMLDocument("other");
    const ul = buildList(other, ["x"]);
    expect(ul.ownerDocument).toBe(other);
    expect(ul.firstElementChild?.ownerDocument).toBe(other);
  });

  it("does not attach the list to the page", () => {
    const ul = buildList(document, ["x"]);
    expect(ul.parentElement).toBeNull();
  });
});
