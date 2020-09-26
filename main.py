class Pokemon:
  def __init__(self, name, level, pokemon_type, maximum_health, current_health, is_knocked_out):
    self.name = name
    self.level = level
    self.pokemon_type = pokemon_type
    self.maximum_health = maximum_health
    self.current_health = current_health
    self.is_knocked_out = is_knocked_out


  def lose_health(self, damage):
    self.current_health -= damage
    if self.current_health == 0:
        self.is_knocked_out = True
        return f"{self.name} got {damage} points of Damage and was Knocked Out!"
    return f"{self.name} got Damage of {damage} points. Current Health is {self.current_health} HP."

  def gain_health(self, potion_item):
    self.current_health += potion_item
    return f"{self.name} gained {potion_item} HP. Current Health is {self.current_health} HP."


  def knock_out(self):
    if self.current_health == 0:
      self.is_knocked_out = True
    return f"{self.name} got Knocked Out!"

  def attack(self, other_pokemon):
      if self.pokemon_type > other_pokemon.pokemon_type:
          other_pokemon.lose_health(self.level * 2)
          return f"""{self.name} attacked {other_pokemon.name} and gave the damage of {self.level * 2}.
                {self.name}'s Health: {self.current_health}
                {other_pokemon.name}'s Health: {other_pokemon.current_health}
                 """

      if self.pokemon_type < other_pokemon.pokemon_type:
          other_pokemon.lose_health(self.level / 2)
          return f"""{self.name} attacked {other_pokemon.name} and gave the damage of {self.level / 2}.
                {self.name}'s Health: {self.current_health}
                {other_pokemon.name}'s Health: {other_pokemon.current_health}
"""


  def __repr__(self):
    return f"""
           Name: {self.name}
           Type: {self.pokemon_type}
           Max. Health: {self.maximum_health}
           Current Health: {self.current_health}
           Knocked Out: {self.is_knocked_out} 

           """



pikachu = Pokemon("Pikachu", 4, 'electric', 100, 100, False)
arcanine = Pokemon("Arcanine", 6, 'fire', 100, 100, False)


potion = ({'elixir': 20, 'cracker': 15, 'stone_of_eternity': 60})
elixir = 20
cracker = 15
stone_of_eternity = 60

print(pikachu.attack(arcanine))
print(pikachu.attack(arcanine))
print(arcanine.attack(pikachu))
print(pikachu.attack(arcanine))




