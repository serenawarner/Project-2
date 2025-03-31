import random
from ship import Ship

EMPTY_SYMBOL = "🌊"  # Water
SHIP_SYMBOL = "🚢"  # ship
HIT_SYMBOL = "💥" # explosion
HIDDEN_SYMBOL = "◼️ "

# KHALIFF: Trying a new organization method...
# class shipSize:

#     def __init__(self, size, x, y, horizontal=True):
#         self.size = size # Number of grid spaces the ship takes up
#         self.x = x # Starting x coords
#         self.y = y # Starting y coords
#         self.horizontal = horizontal # True if horizontal, False if vertical
#         self.positions = self.calc_positions() # Stores occupied positions

#     def calc_positions(self):
#         """Calculates the coordinates occupied by the ship, with orientation"""
#         return [(self.x + i, self.y) if self.horizontal else (self.x, self.y + i) for i in range(self.size)]
    
#     def is_hit(self, x, y):
#         """Check if collected coordinates connect"""
#         return (x,y) in self.positions

# class ship:

#     def __init__(self, size, horizontal, x, y):
#         self.size = size
#         self.x = x
#         self.y = y
#         self.horizontal = horizontal
#         self.ship_object = size_ship(size, x, y, horizontal)

#     def hit(self, x, y):
#         # if in x,y area of ship then return true
#         # return True
    
#         # KHALIFF: for my new thing, it'll need a little different processing of the information, looking at the object now
#         return self.ship_object.is_hit(x, y)


class board:
    map = []
    size = 10

    def __init__(self):
        for i in range(self.size):
            self.map.append([])
            for j in range(self.size):
                self.map[i].append(EMPTY_SYMBOL)
        
    def drawmap(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.map[i][j],end="")
            print()

    def drawhidden(self):
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
                    break

            # if self.map[x][y] == EMPTY_SYMBOL:  # Ensure ship isn't placed on another
                # self.map[x][y] = SHIP_SYMBOL
                # break

    def hit(self,array,x,y):
        if x > 9 or x < 0 or y > 9 or y < 0:
            print("Coordinates out of range")
            return None
        
        if (self.map[x][y] == SHIP_SYMBOL) :
            self.map[x][y] = HIT_SYMBOL

            return True
        else: 
            return False
        
    def printmap(self):
        print(self.map)
    

board1 = board()

board1.drawmap()

board1.drawhidden()