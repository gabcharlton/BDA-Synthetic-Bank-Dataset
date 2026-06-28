import pandas as pd
import numpy as np
from datetime import timedelta
from src.config import TRANSACTION_TYPES, CHANNELS
from src.behavior_engine import get_channel_prob, adjust_for_weather

def generate_transactions(customers, accounts, calendar):

    transactions = []

    for _, day in calendar.iterrows():

        daily_customers = customers.sample(n=200)  # simulate daily activity

        for _, customer in daily_customers.iterrows():

            customer_accounts = accounts[
                accounts["customer_id"] == customer["customer_id"]
            ]

            if customer_accounts.empty:
                continue

            account = customer_accounts.sample(1).iloc[0]

            channel_probs = get_channel_prob(customer)
            channel = np.random.choice(CHANNELS, p=channel_probs)

            tx_type = np.random.choice(
                TRANSACTION_TYPES["financial"] + TRANSACTION_TYPES["service"]
            )

            amount = None
            if tx_type in TRANSACTION_TYPES["financial"]:
                amount = round(np.random.exponential(100), 2)

            transactions.append({
                "transaction_id": np.random.randint(100000000, 999999999),
                "transaction_datetime": day["date"],
                "customer_id": customer["customer_id"],
                "account_id": account["account_id"],
                "channel": channel,
                "transaction_type": tx_type,
                "amount": amount,
                "weather_event": day["weather_event"],
                "is_weekend": day["is_weekend"]
            })

    return pd.DataFrame(transactions)
