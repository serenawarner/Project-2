import random

EMPTY_SYMBOL = "🌊"  # Water
SHIP_SYMBOL = "🚢"  # ship
HIT_SYMBOL = "💥" # explosion
HIDDEN_SYMBOL = "◼️ "

class ship:

    def __init__(self, size, rotation, x, y):
        self.size = size
        self.x = x
        self.y = y

    def hit(self):
        # if in x,y area of ship then return true
        return True


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
            if self.map[x][y] == EMPTY_SYMBOL:  # Ensure ship isn't placed on another
                self.map[x][y] = SHIP_SYMBOL
                break

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