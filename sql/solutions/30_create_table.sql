CREATE TABLE reviews (
        id          INTEGER PRIMARY KEY,
        product_id  INTEGER NOT NULL REFERENCES products(id),
        customer_id INTEGER NOT NULL REFERENCES customers(id),
        rating      INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
        comment     TEXT,
        created_at  TEXT NOT NULL DEFAULT CURRENT_DATE
    );
