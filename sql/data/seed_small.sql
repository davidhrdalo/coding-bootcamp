-- A small, readable data set. Open this file and look at the rows before you write queries.

INSERT INTO customers (id, name, email, country, signup_date) VALUES
  (1,  'Alice Archer', 'alice@example.com', 'Australia',      '2022-03-14'),
  (2,  'Ben Brooks',   'ben@example.com',   'Australia',      '2022-07-01'),
  (3,  'Chloe Chen',   NULL,                'New Zealand',    '2022-09-30'),
  (4,  'Aaron Adams',  'aaron@example.com', 'New Zealand',    '2023-01-12'),
  (5,  'Dana Diaz',    'dana@example.com',  'Canada',         '2023-02-20'),
  (6,  'Eli Evans',    NULL,                'Canada',         '2023-05-05'),
  (7,  'Fiona Fox',    'fiona@example.com', 'United Kingdom', '2023-08-19'),
  (8,  'Greg Grant',   'greg@example.com',  'United Kingdom', '2024-01-08'),
  (9,  'Hana Hill',    'hana@example.com',  'United States',  '2024-02-25'),
  (10, 'Ivan Ito',     NULL,                'Australia',      '2024-04-02'),
  (11, 'Jade Jones',   'jade@example.com',  'Ireland',        '2024-05-01');

INSERT INTO products (id, name, category, price, stock) VALUES
  (1,  'Python Basics',       'Books',       15.00,  40),
  (2,  'SQL Cookbook',        'Books',       24.50,  25),
  (3,  'Data Structures',     'Books',       45.00,   8),
  (4,  'USB-C Cable',         'Electronics',  9.99, 120),
  (5,  'Wireless Mouse',      'Electronics', 29.99,  60),
  (6,  'Mechanical Keyboard', 'Electronics', 89.00,   5),
  (7,  'Desk Lamp',           'Home',        34.00,  15),
  (8,  'Coffee Mug',          'Home',         8.50, 200),
  (9,  'Puzzle Set',          'Toys',        19.99,  30),
  (10, 'Board Game',          'Toys',        39.99,  12);

INSERT INTO orders (id, customer_id, order_date, status) VALUES
  (1,  1, '2023-02-10', 'delivered'),
  (2,  1, '2023-11-05', 'delivered'),
  (3,  2, '2023-03-22', 'delivered'),
  (4,  3, '2023-06-18', 'cancelled'),
  (5,  4, '2023-07-30', 'delivered'),
  (6,  5, '2023-12-12', 'delivered'),
  (7,  5, '2024-01-20', 'shipped'),
  (8,  6, '2024-02-14', 'pending'),
  (9,  7, '2024-03-03', 'delivered'),
  (10, 7, '2024-03-28', 'delivered'),
  (11, 8, '2024-05-17', 'cancelled'),
  (12, 9, '2024-06-09', 'shipped'),
  (13, 2, '2024-07-21', 'delivered'),
  (14, 1, '2024-09-15', 'pending');

INSERT INTO order_items (id, order_id, product_id, quantity, unit_price) VALUES
  (1,  1,  1, 1, 15.00), (2,  1,  4, 2,  9.99),
  (3,  2,  6, 1, 89.00), (4,  2,  5, 1, 29.99),
  (5,  3,  2, 1, 24.50), (6,  3,  8, 2,  8.50),
  (7,  4,  9, 1, 19.99),
  (8,  5,  7, 1, 34.00), (9,  5,  1, 2, 15.00),
  (10, 6,  3, 1, 45.00), (11, 6,  2, 1, 24.50),
  (12, 7,  5, 2, 29.99),
  (13, 8,  4, 3,  9.99), (14, 8,  8, 1,  8.50),
  (15, 9,  6, 1, 89.00), (16, 9,  3, 1, 45.00),
  (17, 10, 1, 1, 15.00), (18, 10, 9, 2, 19.99),
  (19, 11, 7, 1, 34.00),
  (20, 12, 5, 1, 29.99), (21, 12, 4, 1,  9.99),
  (22, 13, 2, 2, 24.50), (23, 13, 1, 1, 15.00),
  (24, 14, 8, 4,  8.50), (25, 14, 9, 1, 19.99);

INSERT INTO employees (id, name, department, salary, manager_id, hire_date) VALUES
  (1,  'Nora Quinn', 'Executive',   250000, NULL, '2015-01-05'),
  (2,  'Omar Patel', 'Engineering', 180000, 1,    '2016-03-01'),
  (3,  'Priya Shah', 'Sales',       160000, 1,    '2016-05-10'),
  (4,  'Quinn Lee',  'Engineering', 130000, 2,    '2018-02-12'),
  (5,  'Rosa Diaz',  'Engineering', 130000, 2,    '2019-09-09'),
  (6,  'Sam Wu',     'Engineering', 110000, 4,    '2021-04-19'),
  (7,  'Tara Ng',    'Sales',        95000, 3,    '2020-06-01'),
  (8,  'Uma Roy',    'Sales',        90000, 3,    '2022-08-15'),
  (9,  'Vik Rao',    'Marketing',   100000, 1,    '2019-01-21'),
  (10, 'Wen Zhao',   'Marketing',    85000, 9,    '2023-02-27');

INSERT INTO page_views (page, views) VALUES ('/home', 10), ('/about', 3);
