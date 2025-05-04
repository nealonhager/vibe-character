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


class NaturalHairColor(Enum):
    BLACK = "Black"
    BROWN = "Brown"
    RED = "Red"
    BLONDE = "Blonde"
    GRAY = "Gray"
    WHITE = "White"


class DyedHairColor(Enum):
    BLUE = "Blue"
    GREEN = "Green"
    PINK = "Pink"
    PURPLE = "Purple"
    ORANGE = "Orange"


class Race(Enum):
    INUIT = "Inuit"
    NATIVE_AMERICAN = "Native American (North America)"
    CENTRAL_AMERICAN = "Central American (Mexico, Central America)"
    SOUTH_AMERICAN = "South American (Latin America)"
    PACIFIC_ISLANDER = "Pacific Islander"
    NORTHERN_EUROPEAN = "Northern European (Britain, Scandinavia, Germany)"
    SOUTH_EUROPEAN = "South European (Italy, Spain, Greece)"
    EASTERN_EUROPEAN = "Eastern European (Russia, Poland, Ukraine)"
    MIDDLE_EASTERN = "Middle Eastern"
    INDIAN = "Indian (Indian Subcontinent)"
    SOUTH_EAST_ASIAN = "South East Asian"
    NORTH_AFRICAN = "North African"
    AFRICAN = "African (Sub-Saharan Africa)"


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


class RelationshipStatus(Enum):
    EXCELLENT = "Excellent"
    GOOD = "Good"
    NEUTRAL = "Neutral"
    BAD = "Bad"
    TERRIBLE = "Terrible"
    ENEMY = "Enemy"


class RelationshipType(Enum):
    PARENT = "Parent"
    CHILD = "Child"
    SIBLING = "Sibling"
    SPOUSE = "Spouse"
    PARTNER = "Partner"
    FRIEND = "Friend"
    CLOSE_FRIEND = "Close Friend"
    ACQUAINTANCE = "Acquaintance"
    ROMANTIC_INTEREST = "Romantic Interest"
    COLLEAGUE = "Colleague"
    MENTOR = "Mentor"
    MENTEE = "Mentee"
    RIVAL = "Rival"
    ENEMY = "Enemy"
    GUARDIAN = "Guardian"
    WARD = "Ward"


class Hobbies(Enum):
    FARMING = "Farming"
    MINING = "Mining"
    CRAFTING = "Crafting"
    SMITHING = "Smithing"
    COOKING = "Cooking"
    CARPENTRY = "Carpentry"
    TAILORING = "Tailoring"
    WEAVING = "Weaving"
    FISHING = "Fishing"
    HUNTING = "Hunting"
    TRAPPING = "Trapping"
    GARDENING = "Gardening"
    BAKING = "Baking"
    PAINTING = "Painting"
    WRITING = "Writing"
    READING = "Reading"
    MUSIC = "Music"
    DANCING = "Dancing"
    DRAWING = "Drawing"
    SCULPTING = "Sculpting"
    POTTERY = "Pottery"
    CARTOONING = "Cartooning"
    PHOTOGRAPHY = "Photography"
    VIDEOGRAPHY = "Videography"
    SEWING = "Sewing"
    VIDEO_GAMING = "Video Gaming"
    TABLE_GAMING = "Tabletop Gaming"
    ARTS = "Arts"
    SCIENCE = "Science"
    HISTORY = "History"
    LITERATURE = "Literature"
    PHILOSOPHY = "Philosophy"
    THEOLOGY = "Theology"
    LAW = "Law"
    MEDICINE = "Medicine"
    ENGINEERING = "Engineering"
    MATHEMATICS = "Mathematics"
    COMPUTER_SCIENCE = "Computer Science"
