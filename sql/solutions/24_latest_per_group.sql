WITH ranked AS (
        SELECT c.name AS customer, o.id AS order_id, o.order_date,
               ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY o.order_date DESC, o.id DESC) AS rn
        FROM customers c
        JOIN orders o ON o.customer_id = c.id
    )
    SELECT customer, order_id, order_date
    FROM ranked
    WHERE rn = 1
    ORDER BY customer;
