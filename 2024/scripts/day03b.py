import numpy as np
import re
from day03a import input, mul_pattern

test = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

do_pattern = re.compile(r"(?P<enable>do\(\))")
dont_pattern = re.compile(r"(?P<disable>don\'t\(\))")

instruction_pattern = re.compile('|'.join('(?:{0})'.format(x.pattern) for x in [mul_pattern, do_pattern, dont_pattern]))
# [m.groupdict() for m in dont_pattern.finditer(s)]

def mulSum(instructions):
    instructions_enabled = True
    total = 0
    for m in instruction_pattern.finditer(instructions):
        # print(f"{m.groups()}")
        if m.groupdict()["enable"]:
            instructions_enabled = True
            print("code_enabled")
        elif m.groupdict()["disable"]:
            instructions_enabled = False
            print("code_disabled")
        elif instructions_enabled:
            total += np.prod([int(i) for i in m.groups()[:2]])
            print(f"{total = }")
    return total

ans = mulSum(input)

if __name__ == "__main__":
    print(ans)
    print(f"{instruction_pattern.pattern}")
    # print(test)