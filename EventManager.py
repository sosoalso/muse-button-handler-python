from Logger import Logger

logger = Logger(__name__).get_logger()


class EventManager:
    """
    A class that manages events and event handlers.

    Attributes:
        event_handlers (dict): A dictionary that maps event names to a list of event handlers.

    Methods:
        __init__(*initial_events_name_list): Initializes the EventManager with a list of initial event names.
        add_event(name): Adds a new event to the EventManager.
        remove_event(name): Removes an event from the EventManager.
        add_event_handler(name, handler): Adds an event handler to an existing event.
        remove_event_handler(name, handler): Removes an event handler from an existing event.
        trigger_event(name, *args, **kwargs): Triggers an event by calling all its event handlers with the given arguments.
    """

    def __init__(self, *initial_events_name_list):
        self.event_handlers = {event: [] for event in initial_events_name_list}

    def add_event(self, name):
        if name not in self.event_handlers:
            self.event_handlers[name] = []
        else:
            logger.info(f"Event already exists: {name}")

    def remove_event(self, name):
        try:
            del self.event_handlers[name]
        except KeyError:
            logger.info(f"No such event: {name}")

    def add_event_handler(self, name, handler):
        try:
            self.event_handlers[name].append(handler)
        except KeyError:
            logger.info(f"No such event: {handler}")

    def remove_event_handler(self, name, handler):
        try:
            self.event_handlers[name].remove(handler)
        except ValueError:
            logger.info(f"Handler not found for name: {handler}")
        except KeyError:
            logger.info(f"No such event: {handler}")

    def trigger_event(self, name, *args, **kwargs):
        if name in self.event_handlers:
            for handler in self.event_handlers[name]:
                handler(*args, **kwargs)
        else:
            logger.info(f"No such event: {name}")


# ---------------------------------------------------------------------------- #
