import numpy as np

def off_policy_nstep_td(
    episodes: list,
    behavior_policy: list,
    target_policy: list,
    num_states: int,
    num_actions: int,
    n: int,
    alpha: float,
    gamma: float
) -> np.ndarray:

    # Initialize state values to 0
    V = np.zeros(num_states)

    # Process each episode
    for episode in episodes:

        T = len(episode)

        # Process each time step
        for t in range(T):

            # -------------------------
            # Calculate n-step return
            # -------------------------
            G = 0.0

            end = min(t + n, T)

            for k in range(t, end):
                state, action, reward = episode[k]

                G += (gamma ** (k - t)) * reward

            # Bootstrap if episode has not ended
            if t + n < T:
                next_state = episode[t + n][0]
                G += (gamma ** n) * V[next_state]

            # -------------------------
            # Importance sampling ratio
            # -------------------------
            rho = 1.0

            for k in range(t, end):
                state, action, reward = episode[k]

                b = behavior_policy[state][action]
                pi = target_policy[state][action]

                if b == 0:
                    rho = 0.0
                    break

                rho *= pi / b

            # -------------------------
            # TD update
            # -------------------------
            state = episode[t][0]

            V[state] += alpha * rho * (G - V[state])

    return V