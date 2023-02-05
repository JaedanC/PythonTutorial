class Game:
    def __init__(self, name, age_rating, platforms):
        self.name = name
        self.age_rating = age_rating
        self.platforms = platforms

class Player:
    def __init__(self, name, age, preferred_platform):
        self.name = name
        self.age = age
        self.preferred_platform = preferred_platform
    
    def can_play(self, game):
        if self.age < game.age_rating:
            return False
        
        for platform in game.platforms:
            if platform == self.preferred_platform:
                return True
        return False
        # or return self.preferred_platform in game.platforms


# You can use this for your own testing
horror = Game("Resident Evil", 18, ["Xbox", "PC", "Playstation"])
racing = Game("Mario Kart", 6, ["Switch"])
shooter = Game("Doom", 15, ["PC", "Xbox", "Switch"])

adult = Player("John Blue", 25, "Xbox")
child = Player("Timmy Green", 8, "Switch")

assert adult.can_play(horror)
assert not adult.can_play(racing)
assert adult.can_play(shooter)
assert not child.can_play(horror)
assert child.can_play(racing)
assert not child.can_play(shooter)