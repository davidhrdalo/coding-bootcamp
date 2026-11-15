-- The sample database used by every exercise.
--
--   customers ----< orders ----< order_items >---- products
--   employees (manager_id points back at employees.id)
--   page_views (a small counter table, used for the upsert exercise)
--
-- Dates are text in ISO format: 'YYYY-MM-DD'. Money is a decimal number.

CREATE TABLE customers (
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    email       TEXT,                 -- may be NULL
    country     TEXT NOT NULL,
    signup_date TEXT NOT NULL
);

CREATE TABLE products (
    id       INTEGER PRIMARY KEY,
    name     TEXT NOT NULL,
    category TEXT NOT NULL,
    price    REAL NOT NULL,
    stock    INTEGER NOT NULL
);

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    order_date  TEXT NOT NULL,
    status      TEXT NOT NULL CHECK (status IN ('pending', 'shipped', 'delivered', 'cancelled'))
);

CREATE TABLE order_items (
    id         INTEGER PRIMARY KEY,
    order_id   INTEGER NOT NULL REFERENCES orders(id),
    product_id INTEGER NOT NULL REFERENCES products(id),
    quantity   INTEGER NOT NULL CHECK (quantity > 0),
    unit_price REAL NOT NULL,         -- the price at the time of the order
    UNIQUE (order_id, product_id)
);

CREATE TABLE employees (
    id         INTEGER PRIMARY KEY,
    name       TEXT NOT NULL,
    department TEXT NOT NULL,
    salary     INTEGER NOT NULL,
    manager_id INTEGER REFERENCES employees(id),   -- NULL for the top person
    hire_date  TEXT NOT NULL
);

CREATE TABLE page_views (
    page  TEXT PRIMARY KEY,
    views INTEGER NOT NULL
);
