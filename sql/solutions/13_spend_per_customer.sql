SELECT c.id AS customer_id,
           c.name,
           ROUND(COALESCE(SUM(oi.quantity * oi.unit_price), 0), 2) AS total_spent
    FROM customers c
    LEFT JOIN orders o ON o.customer_id = c.id AND o.status <> 'cancelled'
    LEFT JOIN order_items oi ON oi.order_id = o.id
    GROUP BY c.id, c.name
    ORDER BY total_spent DESC, c.id;
