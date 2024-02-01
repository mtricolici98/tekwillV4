class Animal:

    def __init__(self, name, species, varsta, color='black'):
        self.name = name
        self.species = species
        self.varsta = varsta
        self.color = color

    def sleep(self):
        print(f'{self.species} {self.name} is sleeping')


animal_object = Animal("Kuzea", "Dog", 1, "Blue")
animal_object.sleep()
print(type(animal_object))

print(animal_object.name)
print(animal_object.species)
print(animal_object.varsta)

cat_object = Animal("Valera", species="Cat", varsta=2, color="Red")

print(cat_object.name)
print(cat_object.species)

print(cat_object.color)

print(animal_object.color)
animal_object.color = 'red'
print(animal_object.color)

cat_object.sleep()
