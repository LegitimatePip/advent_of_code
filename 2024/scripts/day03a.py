import re
import numpy as np

test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open("2024/inputs/day03", "r") as f:
    input = f.read()

mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")

def mulSum(instructions):
    return np.sum(
        np.prod([int(i) for i in inputs])
        for inputs in mul_pattern.findall(instructions)
    )
    # for inputs in mul_pattern.findall(instructions):
    #     print(([int(i) for i in inputs]))
    #     print(np.prod([int(i) for i in inputs]))


ans = mulSum(input)

if __name__ == "__main__":
    # for match in mul_pattern.findall(test):
    #     print(match)
    # print(mul_pattern.findall(test))
    print(ans)
    # print(input)