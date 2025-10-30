import getpass
import pwinput





def play_rps():
    player1 = pwinput.pwinput(prompt="Player 1❓❓❓ ",mask='⚪')  
    player2 = pwinput.pwinput(prompt="Player 2❓❓❓ ",mask='⚪')

    if (player1 == 'r' and player2 == 's'):
        print('😊Player 1 wins.😊   ⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅')
    elif (player1 == 's' and player2 == 'p'):
        print('😊Player 1 wins.😊   ⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅')
    elif (player1 == 'p' and player2 == 'r'):
        print('😊Player 1 wins.😊   ⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅')
    elif player1 == player2:
        print("It's a tie! 👍   ⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅")
    elif (player1 == 'r' and player2 == 'p'):
        print('😊Player 2 wins.😊   ⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅')
    elif (player1 == 's' and player2 == 'r'):
        print('😊Player 2 wins.😊   ⬅⬅⬅⬅⬅⬅⬅⬅⬅⬅')
    elif (player1 == 'p' and player2 == 's'):
        print('😊Player 2 wins.😊   ⬅⬅⬅⬅⬅⬅⬅⬅⬅')
            
    else:
        print('😔Please enter valid choice: r, p, or s😔')


answer="Y"
while answer == 'Y' or answer== 'y':
    play_rps()
    answer=input ('Would you like to play again?')


    


