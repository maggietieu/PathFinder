import queue
import tkinter as tk
from Tile import *

class Board:
    setup = []
    board = []
    path = []
    colCount = 0
    rowCount = 0

    # Build a board setup with a start & finish point
    def createSetup(self):
        setup = self.setup
        board = self.board

        setup.append(["*", "*", "0", "*"])
        setup.append(["*", " ", " ", "*"])
        setup.append([" ", " ", " ", " "])
        setup.append([" ", " ", "*", "*"])
        setup.append(["*", " ", "*", "*"])
        setup.append([" ", " ", "*", "*"])
        setup.append(["*", " ", "*", "*"])
        setup.append(["*", " ", " ", "*"])
        setup.append([" ", "*", " ", " "])
        setup.append([" ", " ", "*", " "])
        setup.append([" ", " ", "1", " "])

        for row in range(len(setup)):
            temp = []
            for col in range(len(setup[0])):
                temp.append(Tile(row, col, setup[row][col]))
            board.append(temp)

    # Print out board with best path
    def printBoard(self):
        board = self.board
        root = tk.Tk()
        root.title("Interactive Pathfinder 1.0.0")
        root.geometry("500x400")
        root.resizable(False, False)

        if len(self.path) == 0:
            print("No available path between points! :(")
            return

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in self.path:
                    #print("+", end=" ")
                    displayPath = tk.Label(root, text="            ", bg="#6ddade")
                    displayPath.grid(row=row, column=col)
                else:
                    #print(board[row][col].getChar(), end=" ")
                    if(board[row][col].getChar() == " "):
                        open = tk.Label(root, text="            ", bg="#c7c7c7")
                        open.grid(row=row, column=col)
                    else:
                        wall = tk.Label(root, text="            ", bg="#03128a")
                        wall.grid(row=row, column=col)
            print("")

        root.mainloop()


    # BFS to find optimal path
    def findPath(self):
        # Find start point
        start = None
        count = 0
        for i in self.board[0]:
            if i.getChar() == "0":
                start = self.board[0][count]
                break
            count = count + 1

        # Find end point
        end = None
        count = 0
        for i in self.board[len(self.board) - 1]:
            if i.getChar() == "1":
                end = self.board[len(self.board) - 1][count]
                break
            count = count + 1

        # Breadth First Search Algorithm:

        # dictionary contains keys for each Tile. value is the 1st Tile to visit it.
        dictionary = {}

        # 1. Begin at start & create dictionary. Continue BFS until frontier queue is empty.
        frontier = queue.Queue()
        frontier.put(start)

        while frontier.qsize() > 0:
            current = frontier.get()
            current.setVisited(True)

            row = current.getRow()
            col = current.getCol()

            # Add neighbors to frontier if they are valid & not yet visited
            if (row - 1) >= 0:
                up = self.board[row - 1][col]
                if (up.getVisited() == False) and (up.checkValid() == True):
                    frontier.put(up)
                    # The 1st tile to neighbor another is its value within the dictionary.
                    if dictionary.get(up) is None:
                        dictionary[up] = current

            if (row + 1) < len(self.board):
                down = self.board[row + 1][col]
                if (down.getVisited() == False) and (down.checkValid() == True):
                    frontier.put(down)
                    if dictionary.get(down) is None:
                        dictionary[down] = current

            if (col - 1) >= 0:
                left = self.board[row][col - 1]
                if (left.getVisited() == False) and (left.checkValid() == True):
                    frontier.put(left)
                    if dictionary.get(left) is None:
                        dictionary[left] = current

            if (col + 1) < len(self.board[0]):
                right = self.board[row][col + 1]
                if (right.getVisited() == False) and (right.checkValid() == True):
                    frontier.put(right)
                    if dictionary.get(right) is None:
                        dictionary[right] = current

        # 3. Use the dictionary to backtrack the most efficient path
        if dictionary.get(end) == None:
            return self.path
        self.path = []
        x = end

        while x != start:
            self.path.append(x)
            x = dictionary.get(x)

        self.path.append(start)

        return self.path


    def setGrid(self, gridWidth, gridHeight):
        self.colCount = gridWidth
        self.rowCount = gridHeight
        return
