import random
from ship import Ship

EMPTY_SYMBOL = "🌊"  # Water
SHIP_SYMBOL = "🚢"  # ship
HIT_SYMBOL = "💥" # explosion
HIDDEN_SYMBOL = "◼️ " # cover

class Board:

    ships = []

    def __init__(self, is_hidden):
        self.size = 10
        self.hidden = is_hidden
        self.map = [["" for _ in range(self.size)] for _ in range(self.size)]
        self.ships = []

        for i in range(0,len(self.map)):
            for j in range(0, len(self.map)):
                if is_hidden == False: # if not hidden
                    self.map[i][j] = "🌊 "
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
            if all(0 <= pos[0] < self.size and 0 <= pos[1] < self.size for pos in new_ship.ship_object.positions): 
                if all(self.map[pos[0]][pos[1]] == EMPTY_SYMBOL for pos in new_ship.ship_object.positions):
                    for posi in new_ship.ship_object.positions:
                        self.map[posi[0]][posi[1]] = SHIP_SYMBOL
                    self.ships.append(new_ship)
                    break


    def hit(self, x, y):
        if 0 <= x < self.size and 0 <= y < self.size:
            if self.map[x][y] == SHIP_SYMBOL:
                self.map[x][y] = HIT_SYMBOL
                return True
        return False
    
