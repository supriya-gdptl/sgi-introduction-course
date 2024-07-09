import numpy as np


def det2x2(A):
    """
    Compute the determinant of a 2x2 matrix.

    This function returns the determinant of the 2x2 matrix A.
    """

    return (A[0,0]*A[1,1])-(A[0,1]* A[1,0])


if __name__ == '__main__':
    print(det2x2(np.array([[1,7], [2,8]])))

