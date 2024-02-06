from datetime import datetime

from homework_21.human import Human


class Pet:

    def __init__(self, name, type_, fav_food):
        self.name = name
        self.type = type_
        self.fav_food = fav_food

    def __str__(self):
        return f'{self.type} {self.name} which likes {self.fav_food}'


class HumanWithPet(Human):

    def __init__(self, first: str, last: str, dob: datetime, pets: list[Pet] | None = None):
        super().__init__(first, last, dob)
        if not pets:
            pets = []
        self._pets = pets

    def __str__(self):
        pet_count = len(self._pets)
        pet_count_string = "pets" if pet_count > 1 else "pet"
        pets_string = ", ".join([str(pet) for pet in self._pets])
        if pet_count > 0:
            return f"{super().__str__()} with {pet_count} {pet_count_string}: {pets_string}"

        return f"{super().__str__()} with no pets"

    def adopt_pet(self, pet: Pet):
        self._pets.append(pet)

    def give_away_pet(self, pet: Pet):
        self._pets.remove(pet)


if __name__ == '__main__':
    marius = HumanWithPet('Marius', 'Tr', datetime(1998, 1, 30))
    print(marius.get_age())
    p1 = Pet("John", "Dog", "Bones")
    print(p1)
    print(marius)
    marius.adopt_pet(p1)
    print(marius)
    p2 = Pet("Kisses", "Cat", "Whiskas")
    marius.adopt_pet(p2)
    print(marius)
    marius.give_away_pet(p1)
    print(marius)

    marius._pets.clear()
