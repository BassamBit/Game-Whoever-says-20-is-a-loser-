# computer plying
def Computer(CNum):
    # List of numbers that lead to losing the game
    loser_numbers = [20, 17, 14, 11, 8, 5, 2]

    if CNum in loser_numbers:
        return CNum + 2
    else:
        return CNum + 1


# player plying
def player(PNum):
    while True:
        new_number = int(input("your tern: "))

        # The player has two options to add 2 or 1 to the last number
        if new_number in {PNum + 1, PNum + 2}:
            return new_number
        print("Sorry, wrong number.")


# Use "while loops" to create a loop to run the game multiple times
repeat = 'yes'
while repeat.lower() == 'yes':
    num = 0

    # The game ends when either player reaches the number 20
    while num < 20:
        # Computer turn
        num = Computer(num)
        print(f"computer: {num}")

        # Player's turn
        num = player(num)

    repeat = input("Do you want to play again? (yes,no):")
    print("_" * 20)
