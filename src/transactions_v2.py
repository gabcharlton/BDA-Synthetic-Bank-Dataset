import numpy as np
from src.behavior_engine_v2 import choose_channel, transaction_intensity
from src.context_effects import compute_context_multiplier

def generate_transactions(customers, accounts, calendar, states):

    transactions = []

    for _, day in calendar.iterrows():

        context_mult = compute_context_multiplier(day)

        daily_customers = customers.sample(n=200)

        for _, customer in daily_customers.iterrows():

            state = states[customer["customer_id"]]

            n_events = transaction_intensity(state)

            for _ in range(n_events):

                account = accounts[
                    accounts["customer_id"] == customer["customer_id"]
                ].sample(1).iloc[0]

                channel = choose_channel(state, context_mult)

                tx_type = np.random.choice([
                    "cash_in", "cash_out", "bill_payment",
                    "password_reset", "statement_request",
                    "transfer", "appointment_booking"
                ])

                amount = None
                if tx_type in ["cash_in", "cash_out", "transfer"]:
                    amount = round(np.random.lognormal(4, 1), 2)

                transactions.append({
                    "transaction_id": np.random.randint(1e8, 1e9),
                    "date": day["date"],
                    "customer_id": customer["customer_id"],
                    "account_id": account["account_id"],
                    "channel": channel,
                    "transaction_type": tx_type,
                    "amount": amount,
                    "digital_adoption_snapshot": state["digital_adoption_score"],
                    "branch_dependency_snapshot": state["branch_dependency"]
                })

    return transactions
