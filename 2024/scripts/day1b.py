import numpy as np
from day1a import c, d

def similarity_score(a, b):
    d = dict(zip(*np.unique(b, return_counts=True)))
    def f(x):
        if x in d.keys():
            return x * d[x]
        else:
            return 0
    return np.vectorize(f)(a)

# print(
#     list(zip(c, similarity_score(c, d)))
#     )

ans = np.sum(similarity_score(c, d))

if __name__ == "__main__":
    print(ans)
    # print()
    pass