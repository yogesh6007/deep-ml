import numpy as np

def fit_sigmoid_scaling(nll_list, acc_list, predict_nll):
    nll = np.array(nll_list)
    acc = np.array(acc_list)

    # Convert accuracy to logit-space target
    z = np.log((1 - acc) / acc)

    # Linear regression: z = a * nll + b
    X = np.column_stack((nll, np.ones(len(nll))))

    a, b = np.linalg.lstsq(X, z, rcond=None)[0]

    # Predict accuracy
    predicted_acc = 1 / (1 + np.exp(a * predict_nll + b))

    return [a, b, predicted_acc]