import random
choice=random.randint(1,100)

def user_input():
  while True:
    try:
      player_guess =int(input("Enter the number in between 1 to 100:"))
      if player_guess <1 or player_guess >100:
        print("Enter number in between 1 to 100:")
        continue
      else:
        return player_guess
    except:
      print("Enter valid number in between 1 to 100:")


count=0
while True:
  player_guess = user_input()
  count+=1
  if choice > player_guess:
    print("Too Low!")
    continue
  elif choice < player_guess:
    print("Too high")
    continue
  elif choice == player_guess:
    print(f"Congratulations! you gused the number in {count} attempts")
    break
