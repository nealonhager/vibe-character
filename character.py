from datetime import datetime
from typing import TYPE_CHECKING
from random import choice, choices, normalvariate
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
        height: int,  # Height in inches
        weight: int,
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
        feet = self.height // 12
        inches = self.height % 12
        return f"A {feet}'{inches}\" tall, {self.weight} lbs, {self.build.value} build, {self.hair_color.value if not isinstance(self.hair_color, str) else self.hair_color} hair, {self.eye_color.value} eyes, {self.gender.value}, of {self.race.value} descent, who is a {self.occupation}."

    @staticmethod
    def generate_name(gender: Gender):
        fake = Faker()
        if gender == Gender.MALE:
            return fake.first_name_male()
        elif gender == Gender.FEMALE:
            return fake.first_name_female()
        else:
            return fake.first_name()

    @staticmethod
    def generate_title(gender: Gender):
        if gender == Gender.MALE:
            return choice(list(MaleTitle) + [None])
        elif gender == Gender.FEMALE:
            return choice(list(FemaleTitle) + [None])
        else:
            return choice(list(MaleTitle) + list(FemaleTitle) + [None])


class CharacterFactory:
    def create_random_adult_character(self) -> Character:
        fake = Faker()
        gender = choices(
            [Gender.MALE, Gender.FEMALE, Gender.INTERSEX, Gender.OTHER],
            weights=[0.45, 0.5, 0.03, 0.02],
            k=1,
        )[0]

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

        # Generate height based on gender using a normal distribution
        height = int(
            round(
                normalvariate(
                    mu=63 if gender == Gender.FEMALE else 68,  # Mean height in inches
                    sigma=3.5,  # Standard deviation in inches
                )
            )
        )
        # Clamp height to a reasonable range (e.g., 4'0" to 8'0")
        height = max(48, min(96, height))

        # Generate BMI using a normal distribution and clamp it
        bmi = normalvariate(mu=24, sigma=4)
        bmi = max(16, min(40, bmi))  # Clamp BMI to a reasonable range

        # Calculate weight based on height and BMI, add variation, and clamp
        base_weight = bmi * (height**2) / 703
        weight_val = round(normalvariate(mu=base_weight, sigma=10))
        weight_val = max(90, min(400, weight_val))  # Clamp weight
        weight = weight_val  # Assign int directly, removed Pounds() call

        # Determine build based on BMI
        build = None
        if bmi < 18.5:
            build = Build.SLIM
        elif 18.5 <= bmi < 25:
            build = choice([Build.SLIM, Build.AVERAGE])
        elif 25 <= bmi < 30:
            build = choice([Build.AVERAGE, Build.FAT, Build.ATHLETIC])
        else:  # bmi >= 30
            build = Build.FAT

        # Strength remains random for now, could be linked later
        strength = fake.random_int(min=1, max=10)

        character = Character(
            id=uuid4(),
            name=Character.generate_name(gender),
            family_name=fake.last_name(),
            title=Character.generate_title(gender),
            birth_date=fake.date_of_birth(minimum_age=18, maximum_age=60),
            birth_place=fake.city(),
            mother=None,
            father=None,
            siblings=[],
            children=[],
            gender=gender,
            height=height,
            weight=weight,  # Use the calculated int weight
            blood_type=choice(list(BloodType)),
            eye_color=choice(list(EyeColor)),
            hair_color=hair_color,
            race=choice(list(Race)),
            build=build,  # Use the calculated build
            strength=strength,  # Use the calculated strength
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
