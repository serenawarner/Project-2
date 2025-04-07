import random
from ship import Ship

EMPTY_SYMBOL = "🌊"  # Water
SHIP_SYMBOL = "🚢"  # ship
HIT_SYMBOL = "💥" # explosion
HIDDEN_SYMBOL = "◼️ " # cover

class Board:

    ships = []

    size : int = 0
     
    map = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
           ]

    def __init__(self, h):
        self.size = len(self.map)
        
        for i in range(0,len(self.map)):
            for j in range(0, len(self.map)):
                if h == False: # if not hidden
                    self.map[i][j] = "🌊"
                else: # if
                    self.map[i][j] = "◼️ "
        
    def drawmap(self):
        for i in range(len(self.map)):
            printstring = ""
            for j in self.map[i]:
                printstring = printstring + j
            print(printstring)

    def place_ship(self, ship_size):
        """Randomly places a ship on the map."""
        while True:
            x, y = random.randint(0, len(self.map) - 1), random.randint(0, len(self.map) - 1)
            pos = [x,y]
            horizontal = random.choice([True, False]) # Randomized orientation boolean
            new_ship = Ship(ship_size, horizontal, x, y)

            # KHALIFF: Check if within x & y boundary, then For Loop to check for overlap
            if (0 <= pos[0] < self.size and 0 <= pos[1] < self.size for pos in new_ship.ship_object.positions): 
                if (self.map[pos[0]][pos[1]] == EMPTY_SYMBOL for pos in new_ship.ship_object.positions):
                    for posi in new_ship.ship_object.positions:
                        self.map[pos[0]][pos[1]] = SHIP_SYMBOL
                    self.ships.append(new_ship)
                    break

    def hit(self, x, y):
        if 0 <= x < self.size and 0 <= y < self.size:
            if self.map[x][y] == SHIP_SYMBOL:
                self.map[x][y] = HIT_SYMBOL
                return True
        return False
    
board1 = Board(False)
board1.drawmap()