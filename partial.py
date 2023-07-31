from functools import partial

"""
Why use partial:
    partial copy a function into a new one, 
    with some of the original parameter(even not positional arg) pre-defined
"""


def adding(a, b, c, d):
    return a * 10000 + b * 1000 + c * 100 + d * 10 + 1


if __name__ == "__main__":
    new_f = partial(adding, d=2)
    print("\nnum for new function : %d" % (new_f(3, 2, 1)))
