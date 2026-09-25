import numpy as np

def forward_diffusion(x_0, t, beta_start, beta_end, num_timesteps, noise):
    betas = np.linspace(beta_start, beta_end, num_timesteps)
    alphas = 1 - betas
    alpha_bar = np.cumprod(alphas)
    alpha_t = alpha_bar[t - 1]
    x_t = np.sqrt(alpha_t) * x_0 + np.sqrt(1 - alpha_t) * noise
    return x_t