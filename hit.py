class board:
    map = [[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "]]

    def hit(self,x,y):
        if x > 9 or x < 0 or y > 9 or y < 0:
            print("Coordinates out of range")