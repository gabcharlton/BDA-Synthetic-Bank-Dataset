from src.customers import generate_customers
from src.accounts import generate_accounts
from src.branches import generate_branches
from src.events import generate_calendar
from src.customer_state import initialize_customer_state
from src.lifecycle import apply_life_drift
from src.transactions_v2 import generate_transactions

def main():

    customers = generate_customers()
    branches = generate_branches()
    accounts = generate_accounts(customers, branches)
    calendar = generate_calendar()

    # initialize state memory
    states = {
        row["customer_id"]: initialize_customer_state(row)
        for _, row in customers.iterrows()
    }

    print("Simulating behavioral evolution...")

    # optional: evolve state over time
    for customer_id in states:
        states[customer_id] = apply_life_drift(states[customer_id])

    print("Generating transactions...")
    transactions = generate_transactions(customers, accounts, calendar, states)

    import pandas as pd
    pd.DataFrame(transactions).to_csv("data/transactions_v2.csv", index=False)

    print("Done.")

if __name__ == "__main__":
    main()
