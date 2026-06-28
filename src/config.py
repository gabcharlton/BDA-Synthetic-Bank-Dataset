import numpy as np

SEED = 42
np.random.seed(SEED)

START_DATE = "2019-01-01"
END_DATE = "2024-12-31"

N_CUSTOMERS = 10000

BRANCHES = [
    {"branch_id": 1, "name": "Downtown Vancouver", "transit": "1001"},
    {"branch_id": 2, "name": "Gastown", "transit": "1002"},
    {"branch_id": 3, "name": "Yaletown", "transit": "1003"},
]

TRANSACTION_TYPES = {
    "financial": [
        "cash_in", "cash_out", "bill_payment", "credit_card_payment",
        "loan_payment", "draft_purchase", "transfer"
    ],
    "service": [
        "password_reset", "address_change", "debit_card_replacement",
        "cheque_order", "statement_request", "direct_deposit_setup",
        "appointment_booking"
    ]
}

CHANNELS = ["online", "atm", "branch", "phone"]
