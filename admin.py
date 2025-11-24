from backend.user import User


class Admin(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    def add_venue_permission(self):
        return f"Admin {self.get_name()} can add venues."

    def to_dict(self):
        data = super().to_dict()
        data["role"] = "Admin"
        return data

    @staticmethod
    def from_dict(data):
        return Admin(data["name"], data["email"])
