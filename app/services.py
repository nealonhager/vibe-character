import uuid
from datetime import date
from random import choice, choices, normalvariate
from faker import Faker

# Adjust import paths as needed based on project structure
from .models import Character

# Assuming enums.py is in the root directory
import sys
import os

# Correctly join path components to add the project root directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
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

# Define the trait lists (consider moving these to a config or constants file)
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


class CharacterBuilder:
    def __init__(self):
        # Initialize attributes corresponding to the Character model
        self._id: uuid.UUID | None = None
        self._name: str | None = None
        self._family_name: str | None = None
        self._title: MaleTitle | FemaleTitle | None = None  # Store enum or None
        self._birth_date: date | None = None
        self._birth_place: str | None = None
        self._mother_id: uuid.UUID | None = None
        self._father_id: uuid.UUID | None = None
        # Siblings, Children, History, Relationships handled outside builder
        self._gender: Gender | None = None
        self._height: int | None = None  # inches
        self._weight: int | None = None  # lbs
        self._blood_type: BloodType | None = None
        self._eye_color: EyeColor | None = None
        self._hair_color: NaturalHairColor | DyedHairColor | str | None = (
            None  # Store enum or "Bald"
        )
        self._race: Race | None = None
        self._build: Build | None = None
        self._strength: int | None = None
        self._endurance: int | None = None
        self._dexterity: int | None = None
        self._constitution: int | None = None
        self._intelligence: int | None = None
        self._wisdom: int | None = None
        self._charisma: int | None = None
        self._traits: list[str] | None = None
        self._occupation: str | None = None
        self._hobbies: list[str] = []
        self._primary_address: str | None = None
        # Generation parameters
        self._min_age: int | None = 18
        self._max_age: int | None = 60
        self._is_bald: bool | None = None  # Track baldness separately

    # --- Setter Methods ---
    def set_id(self, val: uuid.UUID) -> "CharacterBuilder":
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

    def set_birth_date(self, val: date) -> "CharacterBuilder":
        self._birth_date = val
        self._min_age = None  # Clear age range if specific date is set
        self._max_age = None
        return self

    def set_age_range(self, min_age: int, max_age: int) -> "CharacterBuilder":
        self._min_age = min_age
        self._max_age = max_age
        self._birth_date = None  # Clear specific birth date
        return self

    def set_birth_place(self, val: str) -> "CharacterBuilder":
        self._birth_place = val
        return self

    def set_mother_id(self, val: uuid.UUID | None) -> "CharacterBuilder":
        self._mother_id = val
        return self

    def set_father_id(self, val: uuid.UUID | None) -> "CharacterBuilder":
        self._father_id = val
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
        self, val: NaturalHairColor | DyedHairColor | str | None
    ) -> "CharacterBuilder":
        self._hair_color = val
        if val == "Bald":
            self._is_bald = True
        elif val is not None:
            self._is_bald = False
        # else: self._is_bald remains None or its previously set value
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
        if self._hobbies is None:
            self._hobbies = []
        self._hobbies.append(val)
        return self

    def set_primary_address(self, val: str) -> "CharacterBuilder":
        self._primary_address = val
        return self

    def set_bald(self, val: bool) -> "CharacterBuilder":
        self._is_bald = val
        if val:
            self._hair_color = "Bald"
        # If set to False, hair color generation will proceed normally, unless explicitly set
        elif self._hair_color == "Bald":
            self._hair_color = None  # Allow regeneration if previously bald
        return self

    def build(self) -> Character:
        """Builds and returns a transient Character model instance."""
        fake = Faker()

        # --- Attribute Generation (Order Matters!) ---
        _id = self._id or uuid.uuid4()
        _gender = (
            self._gender
            or choices(
                [Gender.MALE, Gender.FEMALE, Gender.INTERSEX, Gender.OTHER],
                weights=[0.45, 0.5, 0.03, 0.02],
                k=1,
            )[0]
        )
        _name = self._name or Character.generate_name(
            _gender
        )  # Assuming static method exists or adapt
        _family_name = self._family_name or fake.last_name()

        # Generate Title if not set
        _title = self._title
        if _title is None:  # Check if title needs generation (wasn't explicitly set)
            # Generate title based on gender using appropriate Enum subset
            if _gender == Gender.MALE:
                _title = choice(list(MaleTitle) + [None])
            elif _gender == Gender.FEMALE:
                _title = choice(list(FemaleTitle) + [None])
            else:  # For INTERSEX, OTHER, or if gender generation fails
                _title = choice(list(MaleTitle) + list(FemaleTitle) + [None])
        # Now _title holds the determined enum or None

        # Generate Birth Date if not set
        if self._birth_date:
            _birth_date = self._birth_date
        elif self._min_age is not None and self._max_age is not None:
            _birth_date_dt = fake.date_of_birth(
                minimum_age=self._min_age, maximum_age=self._max_age
            )
            _birth_date = date(
                _birth_date_dt.year, _birth_date_dt.month, _birth_date_dt.day
            )
        else:  # Default if neither date nor range is set
            _birth_date_dt = fake.date_of_birth(minimum_age=0, maximum_age=100)
            _birth_date = date(
                _birth_date_dt.year, _birth_date_dt.month, _birth_date_dt.day
            )

        _birth_place = self._birth_place or fake.city()

        # --- Hair Generation ---
        _hair_color_val = self._hair_color  # Store explicitly set value
        _is_bald = self._is_bald

        if _is_bald is None:  # Determine baldness randomly only if not explicitly set
            if (
                _gender is not Gender.FEMALE
                and choices([True, False], weights=[0.15, 0.85], k=1)[0]
            ):
                _is_bald = True
            else:
                _is_bald = False

        if _is_bald:
            _hair_color_val = "Bald"
        elif (
            _hair_color_val is None
        ):  # Generate color only if not bald and not explicitly set
            hair_type = choices(["natural", "dyed"], weights=[0.85, 0.15], k=1)[0]
            _hair_color_val = choice(
                list(DyedHairColor if hair_type == "dyed" else NaturalHairColor)
            )
        # If _hair_color_val was already set (and not "Bald"), use the set value.

        # --- Height, Weight, Build Generation ---
        _height = self._height
        _weight = self._weight
        _build = self._build
        _bmi = None

        if _height is None:
            _height = int(
                round(
                    normalvariate(mu=63 if _gender == Gender.FEMALE else 68, sigma=3.5)
                )
            )
            _height = max(48, min(96, _height))

        if _weight is None or _build is None:
            _bmi = normalvariate(mu=24, sigma=4)
            _bmi = max(16, min(40, _bmi))

        if _weight is None:
            base_weight = _bmi * (_height**2) / 703
            _weight = round(normalvariate(mu=base_weight, sigma=10))
            _weight = max(90, min(400, _weight))

        if _build is None:
            if _bmi < 18.5:
                _build = Build.SLIM
            elif 18.5 <= _bmi < 25:
                _build = choice([Build.SLIM, Build.AVERAGE])
            elif 25 <= _bmi < 30:
                _build = choice([Build.AVERAGE, Build.FAT, Build.ATHLETIC])
            else:
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
        _hobbies = self._hobbies or [
            fake.word() for _ in range(fake.random_int(min=0, max=3))
        ]  # Generate hobbies if empty

        # Instantiate the SQLAlchemy model
        character_instance = Character(
            id=_id,
            name=_name,
            family_name=_family_name,
            # Use the model's setters/properties for title and hair_color
            # title=_title, # Setter will handle None or Enum
            # hair_color=_hair_color_val, # Setter will handle Enum or "Bald"
            birth_date=_birth_date,
            birth_place=_birth_place,
            mother_id=self._mother_id,  # Assign IDs directly
            father_id=self._father_id,  # Assign IDs directly
            gender=_gender,
            height=_height,
            weight=_weight,
            blood_type=_blood_type,
            eye_color=_eye_color,
            race=_race,
            build=_build,
            strength=_strength,
            endurance=_endurance,
            dexterity=_dexterity,
            constitution=_constitution,
            intelligence=_intelligence,
            wisdom=_wisdom,
            charisma=_charisma,
            traits=_traits,  # Assign list directly to JSON field
            occupation=_occupation,
            hobbies=_hobbies,  # Assign list directly to JSON field
            primary_address=_primary_address,
        )
        # Set title and hair_color using properties AFTER instantiation
        # This ensures the setters in the model are correctly used
        character_instance.title = _title
        character_instance.hair_color = _hair_color_val

        return character_instance

    # Add back static methods if needed, adjust imports if they use enums etc.
    # @staticmethod
    # def generate_name(gender: Gender): ...
