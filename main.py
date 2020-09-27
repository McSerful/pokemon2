class Pokemon:
  def __init__(self, name, level, pokemon_type, maximum_health, current_health, is_knocked_out, experience):
    self.name = name
    self.level = level
    self.pokemon_type = pokemon_type
    self.maximum_health = maximum_health
    self.current_health = current_health
    self.is_knocked_out = is_knocked_out
    self.experience = experience




  def level_up(self):
     if self.experience >= 10:
         self.level += 1
         self.experience = 0
     return


  def lose_health(self, damage):
    self.current_health -= damage
    if self.current_health == 0:
        self.is_knocked_out = True
        return f"{self.name} got {damage} points of Damage and was Knocked Out!"
    return f"{self.name} got Damage of {damage} points. Current Health is {self.current_health} HP."

  def gain_health(self, potion_item):
      if self.current_health >= 100:
          return f"{self.name}'s Health is full."
      elif (self.current_health + potion_item) > 100:
          self.current_health += 100 - self.current_health
          return f"{self.name} gained {potion_item} HP. Current Health is {self.current_health} HP."
      self.current_health += potion_item
      return f"{self.name} gained {potion_item} HP. Current Health is {self.current_health} HP."


  def knock_out(self):
    if self.current_health == 0:
      self.is_knocked_out = True
    return f"{self.name} got Knocked Out!"

  def attack(self, other_pokemon):

      if self.is_knocked_out == True:
          return f"This pokemon has been knocked out!"

      elif self.pokemon_type == 'Electric' and other_pokemon.pokemon_type == 'Electric':
          other_pokemon.lose_health(self.level / 2)
          self.experience += 2
          return f"""{self.name} attacked {other_pokemon.name} and gave the damage of {self.level / 2}.
    
          {self.name}'s Health: {self.current_health}
          {other_pokemon.name}'s Health: {other_pokemon.current_health}
          {self.name}'s Experience: {self.experience}
          {self.name}'s Level: {self.level}
    
          """
      elif self.pokemon_type == 'Electric' and other_pokemon.pokemon_type == 'Fire' or other_pokemon.pokemon_type == 'Water':
          other_pokemon.lose_health(self.level * 2)
          self.experience += 4
          return f"""{self.name} attacked {other_pokemon.name} and gave the damage of {self.level * 2}.
    
          {self.name}'s Health: {self.current_health}
          {other_pokemon.name}'s Health: {other_pokemon.current_health}
          {self.name}'s Experience: {self.experience}
          {self.name}'s Level: {self.level}
    
             """
      elif self.pokemon_type == 'Water' and other_pokemon.pokemon_type == 'Fire' or other_pokemon.pokemon_type == 'Water':
          other_pokemon.lose_health(self.level / 2)
          self.experience += 2
          return f"""{self.name} attacked {other_pokemon.name} and gave the damage of {self.level / 2}.
    
          {self.name}'s Health: {self.current_health}
          {other_pokemon.name}'s Health: {other_pokemon.current_health}
          {self.name}'s Experience: {self.experience}
          {self.name}'s Level: {self.level}
    
           """
      elif self.pokemon_type == 'Water' and other_pokemon.pokemon_type == 'Electric':
          other_pokemon.lose_health(self.level * 2)
          self.experience += 4
          return f"""{self.name} attacked {other_pokemon.name} and gave the damage of {self.level * 2}.
    
          {self.name}'s Health: {self.current_health}
          {other_pokemon.name}'s Health: {other_pokemon.current_health}
          {self.name}'s Experience: {self.experience}
          {self.name}'s Level: {self.level}
    
          """
      elif self.pokemon_type == 'Fire' and other_pokemon.pokemon_type == 'Fire':
          other_pokemon.lose_health(self.level / 2)
          self.experience += 2
          return f"""{self.name} attacked {other_pokemon.name} and gave the damage of {self.level / 2}.
    
          {self.name}'s Health: {self.current_health}
          {other_pokemon.name}'s Health: {other_pokemon.current_health}
          {self.name}'s Experience: {self.experience}
          {self.name}'s Level: {self.level}
    
          """
      elif self.pokemon_type == 'Fire' and other_pokemon.pokemon_type == 'Water' or other_pokemon.pokemon_type == 'Electric':
          other_pokemon.lose_health(self.level * 2)
          self.experience += 4
          return f"""{self.name} attacked {other_pokemon.name} and gave the damage of {self.level * 2}.
    
          {self.name}'s Health: {self.current_health}
          {other_pokemon.name}'s Health: {other_pokemon.current_health}
          {self.name}'s Experience: {self.experience}
          {self.name}'s Level: {self.level}
    
          """





  def __repr__(self):
    return f"""
           Name: {self.name}
           Type: {self.pokemon_type}
           Max. Health: {self.maximum_health}
           Current Health: {self.current_health}
           Knocked Out: {self.is_knocked_out} 

           """


class Trainer:
    def __init__(self, name, number_of_potions, pokemons, current_pokemon):
        self.name = name
        self.number_of_potions = number_of_potions
        self.pokemons = pokemons
        self.current_pokemon = current_pokemon
        if self.current_pokemon.experience == 10:
            self.current_pokemon.level += 1

        if len(self.pokemons) > 6:
            return "A Trainer can have up to 6 pokemons only!"


    def switch_pokemon(self, new_pokemon):
        if self.current_pokemon.is_knocked_out == True:
            return f"You cannot select {new_pokemon} since he has been knocked out."
        self.current_pokemon = new_pokemon
        return f"""
{self.name} switched his current pokemon to {new_pokemon.name}.
"""



    def attack(self, other_trainer):

        if other_trainer.current_pokemon.current_health <= 0:
            other_trainer.current_pokemon.is_knocked_out = True
            return "This pokemon has been knocked out. You can't attack him!"


        elif self.current_pokemon.pokemon_type == 'Electric' and other_trainer.current_pokemon.pokemon_type == 'Electric':
            other_trainer.current_pokemon.lose_health(self.current_pokemon.level / 2)
            if other_trainer.current_pokemon.current_health <= 0:
                other_trainer.current_pokemon.current_health = 0
                self.current_pokemon.level_up()
                if self.current_pokemon.experience >= 10:
                    self.current_pokemon.experience += 10 - self.current_pokemon.experience
                self.current_pokemon.experience += 2
                return f"""
{self.name} damaged {other_trainer.name}'s current pokemon ({other_trainer.current_pokemon.name}) by {self.current_pokemon.level / 2}.
{other_trainer.current_pokemon.name}'s Current Health is {other_trainer.current_pokemon.current_health} HP.
{self.current_pokemon.name}'s Experience: {self.current_pokemon.experience}
{self.current_pokemon.name}'s Level: {self.current_pokemon.level}
            """

            self.current_pokemon.level_up()
            self.current_pokemon.experience += 2

            return f"""
{self.name} damaged {other_trainer.name}'s current pokemon ({other_trainer.current_pokemon.name}) by {self.current_pokemon.level/2}.
{other_trainer.current_pokemon.name}'s Current Health is {other_trainer.current_pokemon.current_health} HP.
{self.current_pokemon.name}'s Experience: {self.current_pokemon.experience}
{self.current_pokemon.name}'s Level: {self.current_pokemon.level}
"""

        elif self.current_pokemon.pokemon_type == 'Electric' and other_trainer.current_pokemon.pokemon_type == 'Fire' or other_trainer.current_pokemon.pokemon_type == 'Water':
            other_trainer.current_pokemon.lose_health(self.current_pokemon.level * 2)
            if other_trainer.current_pokemon.current_health <= 0:
                other_trainer.current_pokemon.current_health = 0
                self.current_pokemon.level_up()
                self.current_pokemon.experience += 4
                return f"""
{self.name} damaged {other_trainer.name}'s current pokemon ({other_trainer.current_pokemon.name}) by {self.current_pokemon.level * 2}.
{other_trainer.current_pokemon.name}'s Current Health is {other_trainer.current_pokemon.current_health} HP.
{self.current_pokemon.name}'s Experience: {self.current_pokemon.experience}
{self.current_pokemon.name}'s Level: {self.current_pokemon.level}
            """

            self.current_pokemon.level_up()
            self.current_pokemon.experience += 4

            return f"""
{self.name} damaged {other_trainer.name}'s current pokemon ({other_trainer.current_pokemon.name}) by {self.current_pokemon.level * 2}.
{other_trainer.current_pokemon.name}'s Current Health is {other_trainer.current_pokemon.current_health} HP.
{self.current_pokemon.name}'s Experience: {self.current_pokemon.experience}
{self.current_pokemon.name}'s Level: {self.current_pokemon.level}          
            """


        elif self.current_pokemon.pokemon_type == 'Water' and other_trainer.current_pokemon.pokemon_type == 'Fire' or other_trainer.current_pokemon.pokemon_type == 'Water':
            other_trainer.current_pokemon.lose_health(self.current_pokemon.level / 2)
            if other_trainer.current_pokemon.current_health <= 0:
                other_trainer.current_pokemon.current_health = 0
                self.current_pokemon.level_up()
                self.current_pokemon.experience += 2
                return f"""
{self.name} damaged {other_trainer.name}'s current pokemon ({other_trainer.current_pokemon.name}) by {self.current_pokemon.level / 2}.
{other_trainer.current_pokemon.name}'s Current Health is {other_trainer.current_pokemon.current_health} HP.
{self.current_pokemon.name}'s Experience: {self.current_pokemon.experience}
{self.current_pokemon.name}'s Level: {self.current_pokemon.level}     
            """
            self.current_pokemon.level_up()
            self.current_pokemon.experience += 2

            return f"""
{self.name} damaged {other_trainer.name}'s current pokemon ({other_trainer.current_pokemon.name}) by {self.current_pokemon.level / 2}.
{other_trainer.current_pokemon.name}'s Current Health is {other_trainer.current_pokemon.current_health} HP.
{self.current_pokemon.name}'s Experience: {self.current_pokemon.experience}
{self.current_pokemon.name}'s Level: {self.current_pokemon.level}
            """

        elif self.current_pokemon.pokemon_type == 'Water' and other_trainer.current_pokemon.pokemon_type == 'Electric':
            other_trainer.current_pokemon.lose_health(self.current_pokemon.level * 2)
            if other_trainer.current_pokemon.current_health <= 0:
                other_trainer.current_pokemon.current_health = 0
                self.current_pokemon.level_up()
                if self.current_pokemon.experience + (self.current_pokemon.level * 2) >= 10:
                    self.current_pokemon.experience += (10 - self.current_pokemon.experience)
                    print(f"{self.current_pokemon.name} has leveled up!")

                else:
                    self.current_pokemon.experience += 4

                return f"""
{self.name} damaged {other_trainer.name}'s current pokemon ({other_trainer.current_pokemon.name}) by {self.current_pokemon.level * 2}.
{other_trainer.current_pokemon.name}'s Current Health is {other_trainer.current_pokemon.current_health} HP.
{self.current_pokemon.name}'s Experience: {self.current_pokemon.experience}
{self.current_pokemon.name}'s Level: {self.current_pokemon.level}
            """

            self.current_pokemon.level_up()
            if self.current_pokemon.experience + 4 >= 10:
                self.current_pokemon.experience += (10 - self.current_pokemon.experience)
                print(f"{self.current_pokemon.name} has leveled up!")
            else:
                self.current_pokemon.experience += 4

            return f"""
{self.name} damaged {other_trainer.name}'s current pokemon ({other_trainer.current_pokemon.name}) by {self.current_pokemon.level * 2}.
{other_trainer.current_pokemon.name}'s Current Health is {other_trainer.current_pokemon.current_health} HP.
{self.current_pokemon.name}'s Experience: {self.current_pokemon.experience}
{self.current_pokemon.name}'s Level: {self.current_pokemon.level}
            """

        elif self.current_pokemon.pokemon_type == 'Fire' and other_trainer.current_pokemon.pokemon_type == 'Fire':
            other_trainer.current_pokemon.lose_health(self.current_pokemon.level / 2)
            if other_trainer.current_pokemon.current_health <= 0:
                other_trainer.current_pokemon.current_health = 0
                self.current_pokemon.level_up()
                self.current_pokemon.experience += 2
                return f"""
{self.name} damaged {other_trainer.name}'s current pokemon ({other_trainer.current_pokemon.name}) by {self.current_pokemon.level / 2}.
{other_trainer.current_pokemon.name}'s Current Health is {other_trainer.current_pokemon.current_health} HP.
{self.current_pokemon.name}'s Experience: {self.current_pokemon.experience}
{self.current_pokemon.name}'s Level: {self.current_pokemon.level}
            """
            self.current_pokemon.level_up()
            self.current_pokemon.experience += 2

            return f"""
{self.name} damaged {other_trainer.name}'s current pokemon ({other_trainer.current_pokemon.name}) by {self.current_pokemon.level / 2}.
{other_trainer.current_pokemon.name}'s Current Health is {other_trainer.current_pokemon.current_health} HP.
{self.current_pokemon.name}'s Experience: {self.current_pokemon.experience}
{self.current_pokemon.name}'s Level: {self.current_pokemon.level}
            """


        elif self.current_pokemon.pokemon_type == 'Fire' and other_trainer.current_pokemon.pokemon_type == 'Water' or other_trainer.current_pokemon.pokemon_type == 'Electric':
            other_trainer.current_pokemon.lose_health(self.current_pokemon.level * 2)
            if other_trainer.current_pokemon.current_health <= 0:
                other_trainer.current_pokemon.current_health = 0
                self.current_pokemon.level_up()
                self.current_pokemon.experience += 4
                return f"""
{self.name} damaged {other_trainer.name}'s current pokemon ({other_trainer.current_pokemon.name}) by {self.current_pokemon.level * 2}.
{other_trainer.current_pokemon.name}'s Current Health is {other_trainer.current_pokemon.current_health} HP.
{self.current_pokemon.name}'s Experience: {self.current_pokemon.experience}
{self.current_pokemon.name}'s Level: {self.current_pokemon.level}
            """
            self.current_pokemon.level_up()
            self.current_pokemon.experience += 4

            return f"""
{self.name} damaged {other_trainer.name}'s current pokemon ({other_trainer.current_pokemon.name}) by {self.current_pokemon.level * 2}.
{other_trainer.current_pokemon.name}'s Current Health is {other_trainer.current_pokemon.current_health} HP.
{self.current_pokemon.name}'s Experience: {self.current_pokemon.experience}
{self.current_pokemon.name}'s Level: {self.current_pokemon.level}
            """

    def heal_current_pokemon(self, hp):
        if self.current_pokemon.current_health >= 100:
            return f"{self.current_pokemon.name}'s Health is full."
        elif (self.current_pokemon.current_health + hp) > 100:
            self.current_pokemon.current_health += 100 - self.current_pokemon.current_health
            return f"""{self.name} healed {self.current_pokemon.name} by {hp} HP.
{self.current_pokemon.name}'s Health is {self.current_pokemon.current_health} HP."""
        self.current_pokemon.current_health += hp
        return f"""
{self.name} healed {self.current_pokemon.name} by {hp} HP.
{self.current_pokemon.name}'s Current Health is {self.current_pokemon.current_health}
"""



    def __repr__(self):
        return f"""
           Name: {self.name}

           Num. of potions: {self.number_of_potions}

           Pokemons: {self.pokemons}

           Currently Active Pokemons: {len([self.current_pokemon])}

"""




pikachu = Pokemon("Pikachu", 4, 'Electric', 100, 100, False, 0)
arcanine = Pokemon("Arcanine", 6, 'Fire', 100, 100, False, 0)
slowpoke = Pokemon("Slowpoke", 3, 'Water', 100, 100, False, 0)
charizard = Pokemon("Charizard", 8, 'Fire', 100, 100, False, 0)
charmander = Pokemon("Charmander", 5, 'Fire', 100, 100, False, 0)
blastoise = Pokemon("Blastoise", 2, 'Water', 100, 100, False, 0)
squirtle = Pokemon("Squirtle", 1, 'Water', 100, 100, False, 0)
jolteon = Pokemon("Jolteon", 7, 'Electric', 100, 100, False, 0)
raichu = Pokemon("Raichu", 6, 'Electric', 100, 100, False, 0)


potion = ({'elixir': 20, 'cracker': 15, 'stone_of_eternity': 60})
elixir = 20
cracker = 15
stone_of_eternity = 60

#print(slowpoke.attack(pikachu))
#print(pikachu.attack(arcanine))
#print(arcanine.attack(pikachu))
#print(pikachu.attack(arcanine))

player1 = Trainer("Trainer 1", 5, [pikachu, slowpoke, blastoise], pikachu)
player2 = Trainer("Trainer 2", 3, [arcanine, jolteon, raichu], raichu)
player3 = Trainer("Trainer 3", 6, [squirtle, charizard, charmander], charizard)

#print(player3.attack(player1))
#print(player1.heal_current_pokemon(5))

print(player1.switch_pokemon(slowpoke))
print(raichu.attack(pikachu))
#print(pikachu.gain_health(1))
#print(pikachu.gain_health(3))
#print(pikachu.gain_health(1))
#print(player2.attack(player1))
#print(player1.heal_current_pokemon(15))
print(player1.attack(player2))
print(player1.attack(player2))
print(player1.attack(player2))
print(player1.attack(player2))
print(player1.attack(player2))
print(player1.attack(player2))
print(player1.attack(player2))
print(player1.attack(player2))
print(player1.attack(player2))
print(player1.attack(player2))
print(player1.attack(player2))
print(player1.attack(player2))
print(player1.attack(player2))
print(player1.attack(player2))
print(player1.attack(player2))
print(player1.attack(player2))
print(player1.attack(player3))
print(player1.attack(player3))
print(player1.attack(player3))
print(player1.attack(player3))
print(player1.attack(player3))
print(player1.attack(player3))






