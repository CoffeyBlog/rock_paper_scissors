import random

rolls = {
    'rock': {
        'defeats': ['scissors'],
        'defeated_by': ['paper'],
    },
    'paper': {
        'defeats': ['rock'],
        'defeated_by': ['scissors'],
    },
    'scissors': {
        'defeats': ['paper'],
        'defeated_by': ['rock'],
    },
}


def main():
    show_header()
    play_game("You", "Computer")


def show_header():
    print("-------------------------------------------")
    print("----- Rock Paper Scissors Version One -----")
    print("-------------------------------------------")


def play_game(player_one, player_two):
    wins = {player_one: 0, player_two: 0}
    roll_names = list(rolls.keys())

    while not find_winner(wins, wins.keys()):
        roll1 = get_roll(player_one, roll_names)
        roll2 = random.choice(roll_names)

        if not roll1:
            print("Try again")
            continue

        print(f"{player_one} roll {roll1}")
        print(f"{player_two} rolls {roll2}")

        winner = check_for_winning_throw(player_one, player_two, roll1, roll2)

        if winner is None:
            print("This round was a tie")
        else:
            print(f'{winner} takes this round')
            wins[winner] += 1

        print(f"Score is {player_one}: {wins[player_one]} and {player_two}: {wins[player_two]} ")
        print()

    overall_winner = find_winner(wins,wins.keys())
    print(f"{overall_winner} wins tha game!")


def find_winner(wins, names):
    best_of = 3
    for name in names:
        if wins.get(name, 0) >= best_of:
            return name

    return None


def check_for_winning_throw(player_one, player_two, roll1, roll2):
    winner = None
    if roll1 == roll2:
        print("Tie Game!")

    outcome = rolls.get(roll1, {})
    if roll2 in outcome.get('defeats'):
        return player_one
    elif roll2 in outcome.get('defeated_by'):
        return player_two

    return winner


def get_roll(player_name, roll_names):
    print("Available rolls:  ")
    for index, r in enumerate(roll_names, start=1):
        print(f"{index}. {r}")

    text = input(f"{player_name}, what is your roll? : ")
    selected_index = int(text) - 1

    if selected_index < 0 or selected_index >= len(rolls):
        print(f"Sorry {player_name}, {text} is not a valid play!")
        return None

    return rolls_names[selected_index]


if __name__ == '__main__':
    main()
