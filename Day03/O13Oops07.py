
# magic method
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor.....")

    def __str__(self):
        return f"Name is {self.name}\nAge is {self.age}"

ply1 = Player("Sehwag", 33)
# ply1.get_details()

print("-" * 40)

print(str(ply1))                # call __str__()

print("-" * 40)

print(ply1)                     # implicitly calls __str__()

