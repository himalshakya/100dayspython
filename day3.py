print('''
                             .I.
                            / : \\
                            |===|
                            >._.<
                        .=-<     >-=.
                       /.'`(`-+-')'`.\\
                     _/`.__/  :  \__.'\_
                    ( `._/\`. : .'/\_.' )
                     >-(_) \ `:' / (_)-<
                     | |  / \___/ \  | |
                     )^( | .' : `. | )^(
                    |  _\|`-._:_.-'| \  |
                    "-<\)| :  |  : |  "-"
                      (\\| : / \ : |
                        \\-:-| |-:-')
                         \\:_/ \_:_/
                         |\\_| |_:_|
                         (;\\/ \__;)
                         |: \\  | :|
                         \: /\\ \ :/
                         |==| \\|==|
                        /v-'(  \\`-v\\
                       // .-'   \\. \\
                       `-'       \\`-'
                                  \|

Welcome to Tresure Island.
Your mission is to find the treasure.
''')

direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")
if direction != "left":
  print("You fall into a hole. Game Over.")
else:
  direction = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
  if direction != "wait":
    print("You are attacked by a trout. Game Over.")
  else:
    direction = input("You arrive at the island unharmed. There is a house with 3 doors. One read, one yellow, and one blue. Which colour do you choose?\n")
    if direction == "blue":
      print("You enter a room of beasts. Game Over.")
    elif direction == "red":
      print("You are burned by fire. Game Over.")
    elif direction == "yellow":
      print("You Win! Game Over.")
    else:
      print("Game Over.")

