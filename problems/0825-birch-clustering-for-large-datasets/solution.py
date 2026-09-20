import numpy as np

def birch_cluster(X, threshold):
    X = np.asarray(X, dtype=float)
    subclusters = []
    for x in X:
        if not subclusters:
            subclusters.append({
                "N": 1,
                "LS": x.copy(),
                "SS": x * x
            })
            continue
        best_idx = 0
        best_dist = float("inf")
        for i, cf in enumerate(subclusters):
            centroid = cf["LS"] / cf["N"]
            dist = np.linalg.norm(x - centroid)
            if dist < best_dist:
                best_dist = dist
                best_idx = i
        cf = subclusters[best_idx]
        new_N = cf["N"] + 1
        new_LS = cf["LS"] + x
        new_SS = cf["SS"] + x * x
        mean = new_LS / new_N
        variance = new_SS / new_N - mean * mean
        variance = np.maximum(variance, 0.0)
        radius = np.sqrt(np.sum(variance))
        if radius <= threshold:
            cf["N"] = new_N
            cf["LS"] = new_LS
            cf["SS"] = new_SS
        else:
            subclusters.append({
                "N": 1,
                "LS": x.copy(),
                "SS": x * x
            })
    centroids = [
        (cf["LS"] / cf["N"]).tolist()
        for cf in subclusters
    ]
    centroids.sort()
    return centroids