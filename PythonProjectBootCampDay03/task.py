print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
user_option1 = input('You\'re at a cross road. '
                     'Where do you want to go?\n \t type "left" or "right"\n').lower()
if user_option1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    user_option2 =input('Type\' "wait" to wait for a boat. '
                        'Type "swim" to swim a cross.\n').lower()
    if user_option2 == "wait":
        print("You arrive at the island unharmed.")
        user_option3 =input("There is a house with 3 doors. "
                            "One red, One yellow and One blue. "
                            "Which colour do you choose?\n").lower()
        if user_option3 == "yellow":
            print('Congratulation \'you find a "Treasure".')
        elif user_option3 == "red" or user_option3 == "blue":
            print('You\'re eaten by beast. "Game Over".')
        else:
            print('You\'re trap in house. "Game Over".')
    else:
        print('Attacked \'by trout. "Game Over".')
else:
    print('Fall \'into a hole. "Game Over".')