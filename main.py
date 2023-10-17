from sudoku import Sudoku

def main(filename):


    puzzle = Sudoku(filename)
    print('\n')
    for row in puzzle.rows:
        print(row)
    # print(puzzle.rows)
    # print('\n')
    puzzle.solve()
    print('\n')

    for row in puzzle.rows:
        print(row)

    # print(puzzle.mutable_rows)

    # puzzle.get_square(1,8)
    # print('\n')
    # puzzle.get_square(6, 5)
    # print('\n')
    # puzzle.get_square(2, 0)

    # assert puzzle.get_square(0,0) == puzzle.get_square(1,0) == puzzle.get_square(2,0)
    # print('\n')
    # assert puzzle.get_square(3,0) == puzzle.get_square(4,0) == puzzle.get_square(5,0)
    # print('\n')
    # assert puzzle.get_square(6,0) == puzzle.get_square(7,0) == puzzle.get_square(8,0)
    # print('\n')

main(filename = 'puzzles/one.csv')
