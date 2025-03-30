import random
user_wins=0
computer_wins=0
stop=False
while stop==False:
  user_choice= input("Enter your choice (Rock/Paper/Scissors/Quit): ").lower
  if user_choice=="quit":
    stop=True
  elif user_choice in ["rock", "paper", "scissors"]:
    choice_number = random.randint(0,2)
    if choice_number==0:
      comp_choice="rock"
    elif choice_number==1:
      comp_choice="paper"
    else:
      comp_choice="scissors"
  else:
    "Please enter a valid option"
    continue
  if user_choice==comp_choice:
    print("tie")
  elif user_choice=="rock" and comp_choice=="scissors":
    print("you win")
    user_wins += 1
  elif user_choice=="paper" and comp_choice=="rock":
    print("you win")
    user_wins += 1
  elif user_choice=="scissors" and comp_choice=="paper":
    print("you win")
    user_wins += 1
  elif user_choice=="rock" and comp_choice=="paper":
    print("I win")
    computer_wins += 1
  elif user_choice=="paper" and comp_choice=="scissors":
    print("I win")
    computer_wins += 1
  elif user_choice=="scissors" and comp_choice=="rock":
    print("I win")
    computer_wins += 1
print("number of computer wins:", computer_wins)
print("number of your wins:", user_wins)
