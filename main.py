from src.customers import generate_customers
from src.branches import generate_branches
from src.accounts import generate_accounts
from src.events import generate_calendar
from src.transactions import generate_transactions

def main():

    print("Generating customers...")
    customers = generate_customers()

    print("Generating branches...")
    branches = generate_branches()

    print("Generating accounts...")
    accounts = generate_accounts(customers, branches)

    print("Generating calendar events...")
    calendar = generate_calendar()

    print("Generating transactions (this may take a while)...")
    transactions = generate_transactions(customers, accounts, calendar)

    print("Saving files...")

    customers.to_csv("data/customers.csv", index=False)
    branches.to_csv("data/branches.csv", index=False)
    accounts.to_csv("data/accounts.csv", index=False)
    calendar.to_csv("data/calendar.csv", index=False)
    transactions.to_csv("data/transactions.csv", index=False)

    print("Done.")

if __name__ == "__main__":
    main()
