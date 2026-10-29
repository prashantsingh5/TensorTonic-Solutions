import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    if len(y) == 0:
        return 0.0
    labels,counts = np.unique(y,return_counts=True)
    pi = counts/len(y)
    entropy = -pi*(np.log2(pi))
    return sum(entropy)