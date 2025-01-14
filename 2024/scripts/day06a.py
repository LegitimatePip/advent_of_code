import re
import numpy as np

test ="""\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

with open("inputs/day06", "r") as file:
    input = file.read()

class Map():
    # def interpretChar(char):
    #     directions = ["^", ">", "v", "<"]
    #     walls = 
    #     if char in directions:
    #         return "."
    #     else:
    #         return char
    def isWall(char):
        return char == "#"
    def resetGuardPos(self):
        self.guard_pos = self.start_pos.copy()
        self.guard_dir = -1j
        self.travel_map = np.zeros(self.map.shape)
        self.travel_map[*self.guard_pos] = True
    def turnGuard(self):
        self.guard_dir *= 1j
    def __init__(self, map):
        self.map = np.array(
            [
                [(char) for char in line]
                for line in test.split("\n")
            ]
        )
        self.start_pos = np.argwhere(map=="^").flatten()
        self.resetGuardPos()
        self.wall_map = np.array(
            [
                [(char == "#") for char in line]
                for line in map.split("\n")
            ]
        )
    def moveGuard(self):
        # stop_point is nearest wall (for stop conditions)
        if self.guard_dir == -1j:
            stop_point = np.array(
                [np.argwhere(self.wall_map[:self.guard_pos[0]+1, self.guard_pos[1]]).flatten()]
                )
            

if __name__ == "__main__":
    my_map = Map(test)
    print(my_map.start_pos)
    # print(np.argwhere(my_map.map=="^").flatten())