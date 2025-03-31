class board:
     
    map = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "], 
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
           ]

    def __init__(self, h):
        for i in range(0,len(self.map)):
            for j in range(0, len(self.map)):
                if h == False:
                    self.map[i][j] = "🌊"
                else:
                    self.map[i][j] = "◼️ "
        
    def drawmap(self):
        for i in range(len(self.map)):
            printstring = ""
            for j in self.map[i]:
                printstring = printstring + j
            print(printstring)


hiddenboard = board(True)
hiddenboard.drawmap()

visibleboard = board(False)
visibleboard.drawmap()