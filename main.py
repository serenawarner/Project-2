from board import Board
from scoreboard import Scoreboard
from random import choice as randch



def main():
    game = Scoreboard()
    hiddenb1 = Board(True)
    board1 = Board(False)
    
    hiddenb2 = Board(True)
    board2 = Board(False)


    ship_place_amount = 5
    # Randomly place ships
    ship_sizes_list = [2, 3, 3, 4, 5]
    for _ in range(ship_place_amount):
        board1.place_ship(randch(ship_sizes_list))

    game.start_game(board1, hiddenb1, board2, hiddenb2)


if __name__ == "__main__":
    main()

    hiddenboard = Board(True)
    hiddenboard.drawmap()

    visibleboard = Board(False)
    visibleboard.drawmap()