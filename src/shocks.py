def get_pandemic_multiplier(date):
    """
    Simulates behavioral shifts over time.
    """

    year = date.year
    month = date.month

    # pre-pandemic
    if year == 2019:
        return {
            "branch": 1.0,
            "digital": 1.0,
            "atm": 1.0
        }

    # pandemic shock (2020)
    if year == 2020:
        if month < 3:
            return {"branch": 1.0, "digital": 1.0, "atm": 1.0}

        return {
            "branch": 0.4,
            "digital": 1.6,
            "atm": 0.8
        }

    # recovery phase (2021)
    if year == 2021:
        return {
            "branch": 0.7,
            "digital": 1.3,
            "atm": 0.9
        }

    # post-pandemic stabilization
    return {
        "branch": 0.8,
        "digital": 1.2,
        "atm": 1.0
    }
