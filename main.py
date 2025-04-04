from board import Board
from scoreboard import Scoreboard
from random import choice as randch



def main():
    #game = Scoreboard()
    #game.start_game()
    #hidden_board1 = Board(True)
    board1 = Board(False)
    
    hidden_board2 = Board(True)
    board2 = Board(False)


    ship_place_amount = 5
    # Randomly place ships
    ship_sizes_list = [2, 3, 3, 4, 5]
    for _ in range(ship_place_amount):
        board1.place_ship(randch(ship_sizes_list))
    
    hidden_board2.drawmap()
    board1.drawmap()

    game = Scoreboard()
    game.start_game()


if __name__ == "__main__":
    main()

    hiddenboard = Board(True)
    hiddenboard.drawmap()

    visibleboard = Board(False)
    visibleboard.drawmap()