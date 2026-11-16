export function initTabs(root: HTMLElement): void {
  const tabs = Array.from(root.querySelectorAll<HTMLElement>('[role="tab"]'));
  const panels = Array.from(root.querySelectorAll<HTMLElement>('[role="tabpanel"]'));

  function select(index: number, focus = false) {
    tabs.forEach((tab, i) => {
      const selected = i === index;
      tab.setAttribute("aria-selected", String(selected));
      tab.setAttribute("tabindex", selected ? "0" : "-1");
    });
    const controlled = tabs[index].getAttribute("aria-controls");
    panels.forEach((panel) => {
      panel.hidden = panel.id !== controlled;
    });
    if (focus) tabs[index].focus();
  }

  tabs.forEach((tab, index) => {
    tab.addEventListener("click", () => select(index));
    tab.addEventListener("keydown", (event) => {
      const last = tabs.length - 1;
      let target: number | null = null;
      if (event.key === "ArrowRight") target = index === last ? 0 : index + 1;
      else if (event.key === "ArrowLeft") target = index === 0 ? last : index - 1;
      else if (event.key === "Home") target = 0;
      else if (event.key === "End") target = last;
      if (target !== null) {
        event.preventDefault();
        select(target, true);
      }
    });
  });

  select(0);
}
