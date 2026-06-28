import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime
from src.config import N_CUSTOMERS, SEED

fake = Faker()
Faker.seed(SEED)
np.random.seed(SEED)

def generate_customers():
    customers = []

    for i in range(N_CUSTOMERS):
        dob = fake.date_of_birth(minimum_age=18, maximum_age=85)
        age = datetime.today().year - dob.year

        income_band = np.random.choice(
            ["low", "mid", "high"], p=[0.4, 0.4, 0.2]
        )

        high_value = np.random.choice([0, 1], p=[0.9, 0.1])

        customers.append({
            "customer_id": 100000 + i,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "date_of_birth": dob,
            "age": age,
            "city": "Vancouver",
            "province": "BC",
            "country": "Canada",
            "income_band": income_band,
            "customer_since": fake.date_between(start_date="-10y", end_date="-1y"),
            "high_value_client": bool(high_value)
        })

    return pd.DataFrame(customers)
