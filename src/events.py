import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_calendar(start="2019-01-01", end="2024-12-31"):
    dates = pd.date_range(start, end)

    data = []

    for d in dates:
        month = d.month

        # seasonal weather proxy
        if month in [12, 1, 2]:
            weather = np.random.choice(["snow", "rain", "clear"], p=[0.3, 0.4, 0.3])
        elif month in [10, 11]:
            weather = np.random.choice(["rain", "wind", "clear"], p=[0.5, 0.2, 0.3])
        else:
            weather = np.random.choice(["clear", "rain"], p=[0.7, 0.3])

        holiday = d.weekday() >= 5  # simple proxy

        data.append({
            "date": d,
            "is_weekend": holiday,
            "weather_event": weather
        })

    return pd.DataFrame(data)
