def compute_context_multiplier(event):
    """
    Converts real-world context into behavioral impact.
    """

    multiplier = {
        "branch": 1.0,
        "digital": 1.0,
        "atm": 1.0
    }

    # weather effects
    if event["weather_event"] == "snow":
        multiplier["branch"] = 0.6
        multiplier["atm"] = 0.8

    if event["weather_event"] == "heavy_rain":
        multiplier["branch"] = 0.85

    # weekends
    if event["is_weekend"]:
        multiplier["branch"] *= 0.7
        multiplier["atm"] *= 1.1

    # sports events (downtown Vancouver effect)
    if event.get("sports_event") == "NHL_game":
        multiplier["atm"] *= 1.3
        multiplier["digital"] *= 0.95

    return multiplier
