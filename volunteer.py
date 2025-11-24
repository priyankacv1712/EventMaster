class Volunteer:
    def __init__(self, vol_id, name, role, contact):
        self._id = vol_id
        self._name = name
        self._role = role
        self._contact = contact

    def get_info(self):
        return self.to_dict()

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "role": self._role,
            "contact": self._contact
        }

    @staticmethod
    def from_dict(data):
        return Volunteer(
            data.get("id", "VOL-UNKNOWN"),
            data["name"],
            data["role"],
            data["contact"]
        )
