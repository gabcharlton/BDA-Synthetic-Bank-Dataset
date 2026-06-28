import numpy as np

def initialize_customer_state(customer):
    """
    Each customer gets a dynamic behavioral state.
    """

    age = customer["age"]
    income = customer["income_band"]

    # baseline digital adoption
    if age < 30:
        digital = np.random.normal(70, 10)
    elif age < 55:
        digital = np.random.normal(55, 15)
    else:
        digital = np.random.normal(35, 15)

    # income adjustment
    if income == "high":
        digital += 10
    elif income == "low":
        digital -= 5

    return {
        "digital_adoption_score": np.clip(digital, 0, 100),
        "branch_dependency": np.clip(100 - digital, 0, 100),
        "stress_level": np.random.normal(30, 10),
        "financial_stability": np.random.normal(60, 20),
        "trust_in_digital": np.random.normal(60, 15),
        "life_stage": "stable"
    }
