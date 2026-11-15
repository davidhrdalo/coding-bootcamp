export type Listener = (...args: any[]) => void;

type Stored = Listener & { original?: Listener };

export class EventEmitter {
  private listeners = new Map<string, Stored[]>();

  on(event: string, listener: Listener): void {
    const list = this.listeners.get(event) ?? [];
    list.push(listener);
    this.listeners.set(event, list);
  }

  off(event: string, listener: Listener): void {
    const list = this.listeners.get(event);
    if (!list) return;
    const index = list.findIndex((l) => l === listener || l.original === listener);
    if (index !== -1) list.splice(index, 1);
  }

  once(event: string, listener: Listener): void {
    const wrapper: Stored = (...args: any[]) => {
      this.off(event, wrapper);
      listener(...args);
    };
    wrapper.original = listener;
    this.on(event, wrapper);
  }

  emit(event: string, ...args: any[]): boolean {
    const list = this.listeners.get(event);
    if (!list || list.length === 0) return false;
    for (const listener of [...list]) {
      listener(...args);
    }
    return true;
  }
}
