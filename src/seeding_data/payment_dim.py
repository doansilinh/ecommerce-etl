import pandas as pd


def gen_payment_dim():
    payments = pd.DataFrame(
        [
            ["1", "Cash"],
            ["2", "Credit Card"],
            ["3", "Bank Transfer"],
            ["4", "Digital Wallet"],
        ],
        columns=["payment_id", "payment_method"],
    )
    return payments
