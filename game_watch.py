from game_character import GameCharacter
from explorer import Explorer
from medic import Medic
from warrior import Warrior

def control_panel(self) :

    print("A new Bot game has been started .")

    
    e1=Explorer("explorer1",100,100,100)
    m1=Medic("medic1",100,100,100)
    w1=Warrior("warrior1",100,100,100)
    group1=[w1,m1,e1]

    e2=Explorer("explorer2",100,100,100)
    m2=Medic("medic2",100,100,100)
    w2=Warrior("warrior2",100,100,100)
    group2=[w2,m2,e2]
    
    
  
    round=1
    round_ask=bool(input("Team'1' , Would you like to start a new round/True or False ? "))
    while round == 1 :
       print(f">>>round  {round} ") 
       round+=1

       if round ==2 :
           round_ask=False
           print("you finished each rounds ")

       for l,v in enumerate(group1):
            print(f"{l} -- {v.get_name()}")
       choose=int(input("Team'1',which character do you wish to choose for this round : "))
       print(f"you have choosen {group1[choose].get_name()} to play this round .")
       
       if(isinstance(group1[choose], Warrior)) :
           print(group1[choose])
           print(f"{group1[choose]} can do the following : ")
           print("""\n\t0 -  attack - attacks an openent character 
                    \n\t1 -  cas spell - casts a spell on any openent character
                    \n\t2 -  buy armor -buy armor for a member of the team
                    \n\t3 -  share intelligence  - share intelligence with explorer""")

           choose_move =int(input("choose movment : "))
               
           for l,v in enumerate(group2):
               print(f"{l} -- {v.get_name()}")
           
           if choose_move ==0 :
               print(f"which opponent do you wish to attack")
               choose_opponent=int(input("choose opponent : "))
               w1.attack(group2[choose_opponent])
           elif choose_move ==1 :
               print(f"which opponent do you wish to attack")
               choose_opponent=int(input("choose opponent : "))
               w1.cast_spell_on(group2[choose_opponent])
           elif choose_move == 2 :
               print(f"choose member of your team")
               choose_opponent=int(input("choose member : "))
               w1.buy_armor(w1.gold,group1[choose_opponent])
           elif choose_move == 3 :
               print("you will share your intelligence with your team explorer")
               w1.share_intelligence(group1[choose_opponent])
        #    elif choose_move >= 4 :
        #        print(f"{choose_move} is not existing number ")
           print(group1[choose])
            
            
       if(isinstance(group1[choose], Medic)) :
           print(group1[choose])
           print(f"{group1[choose]} can do the following : ")
           print("""\n\t0 -  attack - heal character of your team 
                    \n\t1 -  back to the future """)
           choose_move =int(input("choose movment : "))
           print(f"which opponent do you wish to attack")    
           for l,v in enumerate(group2):
               print(f"{l} -- {v.get_name()}
           choose_opponent=int(input("choose opponent : "))
           if choose_move ==0 :
               m1.attack(group2[choose_opponent])
           elif choose_move ==1 :
               m1.back_to_the_future()
           print(group1[choose])     

       if(isinstance(group1[choose], Explorer)) :
           print(group1[choose])
           print(f"{group1[choose]} can do the following : ")
           print("""\n\t0 -  attack - heal an enemy character 
                    \n\t1 -  go on quest  """) 

           choose_move =int(input("choose movment : "))
           
           print(group1[choose])

    ###########

    
    round_ask=bool(input("Team'2' , Would you like to start a new round/True or False ? "))
    while round_ask :
       print(f">>>round  {round} ") 
       

       if round ==0 :
           round_ask=False
           print("you finished each rounds ")

       for l,v in enumerate(group2):
            print(f"{l} -- {v.get_name()}")
       choose=int(input("Team'2',which character do you wish to choose for this round : "))
       print(f"you have choosen {group1[choose].get_name()} to play this round .")
       
       if(isinstance(group2[choose], Warrior)) :
           print(group2[choose])
           print(f"{group2[choose]} can do the following : ")
           print("""\n\t0 -  attack - attacks an enemy character 
                    \n\t1 -  cas spell - casts a spell on any enemy character
                    \n\t2 -  buy armor -buy armor for a member of the team
                    \n\t3 -  share intelligence  - share intelligence with explorer""")

           choose_move =int(input("choose movment : "))
           print(f"which opponent do you wish to attack")    
           for l,v in enumerate(group1):
               print(f"{l} -- {v.get_name()}")
           choose_opponent=int(input("choose opponent : "))
           if choose_move ==0 :
               w1.attack(group1[choose_opponent])
           elif choose_move ==1 :
               w1.cast_spell_on(group1[choose_opponent])
           elif choose_move == 2 :
               w1.buy_armor(w1.gold,group2[choose_opponent])
           elif choose_move == 3 :
               w1.share_intelligence(group2[choose_opponent])
           print(group2[choose])
            
            
       if(isinstance(group2[choose], Medic)) :
           print(group2[choose])
           print(f"{group2[choose]} can do the following : ")
           print("""\n\t0 -  attack - heal an enemy character 
                    \n\t1 -  back to the future """)
           choose_move =int(input("choose movment : "))
           print(f"which opponent do you wish to attack")    
           for l,v in enumerate(group1):
               print(f"{l} -- {v.get_name()}")
           choose_opponent=int(input("choose opponent : "))
           if choose_move ==0 :
               m1.attack(group1[choose_opponent])
           elif choose_move ==1 :
               m1.back_to_the_future()
           print(group2[choose])     

       if(isinstance(group2[choose], Explorer)) :
           print(group2[choose])
           print(f"{group2[choose]} can do the following : ")
           print("""\n\t0 -  attack - heal an enemy character 
                    1 -  go on quest  """) 

       choose_move =int(input("choose movment : "))
       print(f"which opponent do you wish to attack")    
       for l,v in enumerate(group1):
           print(f"{l} -- {v.get_name()}")
       choose_opponent=int(input("choose opponent : "))
       print(group2[choose])
       round+=1    
        
    

  
control_panel("self")


     
