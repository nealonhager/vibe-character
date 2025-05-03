from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    INTERSEX = "Intersex"
    OTHER = "Other"


class BloodType(Enum):
    A_POS = "A+"
    A_NEG = "A-"
    B_POS = "B+"
    B_NEG = "B-"
    O_POS = "O+"
    O_NEG = "O-"
    AB_POS = "AB+"
    AB_NEG = "AB-"


class EyeColor(Enum):
    LIGHT_BLUE = "Light Blue"
    BLUE = "Blue"
    GREEN = "Green"
    HAZEL = "Hazel"
    BROWN = "Brown"
    BLACK = "Black"
    RED = "Red"
    YELLOW = "Yellow"
    ORANGE = "Orange"
    PINK = "Pink"
    PURPLE = "Purple"
    GRAY = "Gray"


class HairColor(Enum):
    BLACK = "Black"
    BROWN = "Brown"
    RED = "Red"
    BLONDE = "Blonde"
    GRAY = "Gray"
    WHITE = "White"
    BLUE = "Blue"
    GREEN = "Green"
    PINK = "Pink"
    PURPLE = "Purple"
    ORANGE = "Orange"


class Race(Enum):
    INUIT = "Inuit"
    NATIVE_AMERICAN = "Native American"
    CENTRAL_AMERICAN = "Central American"
    SOUTH_AMERICAN = "South American"
    PACIFIC_ISLANDER = "Pacific Islander"
    NORTHERN_EUROPEAN = "Northern European"
    SOUTH_EUROPEAN = "South European"
    EASTERN_EUROPEAN = "Eastern European"
    MIDDLE_EASTERN = "Middle Eastern"
    INDIAN = "Indian (Indian Subcontinent)"
    SOUTH_EAST_ASIAN = "South East Asian"
    NORTH_AFRICAN = "North African"
    AFRICAN = "African"


class MaleTitle(Enum):
    LORD = "Lord"
    SIR = "Sir"
    HONORABLE = "Honorable"
    BARON = "Baron"
    COUNT = "Count"
    DUKE = "Duke"
    PRINCE = "Prince"
    KING = "King"
    EMPEROR = "Emperor"


class FemaleTitle(Enum):
    LADY = "Lady"
    QUEEN = "Queen"
    EMPRESS = "Empress"
    BARONESS = "Baroness"
    COUNTESSE = "Countess"
    DUCHESS = "Duchess"
    PRINCESS = "Princess"
    MADAME = "Madame"


class Build(Enum):
    SLIM = "Slim"
    ATHLETIC = "Athletic"
    AVERAGE = "Average"
    SOFT = "Soft"
    FAT = "Fat"
