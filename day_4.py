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
images=[rock,paper,scissors]

user_input=int(input("Enter 0 for rock, 1 for paper and 2 for scissors\n"))

if user_input>=0 and user_input<=2:
    print(images[user_input])


computer_choice=random.randint(0,2)
print(images[computer_choice])

if user_input>=3 or user_input<0:
    print("You typed wrong input.You loose")

elif user_input == 0 and computer_choice == 2:
    print("You win!")

elif computer_choice == 0 and user_input == 2:
    print("You loose!")

elif user_input> computer_choice:
    print("You win")
elif computer_choice>user_input:
    print("You loose")

elif computer_choice==user_input:
    print("It's a draw")


