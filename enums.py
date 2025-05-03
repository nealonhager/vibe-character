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
