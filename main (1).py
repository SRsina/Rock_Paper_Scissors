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

Death = '''

               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
'''

gift = '''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''
#Write your code below this line 👇
import random
print("Welcome to My Rock, Paper, Scissors Game!")
print("To get started Berry in mind that Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.")
print("The folowing simbols represent the game:")
print("Rock is: " + rock)
print("Paper is: " + paper)
print("Scissors is: " + scissors)
times = int(input("How many times do you want to play? \n"))
user_score = 0
computer_score = 0
for i in range(times):
  answer = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")
  if answer == "0":
    print(rock)
    print("computer choses: ")
    computer = random.randint(0,2)
    if computer == 0:
      print(rock)
      print("It's a tie!")
    elif computer == 1:
      print(paper)
      print("Computers wins!")
      computer_score += 1
    else:
      print(scissors)
      print("Yay! You win!")
      user_score += 1
  elif answer == "1":
    print(paper)
    print("computer choses: ")
    computer = random.randint(0,2)
    if computer == 0:
      print(rock)
      print("Yay! You win!")
      user_score += 1
    elif computer == 1:
      print(paper)
      print("It's a tie!")
    else:
      print(scissors)
      print("Computers wins")
      computer_score += 1
  elif answer == "2":
    print(scissors)
    print("computer choses: ")
    computer = random.randint(0,2)
    if computer == 0:
      print(rock)
      print("Computers wins!")
      computer_score += 1
    elif computer == 1:
      print(paper)
      print("Yay! You win!")
      user_score += 1
    else:
      print(scissors)
      print("It's a tie!")
  else:
    print("You typed an invalid number, you lose!")
if computer_score > user_score:
  print("The final Winner is Computer!")
  print(Death)
elif computer_score < user_score:
  print("You! are The final Winner")
  print(gift)
else:
  print("It's a tie!")
  