/**
 * Event emitter
 *
 * Node's events module and the browser's addEventListener are built on the observer pattern.
 * Build a tiny EventEmitter:
 *
 *   on(event, listener)    call listener every time the event is emitted
 *   off(event, listener)   stop calling that listener
 *   once(event, listener)  call listener only for the next emit, then remove it automatically
 *   emit(event, ...args)   call each listener with args, in the order they were added.
 *                          Return true if there was at least one listener, otherwise false.
 *
 * Details: listeners for different events are independent. If a listener removes itself while the
 * event is being emitted, the other listeners must still run (iterate over a COPY of the list).
 * off(event, fn) must also work for a function that was added with once().
 *
 * Concepts: observer / publish-subscribe, closures, Map of arrays, rest parameters (...args).
 */

export type Listener = (...args: any[]) => void;

export class EventEmitter {
  on(event: string, listener: Listener): void {
    throw new Error("Not implemented");
  }

  off(event: string, listener: Listener): void {
    throw new Error("Not implemented");
  }

  once(event: string, listener: Listener): void {
    throw new Error("Not implemented");
  }

  emit(event: string, ...args: any[]): boolean {
    throw new Error("Not implemented");
  }
}
