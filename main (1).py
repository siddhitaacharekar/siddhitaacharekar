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


#Write your code below this line 👇
def a():
    import random
    Image = [rock, paper, scissors]
    user = int(
        input(
            "What do you chose ?Type 0 for rock or 1 for paper or 2 for scissors.\n"
        ))
    print(Image[user])
    computer = random.randint(0, 2)
    print(f"Computer chose:{computer}")
    print(Image[computer])

    if user >= 3 or user < 0:
        print("You chose an invalid number!!")
    elif user == 0 and computer == 2:
        print("You win!!!")
    elif computer == 0 and user == 2:
        print("You lose!!!")
    elif computer > user:
        print("You win!!!")
    elif user == computer:
        print("It is  a draw!!!")


q = 6
while q > 0:
    q -= 1
    a()
