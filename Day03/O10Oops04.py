
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")


ply1 = Player("Sachin", 32)
ply1.get_details()

print("-" * 40)
ply2 = Player("Sourav", 31)
ply2.get_details()

print("-" * 40)
print(ply1.__dict__)
print(ply2.__dict__)

print("-" * 40)
ply2.runs = 75
print(ply2.__dict__)
print(ply1.__dict__)
