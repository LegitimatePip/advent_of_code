import numpy as np
import re

with open("2024/inputs/day02", "r") as f:
    input = f.read()

num_pattern = re.compile(r"\d+")

def isSafe(a: np.array):
    diffs = np.diff(a)
    check1 = np.unique(np.sign(diffs)).shape[0] == 1
    check2 = np.setdiff1d(np.abs(diffs), np.arange(1, 4)).shape[0] == 0
    # ans = check1 and check2
    # if not ans:
    #     print(f"{check1 = }\n{check2 = }")
    return check1 and check2

# for line in input.split("\n"):
#     a = np.array(num_pattern.findall(line), dtype = int)
#     print(a)
#     print(isSafe(a))
#     # break

ans = np.sum(isSafe(np.array(num_pattern.findall(line), dtype = int)) for line in input.split("\n"))

if __name__ == "__main__":
    # print(isSafe(a))
    print(ans)
    pass