from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from relationship import Relationship


class Character:
    def __init__(
        self,
        id: int,
        name: str,
        family_name: str,
        birth_date: datetime,
        birth_place: str,
        mother: "Character",
        father: "Character",
        gender: str,
        height: int,
        weight: int,
        blood_type: str,
        eye_color: str,
        hair_color: str,
        strength: int,
        dexterity: int,
        constitution: int,
        intelligence: int,
        wisdom: int,
        charisma: int,
        occupation: str,
        hobbies: list[str],
        relationships: list["Relationship"],
    ):
        self.id: int = id

        # Identity
        self.name: str = name
        self.family_name: str = family_name

        # Lineage
        self.birth_date: datetime = birth_date
        self.birth_place: str = birth_place
        self.mother: "Character" = mother
        self.father: "Character" = father

        # Physical
        self.gender: str = gender
        self.height: int = height
        self.weight: int = weight
        self.blood_type: str = blood_type
        self.eye_color: str = eye_color
        self.hair_color: str = hair_color

        # Abilities
        self.strength: int = strength
        self.dexterity: int = dexterity
        self.constitution: int = constitution
        self.intelligence: int = intelligence
        self.wisdom: int = wisdom
        self.charisma: int = charisma

        # Other
        self.occupation: str = occupation
        self.hobbies: list[str] = hobbies
        self.relationships: list["Relationship"] = relationships
