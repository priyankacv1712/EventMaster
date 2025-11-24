from backend.report_generator import ReportGenerator


class BudgetReport(ReportGenerator):
    def __init__(self, events):
        self._events = events

    def generate_report(self):
        lines = []
        lines.append("=== BUDGET REPORT ===")
        total_budget = 0
        total_spent = 0

        for event in self._events:
            info = event.get_info()
            budget = info["budget"]
            if budget:
                lines.append(f"Event: {info['name']}")
                lines.append(f"  Total: {budget['total']}")
                lines.append(f"  Spent: {budget['spent']}")
                lines.append(f"  Remaining: {budget['remaining']}")
                lines.append("")
                total_budget += budget["total"]
                total_spent += budget["spent"]

        lines.append("=== OVERALL ===")
        lines.append(f"Total Budget: {total_budget}")
        lines.append(f"Total Spent: {total_spent}")
        lines.append(f"Overall Remaining: {total_budget - total_spent}")

        return "\n".join(lines)
