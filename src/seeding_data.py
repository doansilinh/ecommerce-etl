from sqlalchemy import create_engine

import customer_dim
import date_dim
import employee_dim
import payment_dim
import product_dim
import sale_fact
import status_dim
import supplier_dim

username = "mysql1"
password = "mysql1"
database = "mysql1"
host = "localhost:3306"


def main():
    mysql = create_engine(
        f"mysql+mysqlconnector://{username}:{password}@{host}/{database}"
    )

    customers = customer_dim.gen_customer_dim(1000)
    employees = employee_dim.gen_employee_dim(100)
    dates = date_dim.gen_date_dim(5000)
    status = status_dim.gen_status_dim()
    payments = payment_dim.gen_payment_dim()
    suppliers = supplier_dim.gen_supplier_dim(10)
    products = product_dim.gen_product_dim(500, suppliers["supplier_id"])
    sales = sale_fact.gen_sale_fact(
        10000,
        products["product_id"],
        customers["customer_id"],
        employees["employee_id"],
        dates["date_id"],
        payments["payment_id"],
        status["status_id"],
    )

    suppliers.to_sql("supplier_dim", con=mysql, if_exists="append", index=False)
    products.to_sql("product_dim", con=mysql, if_exists="append", index=False)
    customers.to_sql("customer_dim", con=mysql, if_exists="append", index=False)
    employees.to_sql("employee_dim", con=mysql, if_exists="append", index=False)
    dates.to_sql("date_dim", con=mysql, if_exists="append", index=False)
    status.to_sql("status_dim", con=mysql, if_exists="append", index=False)
    payments.to_sql("payment_dim", con=mysql, if_exists="append", index=False)
    sales.to_sql("sale_fact", con=mysql, if_exists="append", index=False)

    mysql.dispose()


if __name__ == "__main__":
    main()
