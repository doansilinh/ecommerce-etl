import pandas as pd
from mimesis import Fieldset
from mimesis.locales import Locale


def gen_customer_dim(amount):
    fs = Fieldset(locale=Locale.EN, i=amount)
    customers = pd.DataFrame.from_dict(
        {
            "customer_id": fs("uuid"),
            "first_name": fs("person.first_name"),
            "last_name": fs("person.last_name"),
            "gender": fs("person.gender"),
            "birthday": fs("person.birthdate", min_year=1900, max_year=1980),
            "email": fs("person.email"),
            "phone": fs("person.phone_number", mask="09########"),
            "marital_status": fs(
                "random.weighted_choice",
                choices={
                    "single": 0.4,
                    "married": 0.4,
                    "divorced": 0.1,
                    "unknown": 0.1,
                },
            ),
            "education": fs("person.academic_degree"),
            "job": fs("person.occupation"),
            "nationality": fs("person.nationality"),
            "created_at": fs("datetime.date", start=2000, end=2005),
            "updated_at": fs("datetime.date", start=2010, end=2015),
            "is_active": fs("random.weighted_choice", choices={True: 0.9, False: 0.1}),
        }
    )
    customers["birthday"] = pd.to_datetime(customers["birthday"])
    customers["created_at"] = pd.to_datetime(customers["created_at"])
    customers["updated_at"] = pd.to_datetime(customers["updated_at"])

    return customers
