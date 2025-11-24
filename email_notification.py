from backend.notification import Notification


class EmailNotification(Notification):
    def __init__(self, recipient_email):
        super().__init__(recipient_email)

    def send(self, message):
        # Just simulating, not sending real email
        return f"Email sent to {self._recipient}: {message}"
