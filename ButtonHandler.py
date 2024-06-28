# ---------------------------------------------------------------------------- #
import threading
import time

from EventManager import EventManager


# ---------------------------------------------------------------------------- #
class ButtonHandler(EventManager):
    """
    Represents a button that can handle push, release, hold, and repeat events.

    Args:
        hold_time (float): The duration in seconds for which the button needs to be held to trigger a hold event. Default is 2.0 seconds.
        repeat_interval (float): The interval in seconds between repeat events when the button is held. Default is 0.5 seconds.
        trigger_release_on_hold (bool): Specifies whether to trigger a release event when the button is held. Default is False.

    Attributes:
        hold_time (float): The duration in seconds for which the button needs to be held to trigger a hold event.
        repeat_interval (float): The interval in seconds between repeat events when the button is held.
        repeat_thread (Thread): The thread used for generating repeat events.
        hold_thread (Thread): The thread used for generating hold events.
        is_pushed (bool): Indicates whether the button is currently pushed.
        is_hold (bool): Indicates whether the button is currently in a hold state.
        trigger_release_on_hold (bool): Specifies whether to trigger a release event when the button is held.

    Events:
        push: Triggered when the button is pushed.
        release: Triggered when the button is released.
        hold: Triggered when the button is held for the specified hold time.
        repeat: Triggered at regular intervals when the button is held.

    """

    def __init__(self, hold_time=2.0, repeat_interval=0.5, trigger_release_on_hold=False):
        super().__init__("push", "release", "hold", "repeat")
        self.hold_time = hold_time
        self.repeat_interval = repeat_interval
        self.repeat_thread = None
        self.hold_thread = None
        self.is_pushed = False
        self.is_hold = False
        self.trigger_release_on_hold = trigger_release_on_hold

    def start_repeat(self):
        while self.is_pushed:
            self.trigger_event("repeat")
            time.sleep(self.repeat_interval)

    def start_hold(self):
        while self.is_pushed:
            time.sleep(self.hold_time)
            if self.is_pushed and not self.is_hold:
                self.is_hold = True
                self.trigger_event("hold")

    def handle_event(self, evt):
        if evt.value:  # pushed
            self.is_pushed = True
            self.trigger_event("push")
            if self.repeat_thread is None or not self.repeat_thread.is_alive():
                self.repeat_thread = threading.Thread(target=self.start_repeat)
                self.repeat_thread.start()
            if self.hold_thread is None or not self.hold_thread.is_alive():
                self.hold_thread = threading.Thread(target=self.start_hold)
                self.hold_thread.start()
        else:  # released
            self.is_pushed = False
            if self.trigger_release_on_hold and self.is_hold:
                self.trigger_event("release")
            elif not self.is_hold:
                self.trigger_event("release")
            self.is_hold = False


# ---------------------------------------------------------------------------- #
