class User:
    def __init__(self, name, email):
        self._name = name      # Encapsulated
        self._email = email    # Encapsulated

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def login(self):
        return f"{self._name} logged in."

    def to_dict(self):
        return {
            "name": self._name,
            "email": self._email
        }

    @staticmethod
    def from_dict(data):
        return User(data["name"], data["email"])
