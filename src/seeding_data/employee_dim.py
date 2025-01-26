import pandas as pd
from mimesis import Fieldset
from mimesis.locales import Locale


def gen_employee_dim(amount):
    fs = Fieldset(locale=Locale.EN, i=amount)
    employees = pd.DataFrame.from_dict(
        {
            "employee_id": fs("uuid"),
            "name": fs("person.name"),
            "email": fs("person.email"),
            "phone": fs("person.phone_number", mask="09########"),
            "nationality": fs("person.nationality"),
        }
    )
    return employees
