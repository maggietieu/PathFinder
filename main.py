from PathFinder import *

def main():
    board = createBoard()
    path = findPath(board)
    printBoard(path, board)

main()