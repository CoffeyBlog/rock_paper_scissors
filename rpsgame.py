import random


def main():
    show_header()

    player = "You"
    ai = "Computer"

    play_game(player, ai)


def show_header():
    print("-------------------------------------------")
    print("----- Rock Paper Scissors Version One -----")
    print("-------------------------------------------")


def play_game(player_one, player_two):
    rounds = 3
    wins_p1 = 0
    wins_p2 = 0

    rolls = ['rock', 'paper', 'scissors']

    while wins_p1 < rounds and wins_p2 < rounds:
        roll1 = get_roll(player_one, rolls)
        roll2 = random.choice(rolls)

    if not roll1:
        print("Can't play that - exiting")
        return

    print(f"{player_one} rolls {roll1}")
    print(f"{player_two} rolls {roll2}")

    winner = check_for_winning_throw(player_one, player_two, roll1, roll2)

    if winner is None:
        print("This round was a tie")
    else:
        print(f'{winner} takes this round')
        if winner == player_one:
            wins_p1 += 1
        elif winner == player_two:
            wins_p2 += 1


    if wins_p1 >= rounds:
        overall_winner = player_one
    else:
        overall_winner = player_one

    print(f"{overall_winner} wins")


def check_for_winning_throw(player_one, player_two, roll1, roll2):
    # Test for a Winner
    winner = None
    if roll1 == roll2:
        print("Tie Game!")
    elif roll1 == 'rock':
        if roll2 == 'paper':
            winner = player_two
        elif roll2 == 'scissors':
            winner = player_one

    elif roll1 == 'paper':
        if roll2 == 'scissors':
            winner = player_two
        elif roll2 == 'rock':
            winner = player_one

    elif roll1 == 'scissors':
        if roll2 == 'rock':
            winner = player_two
        elif roll2 == 'paper':
            winner = player_one
    print("The game is over!")
    if winner is None:
        print("It was a tie")
    else:
        print(f'{winner} takes the game')


def get_roll(player_name, rolls):
    roll = input(f"{player_name}, what is your roll? [rock, paper, scissors]: ")
    roll = roll.lower().strip()
    if roll not in rolls:
        print(f"Sorry {player_name}, {roll} is not a valid play!")
        return None

    return roll


if __name__ == '__main__':
    main()
