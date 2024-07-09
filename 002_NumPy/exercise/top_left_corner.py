import numpy as np


def top_left_corner(A, r, c):
    """
    Select the top-left corner of a matrix.

    This function returns the r-by-c top-left corner of the matrix A
    """
    return A[:r,:c]


if __name__ == "__main__":
    ans = top_left_corner(np.array([[1,2,3], [4,5,6], [7,8,9]]), 3,1)
    print(ans)

