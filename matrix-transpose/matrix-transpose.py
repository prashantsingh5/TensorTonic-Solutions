import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A=np.asarray(A)
    N, M = A.shape
    transpose=np.empty((M,N),dtype=A.dtype)
    for i in range(N):
        for j in range(M):
            transpose[j,i]=A[i][j]
    return transpose
