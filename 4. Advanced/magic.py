class Game:
    def __init__(self, name, age_rating, platforms):
        self.name = name
        self.age_rating = age_rating
        self.platforms = platforms

    def __repr__(self):
        # This method expects a string to be returned
        output = f"Game: {self.name}\n" + \
            f"Age Rating: {self.age_rating}\n" + \
            f"Platforms: {self.platforms}"
        return output

deep_rock = Game("Deep Rock Galatic", 16, ["PC", "Xbox"])
print(deep_rock)