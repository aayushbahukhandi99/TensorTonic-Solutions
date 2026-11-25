import math

def gaussian_kernel(size: int, sigma: float) -> list:
    """
    Returns a square two-dimensional list.
    """
    # Write code here
    kernel = []
    center = size // 2
    total = 0.0

    for i in range(size):
        row = []
        for j in range(size):
            x = j - center
            y = i - center

            value = math.exp(-(x*x + y*y) / (2*sigma**2))
            row.append(value)
            total += value

        kernel.append(row)

    return [[val / total for val in row] for row in kernel]