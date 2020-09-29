import queue
import tkinter as tk
from Tile import *

# Build a board with a start & finish point
def createBoard():
    setup = []
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

    board = []

    for row in range(len(setup)):
        temp = []
        for col in range(len(setup[0])):
            temp.append(Tile(row, col, setup[row][col]))
        board.append(temp)
    return board


# Print out board with best path
def printBoard(path, board):
    root = tk.Tk()
    root.title("Interactive Pathfinder 1.0.0")
    root.geometry("500x400")
    root.resizable(False, False)

    if len(path) == 0:
        print("No available path between points! :(")
        return

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] in path:
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
def findPath(board):
    # Find start point
    start = None
    count = 0
    for i in board[0]:
        if i.getChar() == "0":
            start = board[0][count]
            break
        count = count + 1

    # Find end point
    end = None
    count = 0
    for i in board[len(board) - 1]:
        if i.getChar() == "1":
            end = board[len(board) - 1][count]
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
    if dictionary.get(end) == None:
        path = []
        return path
    path = []
    x = end

    while x != start:
        path.append(x)
        x = dictionary.get(x)

    path.append(start)

    return path

# Take in user input for grid size
def getGridInput():
    root = tk.Tk()
    root.title("Welcome!")
    root.geometry("225x190")
    root.resizable(False, False)

    canvas = tk.Canvas(root)
    canvas.pack()

    label1 = tk.Label(root, text="Enter number of columns:")
    label1.place(relx=0.1875, rely=0.05)

    entry1 = tk.Entry(root)
    canvas.create_window(225 / 2, 190 / 4.2, window=entry1)
    gridWidth = entry1.get()

    label2 = tk.Label(root, text="Enter number of rows:")
    label2.place(relx=0.22, rely=0.32)

    entry2 = tk.Entry(root)
    canvas.create_window(225 / 2, 190 / 2, window=entry2)
    gridHeight = entry2.get()

    button = tk.Button(root, text="Generate Board", bg="light blue", command=retriveEntry(gridWidth, gridHeight), width=13)
    button.place(relx=0.27, rely=0.65)

    return

def retriveEntry(gridWidth, gridHeight):
    print("hi")
    return
