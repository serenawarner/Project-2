import random
from ship import Ship

EMPTY_SYMBOL = "🌊"  # Water
SHIP_SYMBOL = "🚢"  # ship
HIT_SYMBOL = "💥" # explosion
HIDDEN_SYMBOL = "◼️ " # cover

class Board:
    size = 10
     
    map = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]

    def __init__(self, h):
        for i in range(0,len(self.map)):
            for j in range(0, len(self.map)):
                if h == False:
                    self.map[i][j] = "🌊"
                else:
                    self.map[i][j] = "◼️ "
        
    def draw_map(self):
        for i in range(len(self.map)):
            printstring = ""
            for j in self.map[i]:
                printstring = printstring + j
            print(printstring)

    def draw_hidden(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.map[i][j] == EMPTY_SYMBOL or self.map[i][j] == SHIP_SYMBOL:
                    print(HIDDEN_SYMBOL,end="")
                else:
                    print(HIT_SYMBOL,end="")
            print()

    def place_ship(self, ship_size):
        """Randomly places a ship on the map."""
        while True:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            horizontal = random.choice([True, False]) # Randomized orientation boolean
            new_ship = Ship(ship_size, horizontal, x, y)

            # KHALIFF: Check if within x & y boundary, then For Loop to check for overlap
            if (0 <= pos[0] < self.size and 0 <= pos[1] < self.size for pos in new_ship.ship_object.positions): 
                if (self.map[pos[0]][pos[1]] == EMPTY_SYMBOL for pos in new_ship.ship_object.positions):
                    for pos in new_ship.ship_object.positions:
                        self.map[pos[0]][pos[1]] = SHIP_SYMBOL
                    self.ships.append(new_ship)
                    break

    def hit(self, x, y):
        if 0 <= x < self.size and 0 <= y < self.size:
            if self.map[x][y] == SHIP_SYMBOL:
                self.map[x][y] = HIT_SYMBOL
                return True
        return False
