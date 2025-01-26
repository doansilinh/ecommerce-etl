import pandas as pd
from mimesis import Fieldset
from mimesis.locales import Locale


def gen_supplier_dim(amount):
    fs = Fieldset(locale=Locale.EN, i=amount)
    suppliers = pd.DataFrame.from_dict(
        {
            "supplier_id": fs("uuid"),
            "name": fs("finance.company"),
            "type": fs("finance.company_type"),
            "country": fs("person.nationality"),
            "email": fs("person.email"),
            "phone": fs("person.phone_number", mask="09########"),
        }
    )
    return suppliers
