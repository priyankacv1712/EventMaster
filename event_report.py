from backend.report_generator import ReportGenerator


class EventReport(ReportGenerator):
    def __init__(self, events):
        self._events = events

    def generate_report(self):
        lines = []
        lines.append("=== EVENT REPORT ===")
        for event in self._events:
            info = event.get_info()
            lines.append(f"Event: {info['name']} on {info['date']}")
            lines.append(f"  Venue: {info['venue']['name']} ({info['venue']['location']})")
            lines.append(f"  Volunteers: {len(info['volunteers'])}")
            lines.append(f"  Milestones: {len(info['milestones'])}")
            lines.append("")

        return "\n".join(lines)
