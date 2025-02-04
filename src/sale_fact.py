import pandas as pd
from mimesis import Fieldset
from mimesis.locales import Locale


def gen_sale_fact(
    amount, product_ids, customer_ids, employee_ids, date_ids, payment_ids, status_ids
):
    fs = Fieldset(locale=Locale.EN, i=amount)
    sales = pd.DataFrame.from_dict(
        {
            "sale_id": fs("uuid"),
            "product_id": fs("random.choice_enum_item", enum=product_ids),
            "customer_id": fs("random.choice_enum_item", enum=customer_ids),
            "employee_id": fs("random.choice_enum_item", enum=employee_ids),
            "date_id": fs("random.choice_enum_item", enum=date_ids),
            "payment_id": fs("random.choice_enum_item", enum=payment_ids),
            "status_id": fs("random.choice_enum_item", enum=status_ids),
            "quantity": fs("random.uniform", a=1, b=10, precision=0),
        }
    )
    return sales
