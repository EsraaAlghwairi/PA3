from game_character import GameCharacter
from csv import reader,writer
import random
#Explorer class (child) .
class Explorer(GameCharacter):
    # Call __init__() method for the Explorer object .
    def __init__(self, name, health, attack_max, magic):
        self.name=name
        self.health=health
        self.attack_max=attack_max
        self.magic=magic
        self.foresight=3

        # Call super().__init__() function
        super().__init__(name, health, attack_max, magic)
        
        print(f"Commander '{self.name}' at your service.")

    #go_on_quest method .
    def go_on_quest(self,map, position) :
       # Reading map.txt file
       # > Open map.txt file for reading
        fp= open("treasure_maps.csv")
        # cret a csv reader
        map_reader = reader(fp)
        map=int(round(random.random()))
        #count=0
        if map in map_reader :
          for record in map :
            position=int(round(random.random()))
            for i in (0,position):
              #cont+=1
              if i==position : 
               if record[i] == "X":
                 self.gold=self.gold
                 return self.gold
               elif record[i] == "$":
                 self.gold=self.gold + 1
                 return self.gold
      #super.foresight-=count  
        
           
         
          # > Close the file
      
        fp.close()
      