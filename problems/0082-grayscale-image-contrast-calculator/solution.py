import numpy as np

def calculate_contrast(img) -> int:
    return int(np.max(img) - np.min(img))