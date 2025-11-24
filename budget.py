class Budget:
    def __init__(self, total_amount):
        self._total_amount = total_amount
        self._spent_amount = 0

    def add_expense(self, amount):
        self._spent_amount += amount

    def get_remaining(self):
        return self._total_amount - self._spent_amount

    def get_info(self):
        return self.to_dict()

    def to_dict(self):
        return {
            "total": self._total_amount,
            "spent": self._spent_amount,
            "remaining": self.get_remaining()
        }

    @staticmethod
    def from_dict(data):
        b = Budget(data["total"])
        b._spent_amount = data.get("spent", 0)
        return b
