import getpass
import pwinput
player1 = pwinput.pwinput(prompt="Player 1: rock, paper, or scissors? ",mask='*')  
player2 = pwinput.pwinput(prompt="Player 2: rock, paper, or scissors? ",mask='*')

if (player1 == 'r' and player2 == 's'):
    print('Player 1 wins.')
elif (player1 == 's' and player2 == 'p'):
    print('Player 1 wins.')
elif (player1 == 'p' and player2 == 'r'):
    print('Player 1 wins.')
elif player1 == player2:
    print("It's a tie!")
elif (player1 == 'r' and player2 == 'p'):
    print('Player 2 wins.')
elif (player1 == 's' and player2 == 'r'):
    print('Player 2 wins.')
elif (player1 == 'p' and player2 == 's'):
    print('Player 2 wins.')
        
else:
    print('Someone did not enter a valid choice. Please use "r", "p", or "s".')
