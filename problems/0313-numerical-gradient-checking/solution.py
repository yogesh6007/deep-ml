import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    numerical_grad = np.zeros_like(x, dtype=float)

    for i in range(x.size):
        x_plus = x.copy()
        x_minus = x.copy()

        x_plus.flat[i] += epsilon
        x_minus.flat[i] -= epsilon

        numerical_grad.flat[i] = (
            f(x_plus) - f(x_minus)
        ) / (2 * epsilon)

    norm_num = np.linalg.norm(numerical_grad)
    norm_analytical = np.linalg.norm(analytical_grad)

    if norm_num + norm_analytical == 0:
        relative_error = 0.0
    else:
        relative_error = (
            np.linalg.norm(numerical_grad - analytical_grad)
            / (norm_num + norm_analytical)
        )

    return numerical_grad, relative_error