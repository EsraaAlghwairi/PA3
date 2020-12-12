from game_character import GameCharacter
from datetime import datetime
import random

#Medic class (child) .
class Medic(GameCharacter):
    
    # Call __init__() method for the Medic object .
    def __init__(self, name, health, heal, magic ):
        
        # Call super().__init__() function
        super().__init__(name, health, heal, magic)

        #instance attributes
        self.nanobots=0
        self.nanobots_accuracy_level =0 
        print(f"Your medic {self.name}, to the rescue!")

    def heal(self, character):
        heal_value = (random.randrange(self.strength - 10 , self.strength + 10)/10)
        print(f"> {self.name} is healing {character.name}. {(heal_value)}")

        if character.get_health() + heal_value > character.max_health:
            character.set_health(100)
        else:
            character.set_health(character.get_health() + heal_value)
        
        return heal_value
    
    def attack(self, character):
        self.heal(character)
    
    def back_to_the_future(self) :
        present=datetime.now()
        future=datetime(2030, 8, 24)
        time_diff=present.microsecond-future.microsecond

        self.nanobots=self.nanobots+time_diff
        self.nanobots_accuracy_level=self.nanobots_accuracy_level+1
        return f"the number of new nanobots= {self.nanobots} "
   

 





 





