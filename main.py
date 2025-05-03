from character import CharacterFactory

if __name__ == "__main__":
    character_factory = CharacterFactory()
    character = character_factory.create_random_adult_character()
    character.print_info()
    print(character.get_physical_description())
