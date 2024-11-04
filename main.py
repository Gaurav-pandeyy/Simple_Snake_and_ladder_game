import random


class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, steps):
        self.position += steps
        if self.position > 100:
            self.position = 100  # Stay at 100 if the player overshoots
        return self.position


def roll_dice():
    return random.randint(1, 6)


def print_board(players):
    """Print the game board with player positions."""
    board = [' ' for _ in range(101)]  # Create an empty board of size 101 (0-100)

    # Mark player positions on the board
    for player in players:
        if player.position <= 100:  # Only show players who are on the board
            board[player.position] = player.name[0]  # Use first letter of player's name

    # Print the board
    print("\nBoard: ")
    for i in range(10, 0, -1):  # Print the board in rows
        row = ''
        for j in range(10):
            cell = (i - 1) * 10 + j
            if cell <= 100:
                row += f"[{board[cell]}]"  # Player markers
            else:
                row += "[ ]"  # Empty space
        print(row)
    print()


def main():
    print("Welcome to Snake and Ladder Game!")

    # Define the snakes and ladders on the board
    snakes_and_ladders = {
        3: 22,  # Ladder from 3 to 22
        5: 8,  # Ladder from 5 to 8
        11: 26,  # Ladder from 11 to 26
        20: 29,  # Ladder from 20 to 29
        17: 4,  # Snake from 17 to 4
        19: 7,  # Snake from 19 to 7
        21: 9,  # Snake from 21 to 9
        27: 1,  # Snake from 27 to 1
        39: 3,  # Snake from 39 to 3
        51: 19,  # Snake from 51 to 19
        54: 36,  # Snake from 54 to 36
        62: 43,  # Snake from 62 to 43
        64: 60,  # Snake from 64 to 60
        87: 24,  # Snake from 87 to 24
        93: 73,  # Snake from 93 to 73
        95: 75,  # Snake from 95 to 75
        98: 78  # Snake from 98 to 78
    }

    # Create players
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    players = [player1, player2]

    current_player_index = 0

    while True:
        current_player = players[current_player_index]

        input(f"{current_player.name}, press Enter to roll the dice...")
        dice_value = roll_dice()
        print(f"{current_player.name} rolled a {dice_value}!")

        new_position = current_player.move(dice_value)

        # Check for snakes or ladders
        if new_position in snakes_and_ladders:
            if new_position < snakes_and_ladders[new_position]:
                print(
                    f"Oh no! {current_player.name} encountered a snake and went down to {snakes_and_ladders[new_position]}!")
            else:
                print(f"Yay! {current_player.name} climbed a ladder to {snakes_and_ladders[new_position]}!")
            current_player.position = snakes_and_ladders[
                new_position]  # Update position according to snakes and ladders

        print(f"{current_player.name} is now on square {current_player.position}.")

        # Print the board after each turn
        print_board(players)

        # Check if the current player has won
        if current_player.position == 100:
            print(f"Congratulations! {current_player.name} wins!")
            break

        # Switch to the next player
        current_player_index = (current_player_index + 1) % len(players)


if __name__ == "__main__":
    main()
