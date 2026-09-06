import numpy as np

def off_policy_mc_control(episodes: list, behavior_policy: dict, n_states: int, n_actions: int, gamma: float = 1.0) -> list:
    """
    Off-policy Monte Carlo control using weighted importance sampling.
    """
    # Initialize Q(s,a) and cumulative weights C(s,a)
    Q = np.zeros((n_states, n_actions))
    C = np.zeros((n_states, n_actions))

    for episode in episodes:
        G = 0.0
        W = 1.0

        # Process episode backward
        for state, action, reward in reversed(episode):

            # Update return
            G = gamma * G + reward

            # Update cumulative importance-sampling weight
            C[state, action] += W

            # Weighted incremental update of Q
            Q[state, action] += (
                W / C[state, action]
            ) * (G - Q[state, action])

            # Find greedy action, ties broken by lowest index
            greedy_action = np.argmax(Q[state])

            # If behavior action is not greedy, stop processing episode
            if action != greedy_action:
                break

            # Importance sampling ratio
            probability = behavior_policy.get((state, action), 0.0)

            if probability == 0:
                break

            W = W / probability

    # Round to 4 decimal places and convert to nested list
    return np.round(Q, 4).tolist()