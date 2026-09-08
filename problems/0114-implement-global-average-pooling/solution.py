import numpy as np

def global_avg_pool(x: np.ndarray) -> np.ndarray:
    height, width, channels = x.shape

    output = np.zeros(channels)

    for i in range(height):
        for j in range(width):
            output += x[i, j, :]

    output /= (height * width)

    return output