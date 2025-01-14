import re
import numpy as np
from operator import add, mul
from itertools import product

test =\
"""190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

with open("inputs/day07", "r") as file:
    input = file.read()

def parseInput(input):
    LHS = []
    RHS = []
    p = re.compile("\d+")
    for line in input.split("\n"):
        for i, side in enumerate(line.split(":")):
            if i == 0:
                LHS.append(int(side))
            else:
                RHS.append([int(num) for num in p.findall(side)])
    return LHS, RHS

def calibrationResult(LHS, RHS, operators = [add, mul]):
    for i, seq in enumerate(product(operators, repeat=len(RHS)-1)):
        ans = None
        for j, n in enumerate(RHS):
            if ans is not None:
                ans = seq[j-1](ans, n)
            else:
                ans = n
        # print(f"{i}: {ans}")
        if ans == LHS:
            return True
    else:
        return False

def totalCalibrationResult(LHS, RHS, operators = [add, mul]):
    return np.sum(
        np.fromiter(
            (num for i, num in enumerate(LHS) if calibrationResult(LHS[i], RHS[i], operators)),
            dtype = int
        )
    )

def concatenate(a, b):
    """
    a, b must be numbers
    returns the base-10 concatenation of a and b
    """
    return int(str(a)+str(b))

if __name__ == "__main__":
    LHS, RHS = parseInput(input)
    # print(LHS)
    # print(RHS)
    # i = 3
    # print(calibrationResult(LHS[i], RHS[i]))
    # print(totalCalibrationResult(LHS, RHS))
    print(totalCalibrationResult(LHS, RHS, operators=[add, mul, concatenate]))