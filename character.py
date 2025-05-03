from datetime import datetime
from typing import TYPE_CHECKING
from random import choice, choices
from enums import (
    Gender,
    BloodType,
    EyeColor,
    NaturalHairColor,
    DyedHairColor,
    MaleTitle,
    FemaleTitle,
    Build,
    Race,
)
from units import Pounds, Height
from event import Event
from uuid import uuid4
from faker import Faker
from icecream import ic

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
        id: uuid4,
        name: str,
        family_name: str,
        title: MaleTitle | FemaleTitle | None,
        birth_date: datetime,
        birth_place: str,
        mother: "Character",
        father: "Character",
        siblings: list["Character"],
        children: list["Character"],
        gender: Gender,
        height: Height,
        weight: Pounds,
        blood_type: BloodType,
        eye_color: EyeColor,
        hair_color: DyedHairColor | NaturalHairColor | str,
        race: Race,
        build: Build,
        strength: int,
        endurance: int,
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
        primary_address: str,
    ):
        self.id = id

        # Identity
        self.name = name
        self.family_name = family_name
        self.title = title

        # Lineage
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.mother = mother
        self.father = father
        self.siblings = siblings
        self.children = children

        # Physical
        self.gender = gender
        self.height = height
        self.weight = weight
        self.blood_type = blood_type
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.build = build
        self.race = race

        # Abilities
        self.strength = strength
        self.endurance = endurance
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
        self.primary_address = primary_address

        # Events
        self.history = history

    @property
    def age(self) -> int:
        return datetime.now().year - self.birth_date.year

    def print_info(self):
        ic(self.id)
        ic(self.name)
        ic(self.family_name)
        ic(self.title)
        ic(self.birth_date)
        ic(self.age)
        ic(self.birth_place)
        ic(self.mother)
        ic(self.father)
        ic(self.siblings)
        ic(self.children)
        ic(self.gender)
        ic(self.height)
        ic(self.weight)
        ic(self.blood_type)
        ic(self.eye_color)
        ic(self.hair_color)
        ic(self.race)
        ic(self.build)
        ic(self.strength)
        ic(self.endurance)
        ic(self.dexterity)
        ic(self.constitution)
        ic(self.intelligence)
        ic(self.wisdom)
        ic(self.charisma)
        ic(self.traits)
        ic(self.occupation)
        ic(self.hobbies)
        ic(self.relationships)
        ic(self.primary_address)
        ic(self.history)
        ic(self.get_physical_description())

    def get_physical_description(self):
        return f"A {self.height[0]}'{self.height[1]}\" tall, {self.weight} lbs, {self.build.value} build, {self.hair_color.value} hair, {self.eye_color.value} eyes, {self.gender.value}, of {self.race.value} descent, who is a {self.occupation}."


class CharacterFactory:
    def create_random_adult_character(self) -> Character:
        fake = Faker()
        gender = choices(
            [Gender.MALE, Gender.FEMALE, Gender.INTERSEX, Gender.OTHER],
            weights=[0.45, 0.5, 0.03, 0.02],
            k=1,
        )[0]

        # Title
        if gender == Gender.MALE:
            title = choice(list(MaleTitle))
        elif gender == Gender.FEMALE:
            title = choice(list(FemaleTitle))
        else:
            title = None

        # Hair
        hair_color = None
        is_bald = False

        if (
            gender is not Gender.FEMALE
            and choices([True, False], weights=[0.15, 0.85], k=1)[0]
        ):
            is_bald = True
            hair_color = "Bald"

        if not is_bald:
            hair_type = choices(["natural", "dyed"], weights=[0.85, 0.15], k=1)[0]
            hair_color = choice(
                list(DyedHairColor if hair_type == "dyed" else NaturalHairColor)
            )

        # Build
        weight = fake.random_int(min=100, max=300)
        strength = fake.random_int(min=1, max=10)
        if weight < 150:
            build = Build.SLIM
            strength = fake.random_int(min=1, max=5)
        elif weight > 200:
            build = choice([Build.ATHLETIC, Build.FAT])
            strength = fake.random_int(min=3, max=10)
        else:
            build = choice(list(Build))

        character = Character(
            id=uuid4(),
            name=fake.first_name(),
            family_name=fake.last_name(),
            title=title,
            birth_date=fake.date_of_birth(minimum_age=18, maximum_age=60),
            birth_place=fake.city(),
            mother=None,
            father=None,
            siblings=[],
            children=[],
            gender=gender,
            height=(
                choices(range(4, 8), weights=[0.02, 0.66, 0.3, 0.02], k=1)[0],
                choices(range(0, 12), k=1)[0],
            ),
            weight=weight,
            blood_type=choice(list(BloodType)),
            eye_color=choice(list(EyeColor)),
            hair_color=hair_color,
            race=choice(list(Race)),
            build=build,
            strength=strength,
            endurance=fake.random_int(min=1, max=10),
            dexterity=fake.random_int(min=1, max=10),
            constitution=fake.random_int(min=1, max=10),
            intelligence=fake.random_int(min=1, max=10),
            wisdom=fake.random_int(min=1, max=10),
            charisma=fake.random_int(min=1, max=10),
            traits=[choice(TRAITS_LIST_1), choice(TRAITS_LIST_2)],
            occupation=fake.job(),
            hobbies=[],
            relationships=[],
            history=[],
            primary_address=fake.address(),
        )
        return character
