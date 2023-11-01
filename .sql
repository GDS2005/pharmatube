CREATE TABLE products (
    product_name VARCHAR(255),
    category VARCHAR(255),
    manufacturer VARCHAR(255),
    dosage VARCHAR(50),
    price DECIMAL(10, 2),
    quantity_in_stock INT,
    expiration_date DATE,
    supplier_id INT,
    supplier_name VARCHAR(255),
    supplier_contact VARCHAR(20),
    date_received DATE,
    PRIMARY KEY (product_name)
);

/* Test Cases */

INSERT INTO products 
(product_name, category, manufacturer, dosage, price, quantity_in_stock, expiration_date, supplier_id, supplier_name, supplier_contact, date_received) 
VALUES 
('Aspirin', 'Medicine', 'Bayer', '500mg', 5.99, 100, '2023-12-31', 1, 'Pharma Co', '555-555-5555', '2023-10-30');

/* Locally, we need to install psycopg*/