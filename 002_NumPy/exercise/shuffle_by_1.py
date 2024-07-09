import numpy as np


def shuffle_by_1(A):
    """
    Shuffles the columns of a matrix to the right by one.

    This function returns the matrix A with columns shuffled to the right by 1,
    such that the new ith col is the old i-1th col, and the new 1st col 
    is the old last col.
    """

    return np.roll(A, 1 , 1)


if __name__ == '__main__':
    ans = shuffle_by_1(np.array([[1,2,3],[4,5,6],[7,8,9]]))
    print(ans)
