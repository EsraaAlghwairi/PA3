from game_character import GameCharacter
import random
# Warrior class (child) .
class Warrior(GameCharacter):
    # Call __init__() method for the Warrior object .
    def __init__(self, name, health, attack_max, magic):
         
        # Call super().__init__() function
        super().__init__(name, health, attack_max, magic)
        
        #instance attributes
        self.popularity=0
        print(f"{self.name} is ready to fight! \n")

    def buy_armor(self,gold,member,shield_value=0.0) :
       self.gold_value=gold
       self.member=member  
       self.sheild_value=0.0
       self.member=str(input("please choose the name of the character which you want yo purchase a shield"))    
       self.gold=int(input("pleas Enter the amount of gold you would use to prchase the shield"))
       print(f"The worrior orders to buy a shield for the member '{self.member}' by amount '{self.gold_value}' gold coins")

       shield_value=int(random.random(0.00,0.20))
       member.health+=shield_value
       self.popularity+=shield_value
       self.gold-=self.gold_value

    def share_intelligence(self,obj) :
        obj.foresight+=self.popularity*0.1
