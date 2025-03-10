class board:
    map = []

    def __init__(self):
        for i in range(10):
            self.map.append([])
            for j in range(10):
                self.map[i].append(" ")

    def hit(self,x,y):
        if x > 9 or x < 0 or y > 9 or y < 0:
            print("Cordinates out of range")
            return None
        
        self.map[x][y] = "X"
    

board1 = board()
print(board.map)

board1.hit(5,5)

print(board.map)
        