import random

def get_choices():
  options=["rock","paper","scissors"]
  while True:
    try:
      player_choice=input("Enter a choice(Rock, Paper or Scissors):").lower()
      if player_choice not in options:
        print("\nEnter the valid options\n")
        continue
      else:
        break
    except:
      print("Invadil options\n")
  computer_choice=random.choice(options)
  choices={"player":player_choice,"computer":computer_choice}
  return choices

def check_win(player,computer):
    print(f"You chose {player},computer chose {computer}")
    if player==computer:
      return ("It's a tie!")
    elif player=="rock":
      if computer=="scissors":
        return ("Rock smashes the scissors, You win!")
      else:
        return ("Paper covers the rock,You lose.")
    elif player=="paper":
      if computer=="rock":
        return ("Paper covers the rock, You win!")
      else:
        return ("Scissors cut the paper, You lose")
    elif player=="scissors":
      if computer=="rock":
        return ("Rock smashes the scissors, You lose")
      else:
        return ("Scissors cut the paper, You win!")


def play():
  choices=get_choices()
  result=check_win(choices["player"].lower(),choices["computer"].lower()) 
  print(result)
  game_loop()

def game_loop():
  while True:
    try:
      again = input("Do you want to play againg(y/n)").lower()
      if again not in ['y','n']:
        print("\nEnter the valid options!\n")
        continue
      else:
        break
    except:
      print("Invalid option!\n")
  if again == 'y':
      play()
  else:
    print("Thanks for playing")
    
play()


      
    
  
    



