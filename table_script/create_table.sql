create table supplier_dim (
    supplier_id varchar(50) primary key,
    supplier_name varchar(50),
    supplier_type varchar(50),
    country varchar(50),
    email varchar(50),
    phone varchar(20)
);

create table product_dim (
    product_id varchar(50) primary key,
    product_name varchar(50),
    category varchar(50),
    supplier_id varchar(50),
    price decimal(10, 2),
    discount decimal(5, 2),
    foreign key (supplier_id) references supplier_dim(supplier_id)
);

create table customer_dim (
    customer_id varchar(50) primary key,
    first_name varchar(50),
    last_name varchar(50),
    gender varchar(10),
    birthday date,
    email varchar(50),
    phone varchar(20),
    marital_status varchar(20),
    education varchar(20),
    job varchar(50),
    nationality varchar(50),
    created_at date,
    is_active varchar(10)
);

create table employee_dim (
    employee_id varchar(50) primary key,
    employee_name varchar(50),
    email varchar(50),
    phone varchar(20),
    nationality varchar(50)
);

create table date_dim (
    date_id varchar(50) primary key,
    date date,
    year int,
    month int,
    day int
);

create table status_dim (
    status_id int primary key,
    status_name varchar(20)
);

create table payment_dim (
    payment_id int primary key,
    payment_method varchar(20)
);

create table sale_fact (
    sale_id varchar(50) primary key,
    product_id varchar(50),
    customer_id varchar(50),
    employee_id varchar(50),
    date_id varchar(50),
    payment_id int,
    status_id int,
    quantity int,
    foreign key (product_id) references product_dim(product_id),
    foreign key (customer_id) references customer_dim(customer_id),
    foreign key (employee_id) references employee_dim(employee_id),
    foreign key (date_id) references date_dim(date_id),
    foreign key (payment_id) references payment_dim(payment_id),
    foreign key (status_id) references status_dim(status_id)
);