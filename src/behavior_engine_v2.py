import numpy as np

def choose_channel(state, context_mult):

    base = np.array([
        state["digital_adoption_score"],
        state["branch_dependency"],
        40,  # atm baseline
        20   # phone
    ])

    # apply context multipliers
    base[0] *= context_mult["digital"]
    base[1] *= context_mult["branch"]
    base[2] *= context_mult["atm"]

    # softmax for probability distribution
    exp_vals = np.exp(base / 20)
    probs = exp_vals / exp_vals.sum()

    return np.random.choice(
        ["online", "branch", "atm", "phone"],
        p=probs
    )


def transaction_intensity(state):
    """
    Controls how active a customer is.
    """

    base = np.random.poisson(
        lam=1 + (state["financial_stability"] / 50)
    )

    # high stress increases interactions
    if state["stress_level"] > 70:
        base += 2

    return max(1, base)
