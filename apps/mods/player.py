
class Player:
    def __init__(self, name: str, team: str, goal: int=0) -> None:
        self.name = name
        self.team = team
        self.goal = goal

kane = Player(
    name="kane", 
    team="tot",
    goal=10)
    
kane.goal=20
print(kane.goal)