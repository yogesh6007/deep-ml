import numpy as np
def batch_iterator(X, y=None, batch_size=64):
    result = []
    for i in range(0, len(X), batch_size):
        X_batch = X[i:i + batch_size]
        if y is not None:
            result.append([X_batch.tolist(), y[i:i + batch_size].tolist()])
        else:
            result.append(X_batch)
    return result