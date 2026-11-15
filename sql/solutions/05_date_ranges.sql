SELECT id, order_date
    FROM orders
    WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31' AND status <> 'cancelled'
    ORDER BY order_date, id;
