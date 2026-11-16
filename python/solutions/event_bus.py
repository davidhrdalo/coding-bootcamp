class EventBus:
    def __init__(self) -> None:
        self._subscriptions = {}

    @staticmethod
    def _check_event(event: str) -> None:
        if not isinstance(event, str) or not event:
            raise ValueError("event must be a non-empty string")

    def subscribe(self, event: str, handler):
        self._check_event(event)
        if not callable(handler):
            raise TypeError("handler must be callable")
        entry = [handler, True]  # [handler, still_active]
        self._subscriptions.setdefault(event, []).append(entry)

        def unsubscribe() -> None:
            entry[1] = False
            entries = self._subscriptions.get(event, [])
            entries[:] = [e for e in entries if e is not entry]

        return unsubscribe

    def publish(self, event: str, payload=None) -> list:
        self._check_event(event)
        errors = []
        for entry in list(self._subscriptions.get(event, [])):
            handler, active = entry
            if not active:
                continue
            try:
                handler(payload)
            except Exception as exc:  # noqa: BLE001 - collecting failures is the point
                errors.append(exc)
        return errors
