import pytest

from notifier_composition import Notifier


class Recorder:
    name = "recorder"

    def __init__(self):
        self.messages = []

    def send(self, message):
        self.messages.append(message)


class Broken:
    name = "broken"

    def send(self, message):
        raise RuntimeError("no signal")


class Unnamed:
    def send(self, message):
        pass


def test_sends_to_every_channel_in_order():
    first, second = Recorder(), Recorder()
    second.name = "second"
    result = Notifier([first, second]).notify("hi")
    assert first.messages == ["hi"]
    assert second.messages == ["hi"]
    assert result == {"sent": ["recorder", "second"], "failed": {}}


def test_a_failing_channel_does_not_stop_the_others():
    after = Recorder()
    result = Notifier([Broken(), after]).notify("hi")
    assert after.messages == ["hi"]
    assert result == {"sent": ["recorder"], "failed": {"broken": "no signal"}}


def test_name_falls_back_to_the_class_name():
    assert Notifier([Unnamed()]).notify("x")["sent"] == ["Unnamed"]


def test_add_channel():
    notifier = Notifier()
    rec = Recorder()
    notifier.add_channel(rec)
    notifier.notify("x")
    assert rec.messages == ["x"]


def test_does_not_keep_a_reference_to_the_callers_list():
    channels = [Recorder()]
    notifier = Notifier(channels)
    channels.append(Broken())
    assert notifier.notify("x") == {"sent": ["recorder"], "failed": {}}


@pytest.mark.parametrize("message", ["", "   "])
def test_blank_message_is_rejected_before_sending(message):
    rec = Recorder()
    with pytest.raises(ValueError):
        Notifier([rec]).notify(message)
    assert rec.messages == []


def test_no_channels():
    assert Notifier().notify("x") == {"sent": [], "failed": {}}
