from animals import Animal, Dog, Bird, Fish


class AnimalsCreator(Dog, Bird, Fish, Animal):

    @staticmethod
    def create_animal(name: str, weight: int, age: int):
        return Animal(name, weight, age)

    @staticmethod
    def create_bird(name: str, weight: int, age: int, bird_type: str, sound: str):
        return Bird(name, weight, age, bird_type, sound)

    @staticmethod
    def create_dog(name: str, weight: int, age: int, dog_type: str):
        return Dog(name, weight, age, dog_type)

    @staticmethod
    def create_fish(name: str, weight: int, age: int, fish_type: str):
        return Fish(name, weight, age, fish_type)


if __name__ == '__main__':
    jack = AnimalsCreator.create_dog('Джек', 12, 5, 'Питбуль')
    print(jack)
    freddy = AnimalsCreator.create_fish('Фредди', 1, 1, 'Камбала')
    print(freddy)
    anim = AnimalsCreator.create_animal('Кто-то', 30, 4)
    print(anim)
