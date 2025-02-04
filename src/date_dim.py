import datetime

import pandas as pd
from mimesis import Fieldset
from mimesis.locales import Locale


def gen_date_dim(amount):
    fs = Fieldset(locale=Locale.EN, i=amount)
    dates = pd.DataFrame.from_dict(
        {
            "date": fs("datetime.date", start=2015, end=datetime.datetime.now().year),
        }
    )
    dates["date"] = pd.to_datetime(dates["date"])
    dates.insert(
        0, "date_id", dates["date"].astype(str).str.replace("-", "", regex=True)
    )
    dates["year"] = dates["date"].dt.year
    dates["month"] = dates["date"].dt.month
    dates["day"] = dates["date"].dt.day
    dates = dates.drop_duplicates(subset=["date_id"])
    return dates
