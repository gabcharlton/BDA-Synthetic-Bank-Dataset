import numpy as np

def update_life_stage(state, customer_age, year):

    if customer_age < 30:
        return "young_professional"

    if 30 <= customer_age < 50:
        return "mid_career"

    if 50 <= customer_age < 65:
        return "pre_retirement"

    return "retired"


def apply_life_drift(state):
    """
    Slowly changes behavior over time.
    """

    # digital adoption naturally increases over time
    state["digital_adoption_score"] += np.random.normal(0.2, 0.5)

    # trust increases slowly with exposure
    state["trust_in_digital"] += np.random.normal(0.1, 0.3)

    # branch dependency decays
    state["branch_dependency"] -= np.random.normal(0.2, 0.5)

    # clamp values
    for k in state:
        if isinstance(state[k], (int, float)):
            state[k] = max(0, min(100, state[k]))

    return state
