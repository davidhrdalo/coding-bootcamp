"""Composition over inheritance: a notifier

Instead of a class per combination (EmailAndSmsNotifier...), build one Notifier that HAS a
list of channels. A channel is any object with a send(message) method. It may raise.

  notifier = Notifier([email, sms])
  notifier.add_channel(push)
  result = notifier.notify("Server is down")
  result -> {"sent": ["email", "push"], "failed": {"sms": "no signal"}}

Rules:
- notify() tries EVERY channel, in order, even after one fails.
- A channel's name is its `name` attribute if it has one, otherwise the class name.
- "sent" lists the names of channels that worked, in order.
- "failed" maps the name of each channel that raised to str(exception).
- Notifier(channels) must not share or change the list you pass in: copy it.
- Empty or blank messages raise ValueError before any channel is called.

Concepts: composition, duck typing (no base class needed), isolating failures, defensive copy.
"""


class Notifier:
    def __init__(self, channels: list | None = None) -> None:
        raise NotImplementedError

    def add_channel(self, channel) -> None:
        raise NotImplementedError

    def notify(self, message: str) -> dict:
        raise NotImplementedError
