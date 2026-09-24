import numpy as np
from typing import Tuple
def find_best_split(X: np.ndarray, y: np.ndarray) -> Tuple[int, float]:
    n, d = X.shape
    best_feature = 0
    best_threshold = 0.0
    best_gini = float("inf")
    for j in range(d):
        thresholds = np.unique(X[:, j])
        for threshold in thresholds:
            left = y[X[:, j] <= threshold]
            right = y[X[:, j] > threshold]
            if len(left) == 0 or len(right) == 0:
                continue
            p_left = np.mean(left)
            p_right = np.mean(right)
            gini_left = 2 * p_left * (1 - p_left)
            gini_right = 2 * p_right * (1 - p_right)
            weighted_gini = (len(left) * gini_left + len(right) * gini_right) / n
            if weighted_gini < best_gini:
                best_gini = weighted_gini
                best_feature = j
                best_threshold = threshold
    return best_feature, best_threshold