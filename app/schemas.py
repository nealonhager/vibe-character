from marshmallow import Schema, fields
from marshmallow_enum import EnumField
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


# Helper function to handle complex hair color serialization
def serialize_hair_color(obj):
    if isinstance(obj.hair_color, (NaturalHairColor, DyedHairColor)):
        return obj.hair_color.value
    return obj.hair_color  # Handles "Bald" or other strings


# Helper function to handle title serialization
def serialize_title(obj):
    if isinstance(obj.title, (MaleTitle, FemaleTitle)):
        return obj.title.value
    return obj.title  # Handles None


class CharacterSchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.Str(required=True)
    family_name = fields.Str(required=True)
    # Allow string input for title, model handles conversion
    title = fields.Str(allow_none=True)
    birth_date = fields.Date()
    birth_place = fields.Str()
    mother_id = fields.UUID()
    father_id = fields.UUID()
    # Nested relationships might be complex, consider separate endpoints or simplified views
    # siblings = fields.List(fields.Nested('self', only=("id", "name", "family_name"), dump_only=True)) # Example of simple nesting
    # children = fields.List(fields.Nested('self', only=("id", "name", "family_name"), dump_only=True)) # Example

    gender = EnumField(Gender, by_value=True)
    height = fields.Int()
    weight = fields.Int()
    blood_type = EnumField(BloodType, by_value=True)
    eye_color = EnumField(EyeColor, by_value=True)
    # Allow string input for hair color, model handles conversion
    hair_color = fields.Str(allow_none=True)
    race = EnumField(Race, by_value=True)
    build = EnumField(Build, by_value=True)

    strength = fields.Int()
    endurance = fields.Int()
    dexterity = fields.Int()
    constitution = fields.Int()
    intelligence = fields.Int()
    wisdom = fields.Int()
    charisma = fields.Int()

    traits = fields.List(fields.Str())
    hobbies = fields.List(fields.Str())

    occupation = fields.Str()
    primary_address = fields.Str()

    # Add the generated physical description (read-only)
    physical_description = fields.Str(dump_only=True)

    # Method field implementations (can be removed if not needed elsewhere)
    # def get_serializable_hair_color(self, obj):
    #     return serialize_hair_color(obj)
    #
    # def get_serializable_title(self, obj):
    #     return serialize_title(obj)

    # Relationships and History are often handled via separate endpoints for clarity
    # relationships = fields.Nested('RelationshipSchema', many=True, dump_only=True) # Example if RelationshipSchema exists
    # history = fields.Nested('EventSchema', many=True, dump_only=True)          # Example if EventSchema exists


# Simple Schemas for potential nesting (add details as needed)
# class RelationshipSchema(Schema):
#     id = fields.Int(dump_only=True)
#     character2_id = fields.UUID()
#     relationship_type = EnumField(RelationshipType, by_value=True)
#     status = EnumField(RelationshipStatus, by_value=True)
#     start_date = fields.Date()

# class EventSchema(Schema):
#     id = fields.Int(dump_only=True)
#     name = fields.Str()
