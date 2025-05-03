from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from character import Character


class Relationship:
    def __init__(
        self, character1: "Character", character2: "Character", description: str
    ):
        self.id: int = 0
        self.character1: "Character" = character1
        self.character2: "Character" = character2
        self.description: str = description
