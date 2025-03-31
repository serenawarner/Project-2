from board import Board
from scoreboard import Scoreboard
from random import choice as randch

def main():
    board = Board()
    ship_place_amount = 5
    # Randomly place ships
    ship_sizes_list = [(1,2), (1,3), (1,3), (1,4), (1,5)]
    for _ in range(ship_place_amount):
        board.place_ship(randch(ship_sizes_list))
    
    board.draw_hidden()

    game = Scoreboard()
    game.start_game(board)


if __name__ == "__main__":
    main()

    # hiddenboard = board(True)
    # hiddenboard.drawmap()

    # visibleboard = board(False)
    # visibleboard.drawmap()