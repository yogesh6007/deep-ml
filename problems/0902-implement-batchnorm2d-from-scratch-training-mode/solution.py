import torch



def batchnorm2d(x, gamma, beta, eps=1e-5):
    mean = x.mean(dim=(0, 2, 3), keepdim=True)

    variance = ((x - mean) ** 2).mean(dim=(0, 2, 3), keepdim=True)

    x_norm = (x - mean) / torch.sqrt(variance + eps)

    gamma = gamma.reshape(1, -1, 1, 1)
    beta = beta.reshape(1, -1, 1, 1)

    return gamma * x_norm + beta