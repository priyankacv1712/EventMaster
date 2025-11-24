from backend.user import User


class Staff(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    def update_task(self):
        return f"Staff {self.get_name()} updates tasks."

    def to_dict(self):
        data = super().to_dict()
        data["role"] = "Staff"
        return data

    @staticmethod
    def from_dict(data):
        return Staff(data["name"], data["email"])
