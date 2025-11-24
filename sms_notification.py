from backend.notification import Notification


class SMSNotification(Notification):
    def __init__(self, recipient_phone):
        super().__init__(recipient_phone)

    def send(self, message):
        # Just simulating, not sending real SMS
        return f"SMS sent to {self._recipient}: {message}"
