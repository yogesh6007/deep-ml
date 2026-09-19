def differential_sarsa(transitions: dict, initial_state: str,
                       alpha: float, beta: float, num_steps: int) -> tuple:
    """
    Differential Sarsa for the average-reward continuing setting.
    """

    # Initialize Q-values for every state-action pair
    Q = {(state, action): 0.0 for state, action in transitions}

    # Average reward estimate
    R_bar = 0.0

    def get_action(state):
        # Get all actions available from this state
        actions = [
            action for (s, action) in transitions
            if s == state
        ]

        # Greedy action with lexicographically smallest tie-break
        return min(actions, key=lambda action: (-Q[(state, action)], action))

    state = initial_state

    # Initial action
    action = get_action(state)

    for _ in range(num_steps):
        reward, next_state = transitions[(state, action)]

        # Select next action greedily
        next_action = get_action(next_state)

        # Differential TD error
        delta = (
            reward
            - R_bar
            + Q[(next_state, next_action)]
            - Q[(state, action)]
        )

        # Update average reward
        R_bar += beta * delta

        # Update Q-value
        Q[(state, action)] += alpha * delta

        # Move to next state/action
        state = next_state
        action = next_action

    return Q, R_bar