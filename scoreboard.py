import random
from board import Board
import random

class Scoreboard:
    def __init__(self):
        self.ships = {"Player 1": 5, "Player 2": 5}
        self.current_turn = "Player 1"
        self.board1 = Board(False)  # Player 1's visible board
        self.hidden_board1 = Board(True)  # Player 1's hidden board
        self.board2 = Board(False)  # Player 2's visible board
        self.hidden_board2 = Board(True)  # Player 2's hidden board

    def start_game(self):
        """Start the game and alternate turns between players."""
        while True:
            # Player 1's turn
            print("\nPlayer 1's Turn:")
            print("Player 1's Board:")
            self.board1.drawmap()
            print("\nPlayer 2's Hidden Board:")
            self.hidden_board2.drawmap()

            if not self.take_turn(self.board2, self.hidden_board2):
                print("Player 1 Wins!")
                break

            # Player 2's turn
            print("\nPlayer 2's Turn:")
            print("Player 2's Board:")
            self.board2.drawmap()
            print("\nPlayer 1's Hidden Board:")
            self.hidden_board1.drawmap()

            if not self.take_turn(self.board1, self.hidden_board1):
                print("Player 2 Wins!")
                break

    def take_turn(self, opponent_board, opponent_hidden_board):
        opponent = self.get_opponent()

        print(f"\n{self.current_turn}'s turn! {opponent} has {self.ships[opponent]} ships left.")

        # Get attack coordinates from current player
        while True:
            try:
                x, y = map(int, input("Enter coordinates to attack (x y): ").split())
                if 0 <= x < 10 and 0 <= y < 10:
                    break
                else:
                    print("Invalid coordinates. Please enter values between 0 and 9.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")

        # Check if the current player hits a ship
        if opponent_board.hit(x, y):
            print(f"{self.current_turn} scored a HIT! {opponent} loses 1 ship.")
            self.ships[opponent] -= 1

            if self.ships[opponent] == 0:
                print(f"\n{self.current_turn} wins! {opponent} has lost all ships!")
                return False  
        else:
            print("Miss! No ship hit.")

        self.current_turn = opponent
        return True  

    def get_opponent(self):
        """Switches between the 2 players."""
        return "Player 1" if self.current_turn == "Player 2" else "Player 2"
