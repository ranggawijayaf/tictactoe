import random

class Move:
    def __init__(self, position, marker):
        self.position = position
        self.marker = marker

class Player:
    def __init__(self, name, marker, is_human=True):
        self.name = name
        self.marker = marker
        self.is_human = is_human

    def make_move(self, board):
        if self.is_human:
            while True:
                try:
                    position = int(input("Please enter your move (1-9): "))
                    if position < 1 or position > 9:
                        print("❌ Position must be between 1 and 9.")
                    elif not board.is_position_free(position):
                        print("❌ That position is already taken. You lose your turn!")
                        return None
                    else:
                        return Move(position, self.marker)
                except ValueError:
                    print("❌ Invalid input. Please enter a number between 1 and 9.")
        else:
            available_positions = board.get_free_positions()
            if available_positions:
                position = random.choice(available_positions)
                print(f"{self.name} chooses position {position}")
                return Move(position, self.marker)
            else:
                return None

class Board:
    def __init__(self):
        self.cells = [' '] * 9

    def display_positions(self):
        print("Positions:")
        for i in range(0, 9, 3):
            print(f"| {i+1} | {i+2} | {i+3} |")

    def display(self):
        print("Board:")
        for i in range(0, 9, 3):
            print(f"| {self.cells[i]} | {self.cells[i+1]} | {self.cells[i+2]} |")
        print()

    def update(self, move):
        self.cells[move.position - 1] = move.marker

    def is_position_free(self, position):
        return self.cells[position - 1] == ' '

    def get_free_positions(self):
        return [i+1 for i in range(9) if self.cells[i] == ' ']

    def check_winner(self, marker):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        return any(all(self.cells[i] == marker for i in pattern) for pattern in win_patterns)

    def is_full(self):
        return all(cell != ' ' for cell in self.cells)

def play_tic_tac_toe():
    print("**************************")
    print("  Welcome to Tic-Tac-Toe  ")
    print("**************************\n")

    human = Player(name="You", marker='X', is_human=True)
    computer = Player(name="Computer", marker='O', is_human=False)

    while True:
        board = Board()
        board.display_positions()
        board.display()
        current_player = human
        game_over = False

        while not game_over:
            move = current_player.make_move(board)
            if move:
                board.update(move)
            else:
                print(f"{current_player.name} loses the turn.")
            board.display()

            if move and board.check_winner(current_player.marker):
                print(f"🏆 {current_player.name} wins the game!")
                game_over = True
                break

            if board.is_full():
                print("🤝 It's a tie!")
                game_over = True
                break

            current_player = computer if current_player == human else human

        replay = input("Would you like to play again? (y/n): ").lower()
        if replay != 'y':
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
