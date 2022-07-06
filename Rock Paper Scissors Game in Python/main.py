import random

l = ['Rock', 'Paper', 'Scissors']

player = False

while player == False:

    computer = random.choice(l)
    print('\n Choose anyone from here')
    ply = input('Rock Paper Scissors')

    print('Player chose :', ply)
    print('Computer chose :', computer)

    if computer == ply:
        print('Match is draw..........')
    else:
        if computer == 'Rock':
            if ply == 'Paper':
                print('Computer won the match')
            else:
                print('You lose')

        elif computer == 'Paper':
            if ply == 'Scissors':
                print('Player won the match')
            else:
                print('Computer won the match')
        elif computer == 'Scissors':
            if ply == 'Paper':
                print('Computer won the match')
            else:
                print('Player won the match')

    user = input('Do want to continue or not? Yes/No')
    if user.lower() != 'yes':
        break
