def rejection_sampling_best_of_k(candidates, scores):
    result = []
    for i in range(len(candidates)):
        best = 0
        for j in range(1, len(scores[i])):
            if scores[i][j] > scores[i][best]:
                best = j
        result.append(candidates[i][best])
    return result