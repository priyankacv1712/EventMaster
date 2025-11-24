from backend.milestone import Milestone
from backend.budget import Budget
from backend.volunteer import Volunteer
from backend.venue import Venue


class SportEvent:
    def __init__(self, name, venue, date):
        self._name = name
        self._venue = venue
        self._date = date
        self._volunteers = []
        self._milestones = []
        self._budget = None

    def assign_volunteer(self, volunteer):
        self._volunteers.append(volunteer)

    def add_milestone(self, milestone):
        self._milestones.append(milestone)

    def set_budget(self, budget):
        self._budget = budget

    def get_info(self):
        return self.to_dict()

    def to_dict(self):
        return {
            "name": self._name,
            "date": self._date,
            "venue": self._venue.to_dict() if self._venue else None,
            "volunteers": [v.to_dict() for v in self._volunteers],
            "milestones": [m.to_dict() for m in self._milestones],
            "budget": self._budget.to_dict() if self._budget else None
        }

    @staticmethod
    def from_dict(data):
        venue = Venue.from_dict(data["venue"]) if data.get("venue") else None

        event = SportEvent(
            data["name"],
            venue,
            data["date"]
        )

        for v_data in data.get("volunteers", []):
            event.assign_volunteer(Volunteer.from_dict(v_data))

        for m_data in data.get("milestones", []):
            event.add_milestone(Milestone.from_dict(m_data))

        if data.get("budget"):
            event.set_budget(Budget.from_dict(data["budget"]))

        return event
