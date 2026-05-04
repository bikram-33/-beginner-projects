import random
def get_choices():
  dice_choice = []
  choice = random.randint(1,6)
  dice_choice = {"choice":choice}
  return dice_choice

def Play():
  while True:
    games_to_play = input("Roll the dice? (Y/N):")
    if games_to_play in ['y','Y']:
      return game()
    elif games_to_play in ['n','N']:
      print("Thanks for playing.")
      break
    else:
      print("Invalid choice!")

def game():
  result = get_choices()
  print(result["choice"])
  return Play()

Play()




