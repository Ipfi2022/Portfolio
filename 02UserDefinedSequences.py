
# Magic mathod _underscore_ 
   # Examples of sequence object , tuple,list & tuple

from collections.abc import Sequence   # Interface 

class Teams(Sequence):
    def __init__(self, values, name="DefaultSequence"):
        self.values = list(values)
        self.name = name
        self.length = len(values)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return self.values[index]

    def __repr__(self):
        return f"{self.name}({self.values})"

teams1 = Teams(("Pirates", "Chiefs"), name="Mzanzi teams")
teams2 = Teams(("United", "City"), name="English Premier League Teams")
teams3 = Teams(("Barca", "Real"), name="LaLiga Teams")


print(teams1)
print(teams2)
print(teams3)

print(teams2[0])

for team in teams1:
    print(team)
