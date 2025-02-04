import pandas as pd


def gen_status_dim():
    statuses = pd.DataFrame(
        [
            ["1", "Pending"],
            ["2", "Processing"],
            ["3", "Completed"],
            ["4", "Cancelled"],
        ],
        columns=["status_id", "status_name"],
    )
    return statuses
