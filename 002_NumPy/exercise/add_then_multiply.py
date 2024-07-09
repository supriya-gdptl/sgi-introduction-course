import numpy as np


def add_then_multiply(a1, a2, m):
    """Adds the two numbers a1 and a2, then multiplies the result of the
    addition by m.
    """
    return (a1+a2)*m


if __name__ == '__main__':
    print(add_then_multiply(3,4,2))
