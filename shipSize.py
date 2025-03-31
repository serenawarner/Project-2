class shipSize:

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
    
    def checker(self):
        return f"Ship(size ={self.size}, positions ={self.positions})"