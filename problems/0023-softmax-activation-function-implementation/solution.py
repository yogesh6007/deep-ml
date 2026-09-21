import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    max_score=max(scores)
    exp_values = [math.exp(x-max_score) for x in scores]
    total=sum(exp_values)
    return [x/total for x in exp_values]