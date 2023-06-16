class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"The dog's name is {self.name} and it is {self.age} years old.")

    def get_info(self):
        print(f"The dog's coat color is {self.coat_color}.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, num_of_toys):
        super().__init__(name, age, coat_color)
        self.num_of_toys = num_of_toys

    def play(self):
        print(f"{self.name} is playing and having fun with its {self.num_of_toys} toys")

    def bark(self):
        print(f"{self.name} is barking loudly!")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, weight):
        super().__init__(name, age, coat_color)
        self.weight = weight

    def eat(self):
        print(
            f"{self.name} is eating a big meal even though its weight is {self.weight} Kgs"
        )

    def sleep(self):
        print(f"{self.name} is sleeping soundly!")


if __name__ == "__main__":
    dog = Dog("Max", 5, "brown")
    dog.description()
    dog.get_info()

    jack_russell_terrier = JackRussellTerrier("Jack", 3, "white", 2)
    jack_russell_terrier.play()
    jack_russell_terrier.bark()

    bulldog = Bulldog("Rocky", 7, "red", 50)
    bulldog.eat()
    bulldog.sleep()