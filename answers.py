class User:
    def __init__(self, name:str, nationality:str):
        self.name = name
        self.origin = nationality

    def details(self):
        print(f"Hello! Your name is {self.name} and you are from {self.origin}.")

    def greet(self):
        print("Hello! What's good?!")

class Human(User):
    def __init__(self, name, nationality, race):
        super().__init__(name, nationality)
        self.race = race

    def details(self):
        return f'Hello {self.name.capitalize()}, you are from {self.origin} and you are {self.race}.'

if __name__ == '__main__':

    random = User('Demo', 'Earth')
    Kola = Human('Kolawole', 'Nigeria', 'African')

    print(Kola.details())
    random.details()

    Kola.greet()