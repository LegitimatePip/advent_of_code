import re
import numpy as np

test = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

def findXmasFromBoard(board = test, s="XMAS"):
    # d = {"X": 0, "M": 1, "A": 2, "S": 3}
    # board_array = np.array([[d[char] for char in list(line)] for line in board.split("\n")])
    l = len(s)-1
    s0 = np.array([char for char in s])
    s1 = np.flip(s0)
    board_array = np.array(
        [[char for char in line] for line in board.splitlines()],
        dtype="<U1",
        )
    height, width = board_array.shape
    forward = np.arange(4)
    backward = np.arange(3, -1, -1)
    zero = np.zeros(4, dtype=int)
    vertical = np.sum(
        np.fromiter(
            (
            np.array_equal(
                board_array[forward+i[0], zero+i[1]],
                s0) or
            np.array_equal(
                board_array[forward+i[0], zero+i[1]],
                s1)
            for i in np.ndindex(height-l, width)
            ), dtype = int
            )
        )
    horizontal = np.sum(
        np.fromiter(
            (
            np.array_equal(
                board_array[zero+i[0], forward+i[1]],
                s0) or
            np.array_equal(
                board_array[zero+i[0], forward+i[1]],
                s1)
            for i in np.ndindex(height, width-l)
            ), dtype = int
            )
        )
    # diagonal0 is top-left to bottom-right
    diagonal0 = np.sum(
        np.fromiter(
            (
            np.array_equal(
                board_array[forward+i[0], forward+i[1]],
                s0) or
            np.array_equal(
                board_array[forward+i[0], forward+i[1]],
                s1)
            for i in np.ndindex(height-l, width-l)
            ), dtype = int
            )
        )
    # diagonal1 is top-right to bottom-left
    diagonal1 = np.sum(
        np.fromiter(
            (
            np.array_equal(
                board_array[forward+i[0], backward+i[1]],
                s0) or
            np.array_equal(
                board_array[forward+i[0], backward+i[1]],
                s1)
            for i in np.ndindex(height-l, width-l)
            ), dtype = int
            )
        )
    results = [vertical, horizontal, diagonal0, diagonal1]
    result = np.sum(results)
    return result

with open("inputs/day04.txt", "r") as file:
    input = file.read()

ans = findXmasFromBoard(input)

if __name__ == "__main__":
    print(ans)