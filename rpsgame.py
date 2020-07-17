print("-------------------------------------------")
print("----- Rock Paper Scissors Version One -----")
print("-------------------------------------------")


player_one = input("Enter player one's name:  ")
player_two = input("Enter player two's name:  ")

rolls = ['rock', 'paper', 'scissors']

roll1 = input(f"{player_one}, what is your roll? [rock, paper, scissors]: ")
roll1 = roll1.lower().strip()
if roll1 not in rolls:
    print(f"Sorry {player_one}, {roll1} is not a valid play")

roll2 = input(f"{player_two}, what is your roll? [rock, paper, scissors]: ")
roll2 = roll2.lower().strip()
if roll2 not in rolls:
    print(f"Sorry {player_two}, {roll2} is not a valid play")

print(f"{player_one} rolls {roll1}")
print(f"{player_two} rolls {roll2}")

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