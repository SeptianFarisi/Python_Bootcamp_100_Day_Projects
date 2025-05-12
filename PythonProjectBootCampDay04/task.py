import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [scissors, rock, paper]
print("Type 0 for Scissor, 1 for Rock and 2 for Paper")
comp = random.randint(0,2)
user_input = int(input("what do you choose? "))
print("Player choice")
if user_input == 0:
    print(game[0])
elif user_input == 1:
    print(game[1])
elif user_input == 2:
    print(game[2])
else:
    print("choose the number")

print("Computer choice")
print(game[comp])

if user_input == 0 and comp == 1:
    print("Computer win")
elif user_input == 0 and comp == 2:
    print("You win")
elif user_input == 1 and comp == 0:
    print("You win")
elif user_input == 1 and comp == 2:
    print("Computer win")
elif user_input == 2 and comp == 1:
    print("You win")
elif user_input == 2 and comp == 0:
    print("Computer win")
elif user_input == comp:
    print("Draw")