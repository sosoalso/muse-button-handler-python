from Logger import Logger

# 로거 설정
logger = Logger(__name__).get_logger()


class EventManager:
    def __init__(self, *initial_events_name_list):
        # 초기 이벤트와 그에 대한 핸들러를 저장하는 딕셔너리 초기화
        self.event_handlers = {event: [] for event in initial_events_name_list}

    def add_event(self, name):
        # 새로운 이벤트 추가
        if name not in self.event_handlers:
            self.event_handlers[name] = []
        else:
            # 이벤트가 이미 존재하는 경우 로그 출력
            logger.info(f"Event already exists: {name}")

    def remove_event(self, name):
        # 이벤트 제거
        try:
            del self.event_handlers[name]
        except KeyError:
            # 이벤트가 존재하지 않는 경우 로그 출력
            logger.info(f"No such event: {name}")

    def add_event_handler(self, name, handler):
        # 특정 이벤트에 대한 핸들러 추가
        try:
            self.event_handlers[name].append(handler)
        except KeyError:
            # 이벤트가 존재하지 않는 경우 로그 출력
            logger.info(f"No such event: {handler}")

    def remove_event_handler(self, name, handler):
        # 특정 이벤트의 핸들러 제거
        try:
            self.event_handlers[name].remove(handler)
        except ValueError:
            # 핸들러가 목록에 없는 경우 로그 출력
            logger.info(f"Handler not found for name: {handler}")
        except KeyError:
            # 이벤트가 존재하지 않는 경우 로그 출력
            logger.info(f"No such event: {handler}")

    def trigger_event(self, name, *args, **kwargs):
        # 이벤트 발생 시 연결된 모든 핸들러 호출
        if name in self.event_handlers:
            for handler in self.event_handlers[name]:
                handler(*args, **kwargs)
        else:
            # 이벤트가 존재하지 않는 경우 로그 출력
            logger.info(f"No such event: {name}")


# ---------------------------------------------------------------------------- #
