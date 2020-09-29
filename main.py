from PathFinder import *

def main():
    getGridInput()
    board = createBoard()
    path = findPath(board)
    printBoard(path, board)

main()