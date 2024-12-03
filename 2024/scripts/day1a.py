import numpy as np
import re
# from pathlib import Path

with open("2024/inputs/day01", "r") as f:
    input = f.read()

pattern0 = re.compile(r"(\d+)\w+(\d+)")
pattern1 = re.compile(r"\d+")

for line in input:
    pattern1.findall(line)

a, b = zip(*[pattern1.findall(line) for line in input.split("\n")])

c = np.array(a, dtype=int)
d = np.array(b, dtype=int)

e = np.sort(c)
f = np.sort(d)

x = np.abs(e-f)

ans = np.sum(x)

if __name__ == "__main__":
    pass
    print(ans)
    # for line in input.split("\n"):
    #     print(line)
    #     print(pattern1.findall(line))
    #     break