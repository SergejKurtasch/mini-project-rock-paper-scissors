import random
#computers_number = random.randint(1, 9)
#print("random:", number)


def computer_play() -> str:
    '''
    The function generates any random choice for the computer's turn and returns a letter r, p or s.
    '''
    n = random.randint(1, 3)
    if n == 1:
        y = "r"
    elif n == 2:
        y = "p"
    else:
        y = "s"
    return y


def rock_paper_scissors(x, y):

    '''
        The function takes two arguments, x and y, which are the choices of the player and the computer respectively. And returns the result of the game.
    '''
    if x == y:
        return "Odd"
    if x == "r" and y == "s":
        return "Player wins"
    if y == "r" and x == "s":
        return "Computer wins"
    if x == "r" and y == "p":
        return "Computer wins"
    if y == "r" and x == "p":
        return "Player wins"
    if x == "p" and y == "s":
        return "Computer wins"
    if y == "p" and x == "s":
        return "Player wins"



computer_score = 0
player_score = 0

x =input("Please enter r (for rock), p (for paper) or s (for scissor). Enter e for exit the game. Your choice: ")          # input by player


while x != "e":
      print('-------------------------------------------')
      if x == "r" or x == "p" or x == "s" or x == "e":

        y = computer_play()
        print("Player choice", x, end =' ')
        print("Computer choice", y)
        print()
        res = rock_paper_scissors(x, y)
        if res == "Player wins":
           player_score += 1
        elif res == "Computer wins":
            computer_score += 1

        print(res)
        print()
        print("Player score:", player_score)
        print("Computer score:", computer_score)


      else:
         print("Wrong entry")
      print('-------------------------------------------')
      x =input("Please enter r (for rock), p (for paper) or s (for scissor). Enter e for exit the game.")
print()
if computer_score > player_score:
    print("Game is finished. Total score is Computer score:", computer_score, ' Player score: ', player_score, "Computer wins!")
elif computer_score < player_score:
    print("Game is finished. Total score is Computer score:", computer_score, ' player score: ', player_score, "Player wins!")
else:
    print("Game is finished. Total score is Computer score:", computer_score, ' Player score: ', player_score, "Fun to fun, everyone is a winner!")
print()

                                                                            