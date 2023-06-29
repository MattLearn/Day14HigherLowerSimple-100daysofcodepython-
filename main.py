from game_data import data
from art import logo, vs
import random

score = 0
#determine how to randomly pick between the different options
def init_game():
  matching = True
  person1 = data[random.randint(0,len(data))].copy()
  #print (person1)
  person2 = data[random.randint(0,len(data))].copy()
  while(matching == True):
    if person2 == person1:
      person2 = data[random.randint(0,len(data))].copy()
    else:
      break
  return person1, person2

def display(nameA, nameB):
  print(f"{nameA['name']} - {nameA['description']}")
  print(vs)
  print(f"{nameB['name']} - {nameB['description']}")
  print(f"\n\nyour score is {score}")
  #print(nameB["name"])
  #print(nameB["description"])


#display one vs the other
def win_condition(guess, nameA, nameB):
  if nameA['follower_count'] > nameB['follower_count']:
    answer = 'a'
  else:
    answer = 'b'
  if guess == answer:
    print("That's Correct!")
    score+= 1
  else:
    print(f"Incorrect, it's {answer}")
  print(f"{nameA['name']} is a {nameA['description']} with {nameA['follower_count']} followers")
  print(f"{nameB['name']} is a {nameB['description']} with {nameB['follower_count']} followers ")

def play_loop():
  dict1, dict2 = init_game()
  print(logo)
  display(dict1, dict2)
  guess = input("Who has the higher score A or B: ").lower()
  win_condition(guess,dict1,dict2)

play = True
while (play):
  play_loop()
  print("Would you like to play again?")
  replay = input("Yes(y) or No(n)").lower()
  if replay == 'n':
    break