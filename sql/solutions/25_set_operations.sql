SELECT customer_id AS id FROM orders WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31'
    EXCEPT
    SELECT customer_id FROM orders WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31'
    ORDER BY id;
