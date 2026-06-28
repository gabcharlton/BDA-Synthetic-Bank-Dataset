import numpy as np

def get_channel_prob(customer):
    """
    Simple behavioral segmentation logic
    """

    age = customer["age"]
    income = customer["income_band"]

    if age > 65:
        return [0.1, 0.2, 0.6, 0.1]  # branch heavy
    elif income == "high":
        return [0.6, 0.1, 0.2, 0.1]  # digital heavy
    else:
        return [0.4, 0.3, 0.2, 0.1]


def adjust_for_weather(weather):
    if weather == "snow":
        return 0.7  # fewer branch visits
    if weather == "rain":
        return 0.9
    return 1.0


def adjust_for_weekend(is_weekend):
    return 0.6 if is_weekend else 1.0
