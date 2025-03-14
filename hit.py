import random

EMPTY_SYMBOL = "🌊"  # Water
SHIP_SYMBOL = "🚢"  # ship
HIT_SYMBOL = "💥" # explosion
MISS_SYMBOL = "❌" # miss

class ship:

    def __init__(self, size, rotation, x, y):
        self.size = size
        self.x = x
        self.y = y

    def hit(self):
        # if in x,y area of ship then return true


class board:
    map = []
    hidden_map = []
    size = 10

    def __init__(self):
        for i in range(self.size):
            self.map.append([])
            for j in range(self.size):
                self.map[i].append(EMPTY_SYMBOL)
        for i in range(self.size):
            self.hidden_map.append([])
            for j in range(self.size):
                self.hidden_map[i].append(EMPTY_SYMBOL)

    def place_ship(self, ship_size):
        """Randomly places a ship on the map."""
        while True:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if self.map[x][y] == EMPTY_SYMBOL:  # Ensure ship isn't placed on another
                self.map[x][y] = SHIP_SYMBOL
                break

    def hit(self,x,y):
        if x > 9 or x < 0 or y > 9 or y < 0:
            print("Coordinates out of range")
            return None
        
        if (self.map[x][y] == SHIP_SYMBOL) :
            
            self.map[x][y] = HIT_SYMBOL

            return True
        else: 
            return False
        
    def printMap(self):
        for i in range(len(self.map)):
            print(self.map[i])
    

board1 = board()

for i in range(3):
    board1.place_ship(1)
    board1.place_ship(2)
    board1.place_ship(3)


board1.printMap()
        