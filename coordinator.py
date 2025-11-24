from backend.user import User


class Coordinator(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    def manage_event(self):
        return f"Coordinator {self.get_name()} manages events."

    def to_dict(self):
        data = super().to_dict()
        data["role"] = "Coordinator"
        return data

    @staticmethod
    def from_dict(data):
        return Coordinator(data["name"], data["email"])
