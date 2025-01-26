import customer_dim
import date_dim
import employee_dim
import payment_dim
import product_dim
import sale_fact
import status_dim
import supplier_dim


def main():
    customers = customer_dim.gen_customer_dim(1000)
    employees = employee_dim.gen_employee_dim(100)
    dates = date_dim.gen_date_dim(5000)
    status = status_dim.gen_status_dim()
    payments = payment_dim.gen_payment_dim()
    suppliers = supplier_dim.gen_supplier_dim(10)
    products = product_dim.gen_product_dim(500, suppliers["supplier_id"])
    sales = sale_fact.gen_sale_fact(
        10000,
        customers["customer_id"],
        employees["employee_id"],
        dates["date_id"],
        products["product_id"],
        payments["payment_id"],
        status["status_id"],
    )
    print(sales)


if __name__ == "__main__":
    main()
