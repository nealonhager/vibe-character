from datetime import datetime


class Event:
    def __init__(self, name: str, description: str, date: datetime):
        self.name = name
        self.description = description
        self.date = date
