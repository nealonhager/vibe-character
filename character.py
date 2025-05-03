from datetime import datetime
from typing import TYPE_CHECKING
from random import choice
from enums import Gender, BloodType, EyeColor, HairColor, MaleTitle, FemaleTitle
from units import Pounds, Height
from event import Event

if TYPE_CHECKING:
    from relationship import Relationship

# Define the trait lists
TRAITS_LIST_1 = [
    "Honest",
    "Deceiver",
    "Loyal",
    "Cowardly",
    "Brave",
    "Vengeful",
    "Merciful",
    "Impulsive",
    "Reasonable",
    "Lazy",
    "Diligent",
    "Naive",
]

TRAITS_LIST_2 = [
    "Cruel",
    "Friendly",
    "Angry",
    "Optimistic",
    "Pessimistic",
    "Arrogant",
    "Humble",
    "Snob",
    "Respectful",
    "Greedy",
    "Generous",
    "Kind",
]


class Character:
    def __init__(
        self,
        id: int,
        name: str,
        family_name: str,
        title: MaleTitle | FemaleTitle | None,
        birth_date: datetime,
        birth_place: str,
        mother: "Character",
        father: "Character",
        gender: Gender,
        height: Height,
        weight: Pounds,
        blood_type: BloodType,
        eye_color: EyeColor,
        hair_color: HairColor,
        strength: int,
        dexterity: int,
        constitution: int,
        intelligence: int,
        wisdom: int,
        charisma: int,
        traits: list[str],
        occupation: str,
        hobbies: list[str],
        relationships: list["Relationship"],
        history: list[Event],
    ):
        self.id: int = id

        # Identity
        self.name = name
        self.family_name = family_name
        self.title = title

        # Lineage
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.mother = mother
        self.father = father

        # Physical
        self.gender = gender
        self.height = height
        self.weight = weight
        self.blood_type = blood_type
        self.eye_color = eye_color
        self.hair_color = hair_color

        # Abilities
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

        # Traits
        if traits:
            self.traits = traits
        else:
            trait1 = choice(TRAITS_LIST_1)
            trait2 = choice(TRAITS_LIST_2)
            self.traits = [trait1, trait2]

        # Other
        self.occupation = occupation
        self.hobbies = hobbies
        self.relationships = relationships

        # Events
        self.history = history
