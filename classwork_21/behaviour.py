class Animal:

    def __init__(self, name, species, varsta, color='black'):
        self.name = name
        self.species = species
        self.varsta = varsta
        self.color = color
        self.sleeping = False

    def sleep(self):
        self.sleeping = True
        print(f'{self.species} {self.name} is sleeping')

    def eat(self):
        print(f'{self.species} {self.name} is sleeping')


animal_object = Animal("Kuzea", "Dog", 1, "Blue")
animal_object.sleep()

cat_object = Animal("Valera", species="Cat", varsta=2, color="Red")
print(f"Sleeping: {cat_object.sleeping}")
cat_object.sleep()
print(f"Sleeping: {cat_object.sleeping}")


class Glass:

    def __init__(self, volume_in_glass):
        self.volume = volume_in_glass

    def drink(self, how_much):
        if how_much > self.volume:
            print(f'You are not allowed to drink that much, but you drank it all, which is {self.volume}')
            self.volume = 0
            return
        self.volume -= how_much
        print(f'After drinking {how_much}ml you are left with {self.volume}ml')


glass_1 = Glass()
glass_1.drink(300)
glass_1.drink(300)

glass_2 = Glass(1000)
glass_2.drink(20)


class Computer:

    def turn_on(self):
        pass

