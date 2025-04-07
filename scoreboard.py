from board import Board
import random

class Scoreboard:
    def __init__(self):
        self.p1Score = 0
        self.p2Score = 0
        self.ships = {"Player 1": 5, "Player 2": 5}
        self.current_turn = "Player 1"

    def printScores(self):
        print("Player 1 Score:", self.p1Score)
        print("Player 2 Score:", self.p2Score)

    def start_game(self, board1, hiddenb1, board2, hiddenb2):
        """Start the game and alternate turns between players."""
        while True:
            # Player 1's turn
            self.printScores()
            print("\nPlayer 1's Turn:")
            print("Player 1's Board:")
            board1.drawmap()
            print("\nPlayer 2's Hidden Board:")
            hiddenb2.drawmap()

            if not self.take_turn(board2, hiddenb2):
                print("Player 1 Wins!")
                break
            
            # Player 2's turn
            self.printScores()
            print("\nPlayer 2's Turn:")
            print("Player 2's Board:")
            board2.drawmap()
            print("\nPlayer 1's Hidden Board:")
            hiddenb1.drawmap()

            if not self.take_turn(board1, hiddenb1):
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
            if self.current_turn == "Player 1":
                self.p1Score+=1 # player 1 score up 1
            else:
                self.p2Score+=1 # player 2 score up 1

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


