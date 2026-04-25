CREATE SCHEMA sales;
SET search_path TO sales;
CREATE TABLE sales.region (
    region_id INTEGER PRIMARY KEY,
    region_name VARCHAR(50),
    comment VARCHAR(255)
);

CREATE TABLE sales.nation (
    nation_id INTEGER PRIMARY KEY,
    nation_name VARCHAR(50),
    region_id INTEGER,
    comment TEXT,
    FOREIGN KEY (region_id) REFERENCES region(region_id)
);

CREATE TABLE sales.supplier (
    supplier_id INTEGER PRIMARY KEY,
    supplier_name VARCHAR(100),
    address VARCHAR(255),
    nation_id INTEGER,
    phone VARCHAR(50),
    FOREIGN KEY (nation_id) REFERENCES nation(nation_id)
);

CREATE TABLE sales.part (
    part_id INTEGER PRIMARY KEY,
    part_name VARCHAR(100),
    manufacturer VARCHAR(100),
    size VARCHAR(100),
    retail_price NUMERIC(15,2)
);

CREATE TABLE sales.partsupp (
    part_id INTEGER,
    supplier_id INTEGER,
    avail_qty INTEGER,
    supply_price NUMERIC(20,10),
    PRIMARY KEY (part_id, supplier_id),
    FOREIGN KEY (part_id) REFERENCES part(part_id),
    FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id)
);

CREATE TABLE sales.customer (
    customer_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100),
    nation_id INTEGER,
    FOREIGN KEY (nation_id) REFERENCES nation(nation_id)
);

CREATE TABLE sales.orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    total_amount NUMERIC(12,2),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);

CREATE TABLE sales.lineitem (
    order_id INTEGER,
    part_id INTEGER,
    supplier_id INTEGER,
    quantity INTEGER,
    return_flag CHAR(1),
    discount NUMERIC(15,12),
    PRIMARY KEY (order_id, part_id, supplier_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (part_id) REFERENCES part(part_id),
    FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id),
    CHECK (discount >= 0.00 AND discount <= 1.00)
);
SET session_replication_role = replica;
Copy sales.region FROM 'D:/MySQL/MySQL Server 8.0/Uploads/region.csv' DELIMITER ',' CSV HEADER;
Copy sales.nation FROM 'D:/MySQL/MySQL Server 8.0/Uploads/nation.csv' DELIMITER ',' CSV HEADER;
Copy sales.supplier FROM 'D:/MySQL/MySQL Server 8.0/Uploads/supplier.csv' DELIMITER ',' CSV HEADER;
Copy sales.part FROM 'D:/MySQL/MySQL Server 8.0/Uploads/part.csv' DELIMITER ',' CSV HEADER;
Copy sales.partsupp FROM 'D:/MySQL/MySQL Server 8.0/Uploads/partsupp.csv' DELIMITER ',' CSV HEADER;
Copy sales.customer FROM 'D:/MySQL/MySQL Server 8.0/Uploads/customer.csv' DELIMITER ',' CSV HEADER;
Copy sales.orders FROM 'D:/MySQL/MySQL Server 8.0/Uploads/orders.csv' DELIMITER ',' CSV HEADER;
Copy sales.lineitem FROM 'D:/MySQL/MySQL Server 8.0/Uploads/lineitem.csv' DELIMITER ',' CSV HEADER;
SET session_replication_role = DEFAULT;
