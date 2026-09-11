def label_encode_ordinal(values: list, order: list) -> list:
    mapping = {}

    for i in range(len(order)):
        mapping[order[i]] = i

    result = []

    for value in values:
        if value in mapping:
            result.append(mapping[value])
        else:
            result.append(-1)

    return result