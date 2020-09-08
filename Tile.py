# Create Tile objects that compose the board
class Tile:
    def __init__(self, row, col, char):
        self.row = row
        self.col = col
        self.char = char
        self.visited = False

    def checkValid(self):
        if (self.char == "*"):
            return False
        return True

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getVisited(self):
        return self.visited

    def setVisited(self, status):
        self.visited = status

    def getChar(self):
        return self.char