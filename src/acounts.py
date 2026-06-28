import pandas as pd
import numpy as np
from faker import Faker
from src.config import SEED

fake = Faker()
Faker.seed(SEED)
np.random.seed(SEED)

ACCOUNT_TYPES = [
    "chequing", "savings", "credit_card",
    "line_of_credit", "business"
]

def generate_accounts(customers_df, branches_df):
    accounts = []

    for _, row in customers_df.iterrows():
        n_accounts = np.random.randint(1, 4)

        for _ in range(n_accounts):
            accounts.append({
                "account_id": fake.unique.random_int(min=1000000, max=9999999),
                "customer_id": row["customer_id"],
                "account_type": np.random.choice(ACCOUNT_TYPES),
                "opened_date": fake.date_between(
                    start_date=row["customer_since"], end_date="today"
                ),
                "transit_number": np.random.choice(branches_df["transit"]),
                "balance": round(np.random.normal(5000, 2000), 2),
                "currency": "CAD"
            })

    return pd.DataFrame(accounts)
