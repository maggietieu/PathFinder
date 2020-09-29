from PathFinder import *

def main():
    board = Board()
    getGridInput(board)
    board.createSetup()
    board.findPath()
    board.printBoard()

# Take in user input for grid size
def getGridInput(board):
    root = tk.Tk()
    root.title("Welcome!")
    root.geometry("225x190")
    root.resizable(False, False)

    canvas = tk.Canvas(root)
    canvas.pack()

    label1 = tk.Label(root, text="Enter number of columns:")
    label1.place(relx=0.1875, rely=0.05)
    label2 = tk.Label(root, text="Enter number of rows:")
    label2.place(relx=0.22, rely=0.32)

    entry1 = tk.Entry(root)
    canvas.create_window(225 / 2, 190 / 4.2, window=entry1)
    entry2 = tk.Entry(root)
    canvas.create_window(225 / 2, 190 / 2, window=entry2)
    numColumns = entry1.get()
    numRows = entry2.get()

    button = tk.Button(root, text="Generate Board", bg="light blue", command=board.setGrid(numColumns, numRows), width=13)
    button.place(relx=0.27, rely=0.65)

    return

main()