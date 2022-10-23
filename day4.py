import random
from enum import Enum

class Choice(Enum):
  ROCK = 0
  PAPER = 1
  SCISSORS = 2

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

def did_player_win(choice, choice2):
  if (choice == Choice.SCISSORS and choice2 == Choice.PAPER):
    return True
  if (choice == Choice.PAPER and choice2 == Choice.ROCK):
    return True
  if (choice == Choice.ROCK and choice2 == Choice.SCISSORS):
    return True
  return False

def print_rps(choice):
  if choice == choice.ROCK:
    print(rock)
  if choice == choice.PAPER:
    print(paper)
  if choice == choice.SCISSORS:
    print(scissors)


if choice > 2:
  print("You lose, by default.")
else:
  computer_choice = random.randint(0,2)

  # Play ball
  choice_user = Choice(choice)
  print_rps(choice_user)
  print("Computer chose:\n")
  choice_comp = Choice(computer_choice)
  print_rps(choice_comp)

  did_player_win_contest = did_player_win(choice_user, choice_comp)
  if not did_player_win_contest:
    did_computer_win_contest = did_player_win(choice_comp, choice_user)
    if did_computer_win_contest:
      print(f"Computer won by {choice_comp.name} by going against {choice_user.name}")
    else:
      print(f"Draw as you chose {choice_user.name} by going against computer's choice {choice_comp.name}")
  else:
    print(f"You won by {choice_user.name} by going against computer's choice {choice_comp.name}")

