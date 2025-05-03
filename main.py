from character import CharacterBuilder
from event import Event


if __name__ == "__main__":
    builder = CharacterBuilder()
    builder.set_occupation("Bank Robber")
    bank_robber = builder.build()
    builder.set_occupation("Police Officer")
    police_officer = builder.build()

    Event(f"{bank_robber.name} {bank_robber.family_name} robs a bank", [bank_robber])
    Event(
        f"{police_officer.name} {police_officer.family_name} arrests {bank_robber.name} {bank_robber.family_name}",
        [bank_robber, police_officer],
    )
    Event(
        f"{bank_robber.name} {bank_robber.family_name} is sentenced to 10 years in prison",
        [bank_robber],
    )
    Event(
        f"{bank_robber.name} {bank_robber.family_name} escapes from prison",
        [bank_robber],
    )
    Event(
        f"{police_officer.name} {police_officer.family_name} recaptures {bank_robber.name} {bank_robber.family_name}",
        [bank_robber, police_officer],
    )

    print([str(event) for event in bank_robber.history])
    print([str(event) for event in police_officer.history])
