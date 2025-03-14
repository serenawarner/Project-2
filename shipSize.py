from random import randint as r
class shipSize:

    def __init__(self, rotation, x):
        self.size = size
        self.rotation = rotation
        self.x = x
        self.y = y

    def place_varied_ship(self):
        """Randomly places a ship on the map."""
        while True:
            # TODO:
            # ADD an array full of different sizes (e.g. ship_size = [(1,3), (1,5), (1,3)] )
            # CHECK placement is not out-of-bounds; if clause
            # ADD rotation of ship; 0 is vertical, 1 is horizontal 
            # CHECK bounds again 

            ship_size = [(1, r(1,5))]
            x, y = (0, self.size - 1), random.randint(0, self.size - 1)
            if self.hidden_map[x][y] == EMPTY_SYMBOL:  # Ensure ship isn't placed on another
                if # Ensure the ship fits within bounds
                self.hidden_map[x][y] == SHIP_SYMBOL
                break

    def hit(self):
        if in (x,y) of shipSize:
            return True for hit
            Place