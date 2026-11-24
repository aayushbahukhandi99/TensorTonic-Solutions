import numpy 
def linear_layer_forward(X: list, W: list, b: list) -> list:
    """
    Returns the affine transformation for every input row.
    """
    # Write code here
    X = np.asarray(X)
    W = np.asarray(W)
    b = np.asarray(b)
    output =  X@W + b
    return output.tolist()