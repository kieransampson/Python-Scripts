import sys

class Player(object):

    def __init__(self, input_name):
        self.score = 0
        self.name = input_name
        self.choice = None

def start_game(p1, p2):

    winning_hands = {'rock': {'paper':'loss', 'scissors':'win'}, 'paper': {'scissors':'loss', 'paper':'win'}, 'scissors': {'rock':'loss', 'paper':'win'}}

    # start message
    if p1.score + p2.score == 0:
        print('\nOK, {} and {}, let\'s play Rock, Paper, Scissors!'.format(player1.name, player2.name))
    else:
        print('\nOK, {} and {}, next round!'.format(player1.name, player2.name))

    input_choices(p1, p2)

    draw_str = '\nIt\'s a draw! Both players chose {}!'

    if p1.choice == p2.choice:
        outcome = 'draw'
        print(draw_str)
        continue_game(p1, p2)

    else:
        outcome = winning_hands[player1.choice][player2.choice]

    if outcome == 'win':
        print("\nPlayer 1 wins!")
        player1.score += 1

    else:
        print('\nPlayer 2 wins!')
        player2.score += 1

    continue_game(p1, p2)


def input_choices(p1, p2):

    p1.choice = input('\n' + p1.name + ", Rock, Paper or Scissors? ").lower()
    while p1.choice not in ["rock", "paper", "scissors"]:
        p1.choice = input("Not a valid answer, try again: ")

    p2.choice = input('\n' + p2.name + ", Rock, Paper or Scissors? ").lower()
    while p2.choice not in ["rock", "paper", "scissors"]:
        p2.choice = input("Not a valid answer, try again: ")


def continue_game(p1, p2):

    score_str = '\nCurrent score is...\n  {}: {} \n  {}: {}'.format(p1.name, p1.score, p2.name, p2.score)
    print(score_str)
    decision = input('\nPlay again? ')

    if decision[:1].lower() == 'y':
                start_game(player1, player2)
    else:
        print("OK, thanks for playing!")
        sys.exit()


def name_chooser(placeholder_name):

    name_chooser_str = '\nHello {}, what is your name? '
    name_choice = input(name_chooser_str.format(placeholder_name))
    return name_choice



if __name__ == "__main__":

    # a = 1

    player1 = Player(name_chooser('Player 1'))
    player2 = Player(name_chooser('Player 2'))

    start_game(player1, player2)