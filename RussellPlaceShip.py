import random

EMPTY_SYMBOL = "🌊"  # Water
SHIP_SYMBOL = "🚢"  #ship

def place_ship(self, ship_size=1):
        """Randomly places a ship on the map."""
        while True:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if self.hidden_map[x][y] == EMPTY_SYMBOL:  # Ensure ship isn't placed on another
                self.hidden_map[x][y] = SHIP_SYMBOL
                break