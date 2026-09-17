import random
from wordlist import words
hangman_art = {0: ("   ",
                    "   ",
                    "   "),
               1: (" O ",
                   "   ",
                   "   "),
               2: (" O ",
                   " | ",
                   "   "),
               3: (" O ",
                   "/| ",
                   "   "),
               4:(" O ",
                  "/|\\",
                  "   "),
               5:(" O ",
                  "/|\\",
                  "/  "),
               6:(" O ",
                  "/|\\",
                  "/ \\"),
}

def display_man(wrong_guess):
  print("*********")
  for lines in hangman_art[wrong_guess]:
    print(lines)
  print("*********")

def display_hint(hint):
  print()
  print(" ".join(hint))
  
def display_answer(answer):
  print()
  print(" ".join(answer))


def main():
  answer = random.choice(words)
  hint = ["_"] * len(answer)
  is_running = True
  wrong_guess = 0 
  guessed_letter = set()
  
  while is_running:
    
    display_man(wrong_guess)
    display_hint(hint)
    
    if wrong_guess >= 6:
        print("You lose!")
        print(f"Correct answer is {answer}")
        is_running = False
        continue
      
    if '_' not in hint:
              print("You win!")
              is_running = False
              continue
            
    user_gess = input("Enter a word:").lower()
    
    if user_gess in guessed_letter:
      print(f"{user_gess} is alredy guessed")
      continue
    guessed_letter.add(user_gess)
    
    if len(user_gess) != 1 or not user_gess.isalpha():
      print("Invalid input!")
      continue
    
    if user_gess in answer:
      for i in range(len(answer)):
        if answer[i] == user_gess:
          hint[i] = user_gess
    else:
      wrong_guess += 1
        

if __name__ == "__main__":
  main()