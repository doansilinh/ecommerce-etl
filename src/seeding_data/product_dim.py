import pandas as pd
from mimesis import Fieldset
from mimesis.locales import Locale


def gen_product_dim(amount, supplier_ids):
    amount_per_category = amount // 5
    fs = Fieldset(locale=Locale.EN, i=amount_per_category)
    products1 = pd.DataFrame.from_dict(
        {
            "product_id": fs("uuid"),
            "name": fs("food.dish"),
            "category": "dish",
            "supplier_id": fs("random.choice_enum_item", enum=supplier_ids),
            "price": fs("random.uniform", a=50000, b=200000, precision=0),
            "discount": fs("random.uniform", a=0, b=40, precision=0),
        }
    )
    products2 = pd.DataFrame.from_dict(
        {
            "product_id": fs("uuid"),
            "name": fs("food.drink"),
            "category": "drink",
            "supplier_id": fs("random.choice_enum_item", enum=supplier_ids),
            "price": fs("random.uniform", a=50000, b=200000, precision=0),
            "discount": fs("random.uniform", a=0, b=40, precision=0),
        }
    )
    products3 = pd.DataFrame.from_dict(
        {
            "product_id": fs("uuid"),
            "name": fs("food.fruit"),
            "category": "fruit",
            "supplier_id": fs("random.choice_enum_item", enum=supplier_ids),
            "price": fs("random.uniform", a=50000, b=200000, precision=0),
            "discount": fs("random.uniform", a=0, b=40, precision=0),
        }
    )
    products4 = pd.DataFrame.from_dict(
        {
            "product_id": fs("uuid"),
            "name": fs("food.spices"),
            "category": "spices",
            "supplier_id": fs("random.choice_enum_item", enum=supplier_ids),
            "price": fs("random.uniform", a=50000, b=200000, precision=0),
            "discount": fs("random.uniform", a=0, b=40, precision=0),
        }
    )
    products5 = pd.DataFrame.from_dict(
        {
            "product_id": fs("uuid"),
            "name": fs("food.vegetable"),
            "category": "vegetable",
            "supplier_id": fs("random.choice_enum_item", enum=supplier_ids),
            "price": fs("random.uniform", a=50000, b=200000, precision=0),
            "discount": fs("random.uniform", a=0, b=40, precision=0),
        }
    )
    products = pd.concat(
        [products1, products2, products3, products4, products5], ignore_index=True
    )
    return products
