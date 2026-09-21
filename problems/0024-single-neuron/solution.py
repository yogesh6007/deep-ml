import math
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    probabilities = []
    for row in features:
        z = sum(row[i] * weights[i] for i in range(len(weights))) + bias
        probability = 1 / (1 + math.exp(-z))
        probabilities.append(round(probability, 4))
    mse = sum((probabilities[i] - labels[i]) ** 2 for i in range(len(labels))) / len(labels)
    mse = round(mse, 4)
    return probabilities, mse