class Venue:
    def __init__(self, name, location, capacity, status="In Progress"):
        self._name = name
        self._location = location
        self._capacity = capacity
        self._status = status

    def update_status(self, new_status):
        self._status = new_status

    def get_info(self):
        return self.to_dict()

    def to_dict(self):
        return {
            "name": self._name,
            "location": self._location,
            "capacity": self._capacity,
            "status": self._status
        }

    @staticmethod
    def from_dict(data):
        return Venue(
            data["name"],
            data["location"],
            data["capacity"],
            data.get("status", "In Progress")
        )
