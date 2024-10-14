
names = ["Suji", "Alwin", "Kumar", "Vinu"]

class NameStatusHandler:
    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, name, status):
        if hasattr(self, 'next_handler'):
            return self.next_handler.handle(name, status)
        return None


class NameTrueStatusTrue(NameStatusHandler):
    def handle(self, name, status):
        if name in names and status == 'active':
            print(f"{name} is available")
            return
        return super().handle(name, status)


class NameTrueStatusFalse(NameStatusHandler):
    def handle(self, name, status):
        if name in names and status == 'inactive':
            print(f"{name} is unavailable")
            return
        return super().handle(name, status)


class NameFalseStatusFalse(NameStatusHandler):
    def handle(self, name, status):
        if name not in names and (status == 'inactive' or status == 'active'):
            print("Error in the system")
            return
        return super().handle(name, status)


class NameFalseStatusEmpty(NameStatusHandler):
    def handle(self, name, status):
        if name not in names and (not status or status is None):
            print("Unknown person is requesting access.")
            return
        return super().handle(name, status)
