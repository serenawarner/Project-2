from board import Board

class Scoreboard:
    def __init__(self):
        # Initialize players' ships count and  Player 1 as the starting player
        self.ships = {"Player 1": 5, "Player 2": 5}  
        self.current_turn = "Player 1"

    def take_turn(self):
        opponent = self.get_opponent()
        print(f"\n{self.current_turn}'s turn! {opponent} has {self.ships[opponent]} ships left.")

        # print maps here
        # Here we can get the input x,y coords to attack

        if random.choice(["hit", "miss"]) == "hit":
            print(f"{self.current_turn} scored a HIT! {opponent} loses 1 ship.")
            self.ships[opponent] -= 1

            
            if self.ships[opponent] == 0:
                print(f"\n{self.current_turn} wins! {opponent} has lost all ships!")
                return False  
        else:
            print("Miss! No ship hit.")

        # switching  to the opponent
        self.current_turn = opponent
        return True  

    def get_opponent(self):
        """Switches between the 2 players ."""
        return "Player 1" if self.current_turn == "Player 2" else "Player 2"

    def start_game(self):
        while self.take_turn():
            pass