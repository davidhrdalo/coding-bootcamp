import { beforeEach, describe, expect, it } from "vitest";
import { initTabs } from "./tabs";

let root: HTMLElement;
const tab = (n: number) => document.getElementById(`t${n}`) as HTMLButtonElement;
const panel = (n: number) => document.getElementById(`p${n}`) as HTMLElement;
const key = (el: Element, name: string) =>
  el.dispatchEvent(new KeyboardEvent("keydown", { key: name, bubbles: true, cancelable: true }));

beforeEach(() => {
  root = document.createElement("div");
  root.innerHTML = `
    <div role="tablist">
      <button role="tab" id="t1" aria-controls="p1">One</button>
      <button role="tab" id="t2" aria-controls="p2">Two</button>
      <button role="tab" id="t3" aria-controls="p3">Three</button>
    </div>
    <div role="tabpanel" id="p1">first</div>
    <div role="tabpanel" id="p2">second</div>
    <div role="tabpanel" id="p3">third</div>`;
  document.body.append(root);
  initTabs(root);
});

function expectSelected(n: number) {
  [1, 2, 3].forEach((i) => {
    expect(tab(i).getAttribute("aria-selected")).toBe(i === n ? "true" : "false");
    expect(tab(i).getAttribute("tabindex")).toBe(i === n ? "0" : "-1");
    expect(panel(i).hidden).toBe(i !== n);
  });
}

describe("initTabs", () => {
  it("starts with the first tab selected", () => {
    expectSelected(1);
  });

  it("selects a tab when it is clicked", () => {
    tab(3).click();
    expectSelected(3);
    tab(2).click();
    expectSelected(2);
  });

  it("ArrowRight moves to the next tab and focuses it", () => {
    tab(1).focus();
    key(tab(1), "ArrowRight");
    expectSelected(2);
    expect(document.activeElement).toBe(tab(2));
  });

  it("ArrowRight wraps from the last tab to the first", () => {
    tab(3).click();
    tab(3).focus();
    key(tab(3), "ArrowRight");
    expectSelected(1);
    expect(document.activeElement).toBe(tab(1));
  });

  it("ArrowLeft goes back and wraps from the first to the last", () => {
    tab(1).focus();
    key(tab(1), "ArrowLeft");
    expectSelected(3);
    expect(document.activeElement).toBe(tab(3));
    key(tab(3), "ArrowLeft");
    expectSelected(2);
  });

  it("Home and End jump to the ends", () => {
    tab(2).click();
    tab(2).focus();
    key(tab(2), "End");
    expectSelected(3);
    key(tab(3), "Home");
    expectSelected(1);
  });

  it("prevents the default action for the keys it handles, but not for others", () => {
    tab(1).focus();
    const arrow = new KeyboardEvent("keydown", { key: "ArrowRight", bubbles: true, cancelable: true });
    tab(1).dispatchEvent(arrow);
    expect(arrow.defaultPrevented).toBe(true);
    const other = new KeyboardEvent("keydown", { key: "a", bubbles: true, cancelable: true });
    tab(2).dispatchEvent(other);
    expect(other.defaultPrevented).toBe(false);
    expectSelected(2);
  });
});
