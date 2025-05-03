from character import CharacterBuilder
from enums import Gender

if __name__ == "__main__":
    builder = CharacterBuilder()
    builder.set_age_range(18, 60)
    builder.set_gender(Gender.MALE)
    builder.set_name("John")
    builder.set_family_name("Doe")
    character = builder.build()
    character.print_info()
    print(character.get_physical_description())
