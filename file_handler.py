import json
import os


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        """Save Python data (list/dict) to JSON file."""
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load(self):
        """Load Python data from JSON file. Returns [] if file doesn't exist."""
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
