class board:
    def drawmap():
        pass


#whether or not it was hit and is there a ship piece there?
hit = '0'
ship = '0'
space = [hit,ship]
rows, cols = (10, 10)

#initialize space for each element in col then repeat in with rows
arr = [[space for i in range(cols)] for j in range(rows)]

for row in arr:
    print(row)