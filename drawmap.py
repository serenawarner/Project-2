class board:
    map = [[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "],[" ", " ", " ", " ", " "]]

    def mapinit(h):
        if h == True:
            for i in map:
                for j in map[i]:
                    map[i[j]] = "\U00025A1"
        else:
            for i in map:
                for j in map[i]:
                    map[i[j]] = 
        
    
    def drawmap():
        
        