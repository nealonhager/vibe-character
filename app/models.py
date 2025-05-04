from .extensions import db
import uuid
from sqlalchemy import CheckConstraint
from faker import Faker
from datetime import datetime, timezone, date

# Import Enums (adjust path if enums.py is moved)
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
    RelationshipStatus,
    RelationshipType,
)

# Association table for Character siblings (many-to-many self-referential)
character_siblings = db.Table(
    "character_siblings",
    db.Column(
        "character_id",
        db.UUID(as_uuid=True),
        db.ForeignKey("character.id"),
        primary_key=True,
    ),
    db.Column(
        "sibling_id",
        db.UUID(as_uuid=True),
        db.ForeignKey("character.id"),
        primary_key=True,
    ),
)

# Association table for Event participants (many-to-many)
event_characters = db.Table(
    "event_characters",
    db.Column("event_id", db.Integer, db.ForeignKey("event.id"), primary_key=True),
    db.Column(
        "character_id",
        db.UUID(as_uuid=True),
        db.ForeignKey("character.id"),
        primary_key=True,
    ),
)


class Character(db.Model):
    __tablename__ = "character"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Identity
    name = db.Column(db.String(100), nullable=False)
    family_name = db.Column(db.String(100), nullable=False)
    # Store enum values; handle potential None for title
    title_str = db.Column(
        "title", db.String(50), nullable=True
    )  # Store title as string

    # Lineage
    birth_date = db.Column(db.Date, nullable=True)  # Nullable for flexibility
    birth_place = db.Column(db.String(150), nullable=True)
    mother_id = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("character.id"), nullable=True
    )
    father_id = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("character.id"), nullable=True
    )

    mother = db.relationship(
        "Character",
        remote_side=[id],
        foreign_keys=[mother_id],
        backref=db.backref("children_of_mother", lazy="dynamic"),
    )
    father = db.relationship(
        "Character",
        remote_side=[id],
        foreign_keys=[father_id],
        backref=db.backref("children_of_father", lazy="dynamic"),
    )

    # Siblings (using association table)
    siblings = db.relationship(
        "Character",
        secondary=character_siblings,
        primaryjoin=(id == character_siblings.c.character_id),
        secondaryjoin=(id == character_siblings.c.sibling_id),
        backref=db.backref("related_siblings", lazy="dynamic"),
        lazy="dynamic",
    )

    # Children (one-to-many, derived from mother/father relationships)
    # We can access children via mother.children_of_mother or father.children_of_father

    # Physical
    gender = db.Column(db.Enum(Gender), nullable=True)
    height = db.Column(db.Integer, nullable=True)  # Height in inches
    weight = db.Column(db.Integer, nullable=True)  # Weight in lbs
    blood_type = db.Column(db.Enum(BloodType), nullable=True)
    eye_color = db.Column(db.Enum(EyeColor), nullable=True)
    # Store hair color as string, allowing 'Bald' or enum values
    hair_color_str = db.Column("hair_color", db.String(50), nullable=True)
    race = db.Column(db.Enum(Race), nullable=True)
    build = db.Column(db.Enum(Build), nullable=True)

    # Abilities (nullable for flexibility during creation)
    strength = db.Column(db.Integer, nullable=True)
    endurance = db.Column(db.Integer, nullable=True)
    dexterity = db.Column(db.Integer, nullable=True)
    constitution = db.Column(db.Integer, nullable=True)
    intelligence = db.Column(db.Integer, nullable=True)
    wisdom = db.Column(db.Integer, nullable=True)
    charisma = db.Column(db.Integer, nullable=True)

    # Traits & Hobbies
    traits = db.Column(db.JSON, nullable=True)  # Store as list of strings
    hobbies = db.Column(db.JSON, nullable=True)  # Store as list of strings

    # Other
    occupation = db.Column(db.String(100), nullable=True)
    primary_address = db.Column(db.Text, nullable=True)

    # NEW FIELD
    creation_date = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )  # Added creation date

    # Relationships - Define relationships after basic columns
    relationships = db.relationship(
        "Relationship",
        foreign_keys="[Relationship.character1_id]",
        back_populates="character1",
        cascade="all, delete-orphan",
    )
    related_to = db.relationship(
        "Relationship",
        foreign_keys="[Relationship.character2_id]",
        back_populates="character2",
        cascade="all, delete-orphan",
    )

    # History (Events)
    history = db.relationship(
        "Event",
        secondary=event_characters,
        back_populates="characters_involved",
        lazy="dynamic",
    )

    @staticmethod
    def generate_name(gender: Gender | None = None) -> str:
        fake = Faker()
        if gender == Gender.MALE:
            return fake.first_name_male()
        elif gender == Gender.FEMALE:
            return fake.first_name_female()
        else:
            return fake.first_name()

    # Add helper properties to handle enums/strings if needed
    @property
    def title(self):
        # Logic to return MaleTitle/FemaleTitle enum or None based on title_str
        if not self.title_str:
            return None
        return self.title_str

    @title.setter
    def title(self, value: MaleTitle | FemaleTitle | None):
        self.title_str = value.value if value else None

    @property
    def hair_color(self):
        # Logic to return HairColor enum or "Bald"
        if self.hair_color_str == "Bald":
            return "Bald"
        if not self.hair_color_str:
            return None
        return self.hair_color_str

    @hair_color.setter
    def hair_color(self, value: NaturalHairColor | DyedHairColor | str | None):
        if isinstance(value, (NaturalHairColor, DyedHairColor)):
            self.hair_color_str = value.value
        else:
            self.hair_color_str = value  # Handles "Bald" or None

    @property
    def age(self) -> int | None:
        """Calculates the character's age based on birth_date."""
        if not self.birth_date:
            return None
        today = date.today()
        # Calculate age based on year, adjusting for month and day
        years = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            years -= 1
        return years

    @property
    def physical_description(self) -> str:
        feet = self.height // 12
        inches = self.height % 12
        height_str = f"{feet}'{inches}\" tall"
        weight_str = f"{self.weight} lbs"
        age_str = f"{self.age} years old"
        build_str = f"{self.build.value} build"
        hair_color_str = (
            self.hair_color.value
            if not isinstance(self.hair_color, str)
            else self.hair_color
        )
        eye_color_str = self.eye_color.value
        gender_str = self.gender.value
        race_str = self.race.value
        occupation_str = self.occupation
        return f"A {height_str}, {weight_str}, {age_str}, {build_str}, {hair_color_str} hair, {eye_color_str} eyes, {gender_str}, of {race_str} descent, who is a {occupation_str}."

    def __repr__(self) -> str:
        return f"<Character {self.name} {self.family_name} ({self.id})>"


class Event(db.Model):
    __tablename__ = "event"

    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing primary key
    name = db.Column(db.String(200), nullable=False)
    # event_count = db.Column(db.Integer, unique=True, nullable=False) # Add if needed

    characters_involved = db.relationship(
        "Character",
        secondary=event_characters,
        back_populates="history",
        lazy="dynamic",
    )

    def __repr__(self):
        return f"<Event {self.id}: {self.name}>"


# New Relationship Model
class Relationship(db.Model):
    __tablename__ = "relationship"

    id = db.Column(db.Integer, primary_key=True)
    character1_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("character.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    character2_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("character.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    relationship_type = db.Column("type", db.Enum(RelationshipType), nullable=False)
    status = db.Column(db.Enum(RelationshipStatus), nullable=False)
    start_date = db.Column(db.Date, nullable=True)

    character1 = db.relationship(
        "Character", foreign_keys=[character1_id], back_populates="relationships"
    )
    # Define relationship to character2 if needed for querying from Relationship side
    character2 = db.relationship(
        "Character",
        foreign_keys=[character2_id],
        back_populates="related_to",
    )

    # Ensure character1 and character2 are not the same
    __table_args__ = (
        CheckConstraint(
            "character1_id != character2_id", name="ck_relationship_not_self"
        ),
        # Optional: Unique constraint for a pair in one direction
        # db.UniqueConstraint('character1_id', 'character2_id', 'relationship_type', name='uq_relationship_pair_type')
    )

    def __repr__(self):
        return f"<Relationship {self.character1_id} -> {self.character2_id} ({self.relationship_type.value}, {self.status.value})>"


# Example:
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(256))

#     def __repr__(self):
#         return f'<User {self.username}>'
