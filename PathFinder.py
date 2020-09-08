import queue
from Tile import *


# Build a board with a start & finish point
def createBoard():
    setup = []
    setup.append(["*", "*", "0", "*"])
    setup.append(["*", " ", " ", "*"])
    setup.append([" ", " ", "*", "*"])
    setup.append([" ", " ", "1", "*"])

    board = []

    for row in range(len(setup)):
        temp = []
        for col in range(len(setup[0])):
            temp.append(Tile(row, col, setup[row][col]))
        board.append(temp)
    return board


# Print out board with best path
def printBoard(path, board):
    if (len(path) == 0):
        print("No available path between points! :(")
        return

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] in path:
                print("+", end=" ")
            else:
                print(board[row][col].getChar(), end=" ")
        print("")


# BFS to find optimal path
def findPath(board):
    # Find start point
    start = None
    count = 0
    for i in board[0]:
        if (i.getChar() == "0"):
            start = board[0][count]
            break
        count = count + 1

    # Find end point
    end = None
    count = 0
    for i in board[len(board) - 1]:
        if (i.getChar() == "1"):
            end = board[len(board) - 1][count]
            break
        count = count + 1

    # Breadth First Search Algorithm:

    # dictionary contains keys for each Tile. value is the 1st Tile to visit it.
    dictionary = {}

    # 1. Begin at start & create dictionary. Continue BFS until frontier queue is empty.
    frontier = queue.Queue()
    frontier.put(start)

    while (frontier.qsize() > 0):
        current = frontier.get()
        current.setVisited(True)

        row = current.getRow()
        col = current.getCol()

        # Add neighbors to frontier if they are valid & not yet visited
        if (row - 1) >= 0:
            up = board[row - 1][col]
            if (up.getVisited() == False) and (up.checkValid() == True):
                frontier.put(up)
                # The 1st tile to neighbor another is its value within the dictionary.
                if dictionary.get(up) is None:
                    dictionary[up] = current

        if (row + 1) < len(board):
            down = board[row + 1][col]
            if (down.getVisited() == False) and (down.checkValid() == True):
                frontier.put(down)
                if dictionary.get(down) is None:
                    dictionary[down] = current

        if (col - 1) >= 0:
            left = board[row][col - 1]
            if (left.getVisited() == False) and (left.checkValid() == True):
                frontier.put(left)
                if dictionary.get(left) is None:
                    dictionary[left] = current

        if (col + 1) < len(board[0]):
            right = board[row][col + 1]
            if (right.getVisited() == False) and (right.checkValid() == True):
                frontier.put(right)
                if dictionary.get(right) is None:
                    dictionary[right] = current

    # 3. Use the dictionary to backtrack the most efficient path
    if (dictionary.get(end) == None):
        path = []
        return path
    path = []
    x = end

    while (x != start):
        path.append(x)
        x = dictionary.get(x)

    path.append(start)

    return path