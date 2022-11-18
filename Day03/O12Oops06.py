
class Player:

    team = "India"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor.....")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def ChangeTeam(cls, team):
        cls.team = team

    @classmethod
    def CreatePlayer(cls, fname, lname, age):
        print("Factory...")
        return cls(f"Mr.{fname} {lname}", age)              # calls the __init__()

ply1 = Player("Virat Kholi", 35)
ply1.get_details()

print("-" * 40)

Player.ChangeTeam("KKR")
print(f"Player :{Player.team}")
print(f"ply1 :{ply1.team}")

print("-" * 40)
# taking the name in the form of fname and lname
ply2 = Player.CreatePlayer("Rohit", "Sharma", 34)

ply2.get_details()