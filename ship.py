class ShipSize:
    def __init__(self, size, x, y, horizontal=True):
        self.size = size # Number of grid spaces the ship takes up
        self.x = x # Starting x coords
        self.y = y # Starting y coords
        self.horizontal = horizontal # True if horizontal, False if vertical
        self.positions = self.calc_positions() # Stores occupied positions

    def calc_positions(self):
        """Calculates the coordinates occupied by the ship, with orientation"""
        return [(self.x + i, self.y) if self.horizontal else (self.x, self.y + i) for i in range(self.size)]
    
    def is_hit(self, x, y):
        """Check if collected coordinates connect"""
        return (x,y) in self.positions


class Ship:
    def __init__(self, size, horizontal, x, y):
        self.size = size
        self.x = x
        self.y = y
        self.horizontal = horizontal
        self.ship_object = ShipSize(size, x, y, horizontal)

    def hit(self, x, y):
        # if in x,y area of ship then return true
        # return True
    
        # KHALIFF: for my new thing, it'll need a little different processing of the information, looking at the object now
        return self.ship_object.is_hit(x, y)