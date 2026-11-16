import { describe, expect, it, vi } from "vitest";
import { delegate } from "./eventDelegation";

function makeRoot() {
  const root = document.createElement("div");
  root.innerHTML = `
    <ul>
      <li class="row" id="one"><span class="label">One</span></li>
      <li class="row" id="two"><span class="label">Two</span></li>
    </ul>
    <p class="other">other</p>`;
  document.body.append(root);
  return root;
}

describe("delegate", () => {
  it("calls the handler with the matching element when a child is clicked", () => {
    const root = makeRoot();
    const handler = vi.fn();
    delegate(root, "li.row", "click", handler);
    root.querySelector<HTMLElement>("#one .label")!.click();
    expect(handler).toHaveBeenCalledTimes(1);
    expect((handler.mock.calls[0][0] as Element).id).toBe("one");
    expect(handler.mock.calls[0][1]).toBeInstanceOf(Event);
  });

  it("ignores clicks that do not match the selector", () => {
    const root = makeRoot();
    const handler = vi.fn();
    delegate(root, "li.row", "click", handler);
    root.querySelector<HTMLElement>(".other")!.click();
    expect(handler).not.toHaveBeenCalled();
  });

  it("works for elements added later", () => {
    const root = makeRoot();
    const handler = vi.fn();
    delegate(root, "li.row", "click", handler);
    const late = document.createElement("li");
    late.className = "row";
    late.id = "late";
    root.querySelector("ul")!.append(late);
    late.click();
    expect((handler.mock.calls[0][0] as Element).id).toBe("late");
  });

  it("adds a single listener to the root, whatever the number of rows", () => {
    const root = makeRoot();
    const spy = vi.spyOn(root, "addEventListener");
    delegate(root, "li.row", "click", () => {});
    expect(spy).toHaveBeenCalledTimes(1);
    expect(spy.mock.calls[0][0]).toBe("click");
  });

  it("returns a function that removes the listener", () => {
    const root = makeRoot();
    const handler = vi.fn();
    const stop = delegate(root, "li.row", "click", handler);
    stop();
    root.querySelector<HTMLElement>("#two")!.click();
    expect(handler).not.toHaveBeenCalled();
  });

  it("does not match elements above the root", () => {
    const outer = document.createElement("div");
    outer.className = "row";
    const root = document.createElement("div");
    root.innerHTML = `<p class="inner">x</p>`;
    outer.append(root);
    document.body.append(outer);
    const handler = vi.fn();
    delegate(root, ".row", "click", handler);
    root.querySelector<HTMLElement>(".inner")!.click();
    expect(handler).not.toHaveBeenCalled();
  });

  it("does not match the root itself", () => {
    const root = document.createElement("div");
    root.className = "row";
    document.body.append(root);
    const handler = vi.fn();
    delegate(root, ".row", "click", handler);
    root.click();
    expect(handler).not.toHaveBeenCalled();
  });

  it("works for other event types", () => {
    const root = makeRoot();
    const handler = vi.fn();
    delegate(root, "li.row", "mouseover", handler);
    root.querySelector("#one .label")!.dispatchEvent(new MouseEvent("mouseover", { bubbles: true }));
    expect(handler).toHaveBeenCalledTimes(1);
  });
});
