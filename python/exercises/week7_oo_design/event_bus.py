"""The observer pattern: an event bus

Parts of a program react to events without knowing about each other.

  bus = EventBus()
  off = bus.subscribe("user.created", handler)   # returns a function that unsubscribes
  errors = bus.publish("user.created", {"id": 1})   # calls handler({"id": 1})
  off()                                          # handler is no longer called

Rules:
- publish(event, payload=None) calls every handler of that event with the payload, in
  subscription order.
- A handler that raises must NOT stop the others. publish() returns the list of exceptions
  that were raised, in order ([] when all went well).
- Publishing an event nobody listens to does nothing and returns [].
- The same function may be subscribed twice; it is then called twice. Each unsubscribe
  function removes only its own subscription (and is safe to call twice).
- A handler may unsubscribe itself (or others) while publish() is running. The handlers
  that were subscribed when publish() STARTED are all still called... except one that was
  unsubscribed before its turn comes: do not call that one.
- A handler subscribed during publish() is not called until the next publish().
- Event names must be non-empty strings (ValueError otherwise); handlers must be callable
  (TypeError otherwise).

Concepts: observer / publish-subscribe, decoupling, mutating a list while iterating.
"""


class EventBus:
    def __init__(self) -> None:
        raise NotImplementedError

    def subscribe(self, event: str, handler):
        raise NotImplementedError

    def publish(self, event: str, payload=None) -> list:
        raise NotImplementedError
