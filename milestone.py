class Milestone:
    def __init__(self, title, deadline, status="Pending"):
        self._title = title
        self._deadline = deadline
        self._status = status

    def mark_completed(self):
        self._status = "Completed"

    def get_info(self):
        return self.to_dict()

    def to_dict(self):
        return {
            "title": self._title,
            "deadline": self._deadline,
            "status": self._status
        }

    @staticmethod
    def from_dict(data):
        return Milestone(
            data["title"],
            data["deadline"],
            data.get("status", "Pending")
        )
