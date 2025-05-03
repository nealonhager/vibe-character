from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from character import Character

global event_counter
event_counter = 0


class Event:
    def __init__(self, name: str, characters_involved: list["Character"]):
        self.name = name
        self.characters_involved = characters_involved
        global event_counter
        self.event_count = event_counter
        event_counter += 1

        for character in self.characters_involved:
            character.history.append(self)

    def __str__(self):
        return f"{self.event_count} - {self.name}."
