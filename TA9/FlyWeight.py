"""
Flyweight pattern is one of the structural design patterns as this pattern provides ways to decrease object
 count thus improving application required objects structure. Flyweight pattern is used when we need to create
  a large number of similar objects (say 105). One important feature of flyweight objects is that they are immutable.
  This means that they cannot be modified once they have been constructed.
"""

class CharacterFlyweight:
    def __init__(self, character):
        self.character = character

class Document:
    def __init__(self):
        self.characters = []
        self.fonts = []

    def add_character(self, character, font):
        flyweight = CharacterFlyweightFactory.get_flyweight(character)
        self.characters.append(flyweight)
        self.fonts.append(font)

    def get_text(self):
        text = ""
        for i in range(len(self.characters)):
            text += self.characters[i].character
        return text

class CharacterFlyweightFactory:
    flyweights = {}

    @staticmethod
    def get_flyweight(character):
        if character not in CharacterFlyweightFactory.flyweights:
            CharacterFlyweightFactory.flyweights[character] = CharacterFlyweight(character)
        return CharacterFlyweightFactory.flyweights[character]

document = Document()
document.add_character("a", "Arial")
document.add_character("b", "Arial")
document.add_character("c", "Arial")
document.add_character("d", "Arial")
document.add_character("a","Ariel")
document.add_character("Z","Times New Roman")

print(document.get_text())
