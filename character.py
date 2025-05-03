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


class CharacterBuilder:
    def __init__(self):
        # Initialize all attributes to None or a sensible default
        self._id = None
        self._name = None
        self._family_name = None
        self._title = None
        self._birth_date = None
        self._birth_place = None
        self._mother = None
        self._father = None
        self._siblings = []
        self._children = []
        self._gender = None
        self._height = None  # inches
        self._weight = None  # lbs
        self._blood_type = None
        self._eye_color = None
        self._hair_color = None
        self._race = None
        self._build = None
        self._strength = None
        self._endurance = None
        self._dexterity = None
        self._constitution = None
        self._intelligence = None
        self._wisdom = None
        self._charisma = None
        self._traits = None
        self._occupation = None
        self._hobbies = []
        self._relationships = []
        self._history = []
        self._primary_address = None
        self._min_age = 18  # Default adult
        self._max_age = 60  # Default adult
        self._is_bald = None  # Track baldness separately

    # --- Setter Methods ---
    def set_id(self, val: uuid4) -> "CharacterBuilder":
        self._id = val
        return self

    def set_name(self, val: str) -> "CharacterBuilder":
        self._name = val
        return self

    def set_family_name(self, val: str) -> "CharacterBuilder":
        self._family_name = val
        return self

    def set_title(self, val: MaleTitle | FemaleTitle | None) -> "CharacterBuilder":
        self._title = val
        return self

    def set_birth_date(self, val: datetime) -> "CharacterBuilder":
        self._birth_date = val
        # Clear age range if specific date is set
        self._min_age = None
        self._max_age = None
        return self

    def set_age_range(self, min_age: int, max_age: int) -> "CharacterBuilder":
        self._min_age = min_age
        self._max_age = max_age
        # Clear specific birth date if age range is set
        self._birth_date = None
        return self

    def set_birth_place(self, val: str) -> "CharacterBuilder":
        self._birth_place = val
        return self

    def set_mother(self, val: "Character") -> "CharacterBuilder":
        self._mother = val
        return self

    def set_father(self, val: "Character") -> "CharacterBuilder":
        self._father = val
        return self

    def set_siblings(self, val: list["Character"]) -> "CharacterBuilder":
        self._siblings = val
        return self

    def add_sibling(self, val: "Character") -> "CharacterBuilder":
        self._siblings.append(val)
        return self

    def set_children(self, val: list["Character"]) -> "CharacterBuilder":
        self._children = val
        return self

    def add_child(self, val: "Character") -> "CharacterBuilder":
        self._children.append(val)
        return self

    def set_gender(self, val: Gender) -> "CharacterBuilder":
        self._gender = val
        return self

    def set_height(self, val: int) -> "CharacterBuilder":
        self._height = val
        return self

    def set_weight(self, val: int) -> "CharacterBuilder":
        self._weight = val
        return self

    def set_blood_type(self, val: BloodType) -> "CharacterBuilder":
        self._blood_type = val
        return self

    def set_eye_color(self, val: EyeColor) -> "CharacterBuilder":
        self._eye_color = val
        return self

    def set_hair_color(
        self, val: DyedHairColor | NaturalHairColor | str
    ) -> "CharacterBuilder":
        self._hair_color = val
        if val == "Bald":
            self._is_bald = True
        else:
            self._is_bald = False  # Explicitly not bald if color set
        return self

    def set_race(self, val: Race) -> "CharacterBuilder":
        self._race = val
        return self

    def set_build(self, val: Build) -> "CharacterBuilder":
        self._build = val
        return self

    def set_strength(self, val: int) -> "CharacterBuilder":
        self._strength = val
        return self

    def set_endurance(self, val: int) -> "CharacterBuilder":
        self._endurance = val
        return self

    def set_dexterity(self, val: int) -> "CharacterBuilder":
        self._dexterity = val
        return self

    def set_constitution(self, val: int) -> "CharacterBuilder":
        self._constitution = val
        return self

    def set_intelligence(self, val: int) -> "CharacterBuilder":
        self._intelligence = val
        return self

    def set_wisdom(self, val: int) -> "CharacterBuilder":
        self._wisdom = val
        return self

    def set_charisma(self, val: int) -> "CharacterBuilder":
        self._charisma = val
        return self

    def set_traits(self, val: list[str]) -> "CharacterBuilder":
        self._traits = val
        return self

    def set_occupation(self, val: str) -> "CharacterBuilder":
        self._occupation = val
        return self

    def set_hobbies(self, val: list[str]) -> "CharacterBuilder":
        self._hobbies = val
        return self

    def add_hobby(self, val: str) -> "CharacterBuilder":
        self._hobbies.append(val)
        return self

    def set_relationships(self, val: list["Relationship"]) -> "CharacterBuilder":
        self._relationships = val
        return self

    def add_relationship(self, val: "Relationship") -> "CharacterBuilder":
        self._relationships.append(val)
        return self

    def set_history(self, val: list[Event]) -> "CharacterBuilder":
        self._history = val
        return self

    def add_history_event(self, val: Event) -> "CharacterBuilder":
        self._history.append(val)
        return self

    def set_primary_address(self, val: str) -> "CharacterBuilder":
        self._primary_address = val
        return self

    def set_bald(self, val: bool) -> "CharacterBuilder":
        self._is_bald = val
        if val:
            self._hair_color = "Bald"
        # If set to False, hair color generation will proceed normally
        return self

    def build(self) -> Character:
        fake = Faker()

        # --- Attribute Generation (Order Matters!) ---

        _id = self._id or uuid4()
        _gender = (
            self._gender
            or choices(
                [Gender.MALE, Gender.FEMALE, Gender.INTERSEX, Gender.OTHER],
                weights=[0.45, 0.5, 0.03, 0.02],
                k=1,
            )[0]
        )
        _name = self._name or Character.generate_name(_gender)
        _family_name = self._family_name or fake.last_name()
        _title = (
            self._title
            if self._title is not None
            else Character.generate_title(_gender)
        )

        if self._birth_date:
            _birth_date = self._birth_date
        elif self._min_age is not None and self._max_age is not None:
            _birth_date = fake.date_of_birth(
                minimum_age=self._min_age, maximum_age=self._max_age
            )
        else:
            # Default if neither date nor range is set (e.g. 0-100)
            _birth_date = fake.date_of_birth(minimum_age=0, maximum_age=100)

        _birth_place = self._birth_place or fake.city()

        # --- Hair Generation ---
        _hair_color = self._hair_color
        _is_bald = self._is_bald
        if _is_bald is None:  # Only determine randomly if not explicitly set
            if (
                _gender is not Gender.FEMALE
                and choices([True, False], weights=[0.15, 0.85], k=1)[0]
            ):
                _is_bald = True
            else:
                _is_bald = False

        if _is_bald:
            _hair_color = "Bald"
        elif _hair_color is None:  # Only generate if not bald and not explicitly set
            hair_type = choices(["natural", "dyed"], weights=[0.85, 0.15], k=1)[0]
            _hair_color = choice(
                list(DyedHairColor if hair_type == "dyed" else NaturalHairColor)
            )
        # If _hair_color was already set (and not "Bald"), use the set value.

        # --- Height, Weight, Build Generation ---
        _height = self._height
        _weight = self._weight
        _build = self._build
        _bmi = None

        if _height is None:
            # Generate height based on gender
            _height = int(
                round(
                    normalvariate(mu=63 if _gender == Gender.FEMALE else 68, sigma=3.5)
                )
            )
            _height = max(48, min(96, _height))  # Clamp height

        if (
            _weight is None or _build is None
        ):  # Need to calculate BMI if weight or build isn't set
            # Generate BMI
            _bmi = normalvariate(mu=24, sigma=4)
            _bmi = max(16, min(40, _bmi))  # Clamp BMI

        if _weight is None:
            # Calculate weight based on height and BMI
            base_weight = _bmi * (_height**2) / 703
            _weight = round(normalvariate(mu=base_weight, sigma=10))
            _weight = max(90, min(400, _weight))  # Clamp weight

        if _build is None:
            # Determine build based on BMI
            if _bmi < 18.5:
                _build = Build.SLIM
            elif 18.5 <= _bmi < 25:
                _build = choice([Build.SLIM, Build.AVERAGE])
            elif 25 <= _bmi < 30:
                _build = choice([Build.AVERAGE, Build.FAT, Build.ATHLETIC])
            else:  # bmi >= 30
                _build = Build.FAT

        # --- Other Attributes ---
        _strength = self._strength or fake.random_int(min=1, max=10)
        _endurance = self._endurance or fake.random_int(min=1, max=10)
        _dexterity = self._dexterity or fake.random_int(min=1, max=10)
        _constitution = self._constitution or fake.random_int(min=1, max=10)
        _intelligence = self._intelligence or fake.random_int(min=1, max=10)
        _wisdom = self._wisdom or fake.random_int(min=1, max=10)
        _charisma = self._charisma or fake.random_int(min=1, max=10)
        _traits = self._traits or [choice(TRAITS_LIST_1), choice(TRAITS_LIST_2)]
        _occupation = self._occupation or fake.job()
        _primary_address = self._primary_address or fake.address()
        _blood_type = self._blood_type or choice(list(BloodType))
        _eye_color = self._eye_color or choice(list(EyeColor))
        _race = self._race or choice(list(Race))

        # Instantiate the character
        return Character(
            id=_id,
            name=_name,
            family_name=_family_name,
            title=_title,
            birth_date=_birth_date,
            birth_place=_birth_place,
            mother=self._mother,
            father=self._father,
            siblings=self._siblings,
            children=self._children,
            gender=_gender,
            height=_height,
            weight=_weight,
            blood_type=_blood_type,
            eye_color=_eye_color,
            hair_color=_hair_color,
            race=_race,
            build=_build,
            strength=_strength,
            endurance=_endurance,
            dexterity=_dexterity,
            constitution=_constitution,
            intelligence=_intelligence,
            wisdom=_wisdom,
            charisma=_charisma,
            traits=_traits,
            occupation=_occupation,
            hobbies=self._hobbies,
            relationships=self._relationships,
            history=self._history,
            primary_address=_primary_address,
        )
