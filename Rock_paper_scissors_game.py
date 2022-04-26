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
game=[rock,paper,scissors]
user_choice=int(input("What do you choose ? Type 0 for rock, 1 for paper or 2 for scissors : "))

if user_choice >2 or user_choice<0 :
    print("\nInvalid number. You lose !\n")
else :
    print(game[user_choice])

    computer_choice=random.randint(0,2)

    print("\nComputer choose :\n")

    print(game[computer_choice])

    if user_choice==0 and computer_choice==2  :
        print("\n\tYou win !\n")
    elif user_choice==2 and computer_choice==0 :
        print("\n\tYou lose !\n")
    elif user_choice < computer_choice :
        print("\n\tYou lose !\n")
    elif user_choice >  computer_choice :
        print("\n\tYou win !\n")
    elif user_choice==computer_choice :
        print("\n\tIt's a draw !\n")

