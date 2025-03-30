import random
user_wins=0
computer_wins=0
stop=False
while stop==False:
  user_input= input("Enter your choice (Rock/Paper/Scissors/Quit): ")
  user_choice=user_input.lower()
  choice_number = random.randint(0,2)
  if choice_number==0:
      comp_choice="rock"
  elif choice_number==1:
      comp_choice="paper"
  else:
      comp_choice="scissors"
  if user_choice=="rock" and comp_choice=="scissors":
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
  elif user_choice==comp_choice:
      print("tie")
  if user_choice=="quit":
    stop=True    
print("number of computer wins:", computer_wins)
print("number of your wins:", user_wins)
