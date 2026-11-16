class Notifier:
    def __init__(self, channels: list | None = None) -> None:
        self._channels = list(channels or [])

    def add_channel(self, channel) -> None:
        self._channels.append(channel)

    def notify(self, message: str) -> dict:
        if not message or not message.strip():
            raise ValueError("message is required")
        sent = []
        failed = {}
        for channel in self._channels:
            name = getattr(channel, "name", type(channel).__name__)
            try:
                channel.send(message)
            except Exception as exc:  # noqa: BLE001 - isolating failures is the point
                failed[name] = str(exc)
            else:
                sent.append(name)
        return {"sent": sent, "failed": failed}
