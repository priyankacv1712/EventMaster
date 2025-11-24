from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, recipient):
        self._recipient = recipient

    @abstractmethod
    def send(self, message):
        pass
