from board import Board
from scoreboard import Scoreboard
from random import choice as randch

def start_game(self):
        while self.take_turn():
            pass 

def main():
    hidden_board = Board(True)
    board = Board(False)
    ship_place_amount = 5
    # Randomly place ships
    ship_sizes_list = [2, 3, 3, 4, 5]
    for _ in range(ship_place_amount):
        board.place_ship(randch(ship_sizes_list))
    
    hidden_board.drawmap()

    game = Scoreboard()
    game.start_game()


if __name__ == "__main__":
    main()

    # hiddenboard = board(True)
    # hiddenboard.drawmap()

    # visibleboard = board(False)
    # visibleboard.drawmap()