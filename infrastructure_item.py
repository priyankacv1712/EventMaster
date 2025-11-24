class InfrastructureItem:
    def __init__(self, item_name, status="Pending", cost=0):
        self._item_name = item_name
        self._status = status
        self._cost = cost

    def update_status(self, new_status):
        self._status = new_status

    def get_info(self):
        return self.to_dict()

    def to_dict(self):
        return {
            "item_name": self._item_name,
            "status": self._status,
            "cost": self._cost
        }

    @staticmethod
    def from_dict(data):
        return InfrastructureItem(
            data["item_name"],
            data.get("status", "Pending"),
            data.get("cost", 0)
        )
