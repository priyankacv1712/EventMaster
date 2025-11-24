from backend.file_handler import FileHandler
from backend.venue import Venue
from backend.sport_event import SportEvent
from backend.volunteer import Volunteer
from backend.milestone import Milestone
from backend.budget import Budget
from backend.event_report import EventReport
from backend.budget_report import BudgetReport


class SystemManager:
    def __init__(self):
        # In-memory lists
        self.venues = []
        self.events = []
        self.volunteers = []

        # File handlers
        self.venue_handler = FileHandler("data/venues.json")
        self.event_handler = FileHandler("data/events.json")
        self.volunteer_handler = FileHandler("data/volunteers.json")

        # Counter for Volunteer IDs
        self.volunteer_counter = 0

        # Load existing data if any
        self.load_data()
        self._update_volunteer_counter()

    # ---------- INTERNAL HELPERS ----------

    def _update_volunteer_counter(self):
        """
        Reads existing volunteer IDs and sets counter to max + 1.
        ID format: VOL-2030-0001
        """
        max_num = 0
        for v in self.volunteers:
            vid = v.get_info().get("id", "")
            parts = vid.split("-")
            if len(parts) == 3 and parts[-1].isdigit():
                num = int(parts[-1])
                if num > max_num:
                    max_num = num
        self.volunteer_counter = max_num

    def _generate_volunteer_id(self):
        self.volunteer_counter += 1
        return f"VOL-2030-{self.volunteer_counter:04d}"

    # ---------- VENUE METHODS ----------

    def add_venue(self, name, location, capacity, status="In Progress"):
        venue = Venue(name, location, capacity, status)
        self.venues.append(venue)
        self.save_venues()
        return venue

    def get_all_venues(self):
        return self.venues

    def save_venues(self):
        data = [v.to_dict() for v in self.venues]
        self.venue_handler.save(data)

    def load_venues(self):
        data = self.venue_handler.load()
        self.venues = [Venue.from_dict(d) for d in data]

    # ---------- VOLUNTEER METHODS ----------

    def add_volunteer(self, name, role, contact):
        vol_id = self._generate_volunteer_id()
        volunteer = Volunteer(vol_id, name, role, contact)
        self.volunteers.append(volunteer)
        self.save_volunteers()
        return volunteer

    def get_all_volunteers(self):
        return self.volunteers

    def save_volunteers(self):
        data = [v.to_dict() for v in self.volunteers]
        self.volunteer_handler.save(data)

    def load_volunteers(self):
        data = self.volunteer_handler.load()
        self.volunteers = [Volunteer.from_dict(d) for d in data]

    # ---------- EVENT METHODS ----------

    def add_event(self, name, venue, date):
        event = SportEvent(name, venue, date)
        self.events.append(event)
        self.save_events()
        return event

    def get_all_events(self):
        return self.events

    def save_events(self):
        data = [e.to_dict() for e in self.events]
        self.event_handler.save(data)

    def load_events(self):
        data = self.event_handler.load()
        self.events = [SportEvent.from_dict(d) for d in data]

    # ---------- GENERAL DATA LOAD/SAVE ----------

    def save_data(self):
        self.save_venues()
        self.save_volunteers()
        self.save_events()

    def load_data(self):
        self.load_venues()
        self.load_volunteers()
        self.load_events()

    # ---------- EVENT DETAILS HELPERS ----------

    def assign_volunteer_to_event(self, event, volunteer):
        event.assign_volunteer(volunteer)
        self.save_events()

    def add_milestone_to_event(self, event, title, deadline):
        milestone = Milestone(title, deadline)
        event.add_milestone(milestone)
        self.save_events()
        return milestone

    def set_event_budget(self, event, total_amount):
        budget = Budget(total_amount)
        event.set_budget(budget)
        self.save_events()
        return budget

    # ---------- REPORTS ----------

    def generate_event_report(self):
        report = EventReport(self.events)
        return report.generate_report()

    def generate_budget_report(self):
        report = BudgetReport(self.events)
        return report.generate_report()
