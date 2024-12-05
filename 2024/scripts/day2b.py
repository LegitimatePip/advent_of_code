import numpy as np
import re
from day2a import input, num_pattern, isSafe

def isDampenerSafe(a):
    for i in np.arange(a.shape[0]):
        if isSafe(np.delete(a, i)):
            return True
    else:
        return False

ans = np.sum(isDampenerSafe(np.array(num_pattern.findall(line), dtype = int)) for line in input.split("\n"))

if __name__ == "__main__":
    print(ans)